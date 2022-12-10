# -*- coding: utf-8 -*-

import tele
import tele.modules.registry
from tele.tools.translate import _
from tele.exceptions import AccessError
from tele.applets.web.controllers.main import ensure_db, Home
from tele import http
from tele.http import request

import os
import logging

_logger = logging.getLogger(__name__)

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
db_monodb = http.db_monodb


class TeleHome(tele.applets.web.controllers.main.Home):
    '''
    inhere home to extend web.login style
    '''

    @http.route('/web/login', type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        '''
        rewrtie the login go support login style
        :param redirect:
        :param kw:
        :return:
        '''
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            return request.redirect(redirect)

        if not request.uid:
            request.uid = tele.SUPERUSER_ID

        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except tele.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            old_uid = request.uid
            try:
                uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
                request.params['login_success'] = True
                return request.redirect(self._login_redirect(uid, redirect=redirect))
            except tele.exceptions.AccessDenied as e:
                request.uid = old_uid
                if e.args == tele.exceptions.AccessDenied().args:
                    values['error'] = _("Wrong login/password")
                else:
                    values['error'] = e.args[0]
        else:
            if 'error' in request.params and request.params.get('error') == 'access':
                values['error'] = _('Only employees can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
            values['login'] = request.session.get('auth_login')

        if not tele.tools.config['list_db']:
            values['disable_database_manager'] = True

        # add extra info to login page
        ir_config = request.env['ir.config_parameter'].sudo()
        login_style = ir_config.get_param(
            key='tele_login.login_style', default='login_style1')
        login_template = 'tele_login.{login_style}'.format(login_style=login_style)
        
        # add extra info to login page
        values['title'] = ir_config.get_param(
            "tele_theme_setting.window_default_title", "Tele")
        values['powered_by'] = ir_config.get_param("powered_by", "Tele")

        response = request.render(login_template, values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response
