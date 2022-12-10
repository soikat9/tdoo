# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from tele import api, models


class MailRenderMixin(models.AbstractModel):
    _inherit = "mail.render.mixin"

    @api.model
    def _render_template_postprocess(self, rendered):
        # super will transform relative url to absolute
        rendered = super(MailRenderMixin, self)._render_template_postprocess(rendered)

        # apply shortener after
        if self.env.context.get('post_convert_links'):
            for res_id, html in rendered.items():
                rendered[res_id] = self._shorten_links(
                    html,
                    self.env.context['post_convert_links'],
                    blacklist=['/unsubscribe_from_list', '/view']
                )
        return rendered
