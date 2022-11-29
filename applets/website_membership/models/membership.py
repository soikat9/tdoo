# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import models

class MembershipLine(models.Model):

    _inherit = 'membership.membership_line'

    def _get_published_companies(self, limit=None):
        if not self.ids:
            return []
        limit_clause = '' if limit is None else ' LIMIT %d' % limit
        self.env.cr.execute("""
            SELECT DISTINCT p.id
            FROM res_partner p INNER JOIN membership_membership_line m
            ON  p.id = m.partner
            WHERE is_published AND is_company AND m.id IN %s """ + limit_clause, (tuple(self.ids),))
        return [partner_id[0] for partner_id in self.env.cr.fetchall()]
