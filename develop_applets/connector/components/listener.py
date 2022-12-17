# Copyright 2013 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

"""
Listeners
=========

Listeners are Components notified when events happen.
Documentation in :mod:`tele.applets.component_event.components.event`

The base listener for the connectors add a method
:meth:`ConnectorListener.no_connector_export` which can be used with
:func:`tele.applets.component_event.skip_if`.


"""

from tele.applets.component.core import AbstractComponent


class ConnectorListener(AbstractComponent):
    """Base Backend Adapter for the connectors"""

    _name = "base.connector.listener"
    _inherit = ["base.connector", "base.event.listener"]

    def no_connector_export(self, record):
        """Return if the 'connector_no_export' has been set in context

        To be used with :func:`tele.applets.component_event.skip_if`
        on Events::

            from tele.applets.component.core import Component
            from tele.applets.component_event import skip_if


            class MyEventListener(Component):
                _name = 'my.event.listener'
                _inherit = 'base.connector.event.listener'
                _apply_on = ['magento.res.partner']

                @skip_if(lambda: self, record, *args, **kwargs:
                         self.no_connector_export(record))
                def on_record_write(self, record, fields=None):
                    record.with_delay().export_record()

        """
        return record.env.context.get("no_connector_export") or record.env.context.get(
            "connector_no_export"
        )
