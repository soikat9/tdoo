# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class Department(models.Model):
    _inherit = 'hr.department'

    def name_get(self):
        # Get department name using superuser, because model is not accessible
        # for portal users
        self_sudo = self.sudo()
        return super(Department, self_sudo).name_get()
