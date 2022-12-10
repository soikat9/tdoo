# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models


class IrUiMenu(models.Model):
    _inherit = 'ir.ui.menu'

    def _load_menus_blacklist(self):
        res = super()._load_menus_blacklist()
        if self.env.user.has_group('hr_attendance.group_hr_attendance_user'):
            res.append(self.env.ref('hr_attendance.menu_hr_attendance_attendances_overview').id)
        return res
