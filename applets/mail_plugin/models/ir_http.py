# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from werkzeug.exceptions import BadRequest

from tele import models
from tele.http import request

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _auth_method_outlook(cls):
        access_token = request.httprequest.headers.get('Authorization')
        if not access_token:
            raise BadRequest('Access token missing')

        if access_token.startswith('Bearer '):
            access_token = access_token[7:]

        user_id = request.env["res.users.apikeys"]._check_credentials(scope='tele.plugin.outlook', key=access_token)
        if not user_id:
            raise BadRequest('Access token invalid')

        # take the identity of the API key user
        request.uid = user_id
