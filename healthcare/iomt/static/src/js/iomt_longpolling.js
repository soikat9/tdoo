tele.define('iomt.IoMTLongpolling', function (require) {
'use strict';

var core = require('web.core');
var BusService = require('bus.BusService');
var IoMTConnectionMixin = require('iomt.mixins').IoMTConnectionMixin;

var IoMTLongpolling = BusService.extend(IoMTConnectionMixin, {
    // constants
    POLL_TIMEOUT: 60000,
    POLL_ROUTE: '/hw_drivers/event',
    ACTION_TIMEOUT: 6000,
    ACTION_ROUTE: '/hw_drivers/action',

    RPC_DELAY: 1500,
    MAX_RPC_DELAY: 1500 * 10,

    _retries: 0,

    /**
     * @override
     */
    init: function () {
        this._super.apply(this, arguments);
        this._session_id = this._createUUID();
        this._listeners = {};
        this._delayedStartPolling(this.RPC_DELAY);
    },

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------
    /**
     * Add a device_identifier to listeners[iomt_ip] and restart polling
     *
     * @param {String} iomt_ip
     * @param {Array} devices list of devices
     * @param {Callback} callback
     */
    addListener: function (iomt_ip, devices, listener_id, callback) {
        if (!this._listeners[iomt_ip]) {
            this._listeners[iomt_ip] = {
                last_event: 0,
                devices: {},
                session_id: this._session_id,
                rpc: false,
            };
        }
        for (var device in devices) {
            this._listeners[iomt_ip].devices[devices[device]] = {
                listener_id: listener_id,
                device_identifier: devices[device],
                callback: callback,
            };
        }
        this.stopPolling(iomt_ip);
        this.startPolling(iomt_ip);
        return Promise.resolve();
    },
    /**
     * Stop listening to iomt device with id `device_identifier`
     * @param {string} iomt_ip
     * @param {string} device_identifier
     */
    removeListener: function(iomt_ip, device_identifier, listener_id) {
        if (this._listeners[iomt_ip].devices[device_identifier].listener_id === listener_id) {
            delete this._listeners[iomt_ip].devices[device_identifier];
        }
    },
    /**
     * Execute a action on device_identifier
     * Action depend of driver that support the device
     *
     * @param {String} iomt_ip
     * @param {String} device_identifier
     * @param {Object} data contains the information needed to perform an action on this device_identifier
     */
    action: function (iomt_ip, device_identifier, data) {
        this.protocol = window.location.protocol;
        var self = this;
        var data = {
            params: {
                session_id: self._session_id,
                device_identifier: device_identifier,
                data: JSON.stringify(data),
            }
        };
        var options = {
            timeout: this.ACTION_TIMEOUT,
        };
        var prom = new Promise(function(resolve, reject) {
            self._rpcIoMT(iomt_ip, self.ACTION_ROUTE, data, options)
                .then(resolve)
                .fail(reject);
        });
        return prom;
    },

    /**
     * Start a long polling, i.e. it continually opens a long poll
     * connection as long as it is not stopped (@see `stopPolling`)
     */
    startPolling: function (iomt_ip) {
        if (iomt_ip) {
            if (!this._listeners[iomt_ip].rpc) {
                this._poll(iomt_ip);
            }
        } else {
            var self = this;
            _.each(this._listeners, function (listener, ip) {
                self.startPolling(ip);
            });
        }
    },
    /**
     * Stops any started long polling
     *
     * Aborts a pending longpoll so that we immediately remove ourselves
     * from listening on notifications on this channel.
     */
    stopPolling: function (iomt_ip) {
        if (this._listeners[iomt_ip].rpc) {
            this._listeners[iomt_ip].rpc.abort();
            this._listeners[iomt_ip].rpc = false;
        }
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------
    _delayedStartPolling: function (delay){
        var self = this;
        setTimeout(function (){
            self.startPolling();
        }, delay);
    },

    _createUUID: function () {
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 36; i++) {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
        s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
        s[8] = s[13] = s[18] = s[23] = "-";
        return s.join("");
    },
    /**
     * Execute a RPC to the box
     * Used to do polling or an action
     *
     * @param {String} iomt_ip
     * @param {String} route
     * @param {Object} data information needed to perform an action or the listener for the polling
     * @param {Object} options.timeout
     */
    _rpcIoMT: function (iomt_ip, route, data, options) {
        this.protocol = window.location.protocol;
        var port = this.protocol === 'http:' ? ':9000' : '';
        var url = this.protocol + '//' + iomt_ip + port;
        var queryOptions = _.extend({
            url: url + route,
            dataType: 'json',
            contentType: "application/json;charset=utf-8",
            data: JSON.stringify(data),
            method: 'POST',
        }, options);
        var request = $.ajax(queryOptions);
        if (this._listeners[iomt_ip] && route === '/hw_drivers/event') {
            this._listeners[iomt_ip].rpc = request;
            return this._listeners[iomt_ip].rpc;
        } else {
            return request;
        }
    },
    /**
     * Make a request to an IoMT Box
     *
     * @param {String} iomt_ip
     */
    _poll: function (iomt_ip) {
        var self = this;
        var listener = this._listeners[iomt_ip];
        var data = {
            params: {
                listener: listener,
            }
        };
        var options = {
            timeout: this.POLL_TIMEOUT,
        };

        // The backend has a maximum cycle time of 50 seconds so give +10 seconds
        this._rpcIoMT(iomt_ip, this.POLL_ROUTE, data, options)
            .then(function (result) {
                self._retries = 0;
                self._listeners[iomt_ip].rpc = false;
                if (result.result) {
                    if (self._session_id === result.result.session_id) {
                        self._onSuccess(iomt_ip, result.result);
                    }
                } else if (!_.isEmpty(self._listeners[iomt_ip].devices)) {
                    self._poll(iomt_ip);
                }
            }).fail(function (jqXHR, textStatus) {
                if (textStatus === 'error') {
                    self._doWarnFail(iomt_ip);
                } else {
                    self._onError();
                }
            });
    },

    _onSuccess: function (iomt_ip, result){
        this._listeners[iomt_ip].last_event = result.time;

        var devices = this._listeners[iomt_ip].devices;
        if (devices[result.device_identifier]) {
            devices[result.device_identifier].callback(result);
        }
        if (!_.isEmpty(devices)) {
            this._poll(iomt_ip);
        }
        this._retries = 0;
    },

    _onError: function (){
        this._retries++;
        this._delayedStartPolling(Math.min(this.RPC_DELAY * this._retries, this.MAX_RPC_DELAY));
    },
});

core.serviceRegistry.add('iomt_longpolling', IoMTLongpolling);

return IoMTLongpolling;

});
