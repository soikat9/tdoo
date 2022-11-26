# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _get_default_appraisal_survey_template_id(self):
        return self.env.ref('hr_appraisal_survey.appraisal_feedback_template', raise_if_not_found=False)

    appraisal_survey_template_id = fields.Many2one('survey.survey')
