# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class HrContractEmployeeReport(models.Model):
    _inherit = "hr.contract.employee.report"

    final_yearly_costs = fields.Float('Annual Employee Budget', group_operator="avg", readonly=True)

    def _query(self, fields='', from_clause='', outer=''):
        fields += """
            , c.final_yearly_costs AS final_yearly_costs"""

        return super(HrContractEmployeeReport, self)._query(fields, from_clause, outer)
