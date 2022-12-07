# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

import base64
import logging
from collections import defaultdict
from hashlib import sha512
from secrets import choice

from tele import _, api, fields, models, tools, Command
from tele.applets.base.models.avatar_mixin import get_hsl_from_seed
from tele.exceptions import UserError, ValidationError
from tele.osv import expression
from tele.tools import html_escape
from tele.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT

_logger = logging.getLogger(__name__)

channel_avatar = '''<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M0 2.1645H9.09091V7.27273C9.09091 8.27688 8.27688 9.09091 7.27273 9.09091H1.81818C0.814028 9.09091 0 8.27688 0 7.27273V2.1645Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M0 1.81818C0 0.814028 0.814028 0 1.81818 0H7.27273C8.27688 0 9.09091 0.814028 9.09091 1.81818V2.1645H0V1.81818Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M4.54544 4.22074C5.50176 4.22074 6.27704 3.44548 6.27704 2.48914C6.27704 1.5328 5.50176 0.757539 4.54544 0.757539C3.58911 0.757539 2.81384 1.5328 2.81384 2.48914C2.81384 3.44548 3.58911 4.22074 4.54544 4.22074Z" fill="url(#paint0_linear_64_298)"/>
<path d="M4.54544 4.87011C2.87184 4.87011 1.51513 6.22682 1.51513 7.90041V8.54976C1.51513 8.78894 1.70886 8.98266 1.94803 8.98266H7.14284C7.38202 8.98266 7.57574 8.78894 7.57574 8.54976V7.90041C7.57574 6.22682 6.21903 4.87011 4.54544 4.87011Z" fill="url(#paint1_linear_64_298)"/>
<path d="M10.9091 2.1645H20V7.27273C20 8.27688 19.186 9.09091 18.1818 9.09091H12.7273C11.7231 9.09091 10.9091 8.27688 10.9091 7.27273V2.1645Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M10.9091 1.81818C10.9091 0.814028 11.7231 0 12.7273 0H18.1818C19.186 0 20 0.814028 20 1.81818V2.1645H10.9091V1.81818Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M15.4545 4.22074C16.4109 4.22074 17.1861 3.44548 17.1861 2.48914C17.1861 1.5328 16.4109 0.757539 15.4545 0.757539C14.4982 0.757539 13.7229 1.5328 13.7229 2.48914C13.7229 3.44548 14.4982 4.22074 15.4545 4.22074Z" fill="url(#paint2_linear_64_298)"/>
<path d="M15.4545 4.87011C13.7809 4.87011 12.4242 6.22682 12.4242 7.90041V8.54976C12.4242 8.78894 12.6179 8.98266 12.8571 8.98266H18.0519C18.2911 8.98266 18.4848 8.78894 18.4848 8.54976V7.90041C18.4848 6.22682 17.1281 4.87011 15.4545 4.87011Z" fill="url(#paint3_linear_64_298)"/>
<path d="M0 13.0736H9.09091V18.1818C9.09091 19.186 8.27688 20 7.27273 20H1.81818C0.814028 20 0 19.186 0 18.1818V13.0736Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M0 12.7273C0 11.7231 0.814028 10.9091 1.81818 10.9091H7.27273C8.27688 10.9091 9.09091 11.7231 9.09091 12.7273V13.0736H0V12.7273Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M4.54544 15.1298C5.50176 15.1298 6.27704 14.3546 6.27704 13.3982C6.27704 12.4419 5.50176 11.6666 4.54544 11.6666C3.58911 11.6666 2.81384 12.4419 2.81384 13.3982C2.81384 14.3546 3.58911 15.1298 4.54544 15.1298Z" fill="url(#paint4_linear_64_298)"/>
<path d="M4.54544 15.7792C2.87184 15.7792 1.51513 17.1359 1.51513 18.8095V19.4589C1.51513 19.698 1.70886 19.8918 1.94803 19.8918H7.14284C7.38202 19.8918 7.57574 19.698 7.57574 19.4589V18.8095C7.57574 17.1359 6.21903 15.7792 4.54544 15.7792Z" fill="url(#paint5_linear_64_298)"/>
<path d="M10.9091 13.0736H20V18.1818C20 19.186 19.186 20 18.1818 20H12.7273C11.7231 20 10.9091 19.186 10.9091 18.1818V13.0736Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M10.9091 12.7273C10.9091 11.7231 11.7231 10.9091 12.7273 10.9091H18.1818C19.186 10.9091 20 11.7231 20 12.7273V13.0736H10.9091V12.7273Z" fill="#D9D9D9" fill-opacity="0.5"/>
<path d="M15.4545 15.1298C16.4109 15.1298 17.1861 14.3546 17.1861 13.3982C17.1861 12.4419 16.4109 11.6666 15.4545 11.6666C14.4982 11.6666 13.7229 12.4419 13.7229 13.3982C13.7229 14.3546 14.4982 15.1298 15.4545 15.1298Z" fill="url(#paint6_linear_64_298)"/>
<path d="M15.4545 15.7792C13.7809 15.7792 12.4242 17.1359 12.4242 18.8095V19.4589C12.4242 19.698 12.6179 19.8918 12.8571 19.8918H18.0519C18.2911 19.8918 18.4848 19.698 18.4848 19.4589V18.8095C18.4848 17.1359 17.1281 15.7792 15.4545 15.7792Z" fill="url(#paint7_linear_64_298)"/>
<defs>
<linearGradient id="paint0_linear_64_298" x1="3.21625" y1="3.21625" x2="17.1688" y2="17.1688" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint1_linear_64_298" x1="13.4184" y1="16.5602" x2="17.4602" y2="20.602" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint2_linear_64_298" x1="3.21625" y1="3.21625" x2="17.1688" y2="17.1688" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint3_linear_64_298" x1="13.4184" y1="16.5602" x2="17.4602" y2="20.602" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint4_linear_64_298" x1="3.21625" y1="3.21625" x2="17.1688" y2="17.1688" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint5_linear_64_298" x1="13.4184" y1="16.5602" x2="17.4602" y2="20.602" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint6_linear_64_298" x1="3.21625" y1="3.21625" x2="17.1688" y2="17.1688" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
<linearGradient id="paint7_linear_64_298" x1="13.4184" y1="16.5602" x2="17.4602" y2="20.602" gradientUnits="userSpaceOnUse">
<stop stop-color="#32BDEF"/>
<stop offset="1" stop-color="#1EA2E4"/>
</linearGradient>
</defs>
</svg>
'''
group_avatar = '''<svg width="22" height="23" viewBox="0 0 22 23" fill="none" xmlns="http://www.w3.org/2000/svg">
<rect y="0.19043" width="22" height="22" rx="1" fill="url(#paint0_linear_63_249)" fill-opacity="0.2"/>
<path d="M10.5 6.07388C11.8288 6.07388 12.906 4.99666 12.906 3.66786C12.906 2.33905 11.8288 1.26184 10.5 1.26184C9.17122 1.26184 8.09399 2.33905 8.09399 3.66786C8.09399 4.99666 9.17122 6.07388 10.5 6.07388Z" fill="url(#paint1_linear_63_249)"/>
<path d="M10.5 7.07385C8.01484 7.07385 6 8.99281 6 11.3596V21.0024C6 21.5944 6.50344 22.0739 7.12498 22.0739H13.875C14.4966 22.0739 15 21.5944 15 21.0024V11.3596C15 8.99281 12.9851 7.07385 10.5 7.07385Z" fill="url(#paint2_linear_63_249)"/>
<path d="M18 8.07141C19.3807 8.07141 20.5 6.95211 20.5 5.57139C20.5 4.1907 19.3807 3.07141 18 3.07141C16.6193 3.07141 15.5 4.1907 15.5 5.57139C15.5 6.95211 16.6193 8.07141 18 8.07141Z" fill="url(#paint3_linear_63_249)"/>
<path d="M18 9.07141C15.791 9.07141 14 10.9341 14 13.2314V21.0314C14 21.606 14.4475 22.0714 15 22.0714H21C21.5525 22.0714 22 21.606 22 21.0314V13.2314C22 10.9341 20.209 9.07141 18 9.07141Z" fill="url(#paint4_linear_63_249)"/>
<path d="M4.00003 8.07141C5.3807 8.07141 6.5 6.95211 6.5 5.57139C6.5 4.1907 5.3807 3.07141 4.00003 3.07141C2.61929 3.07141 1.5 4.1907 1.5 5.57139C1.5 6.95211 2.61929 8.07141 4.00003 8.07141Z" fill="url(#paint5_linear_63_249)"/>
<path d="M3.99998 9.07141C1.791 9.07141 0 10.9341 0 13.2314V21.0314C0 21.606 0.447498 22.0714 0.999996 22.0714H6.99997C7.5525 22.0714 8 21.606 8 21.0314V13.2314C8 10.9341 6.20898 9.07141 3.99998 9.07141Z" fill="url(#paint6_linear_63_249)"/>
<path d="M10.6316 13.6981C11.9604 13.6981 13.0376 12.6208 13.0376 11.292C13.0376 9.96321 11.9604 8.88599 10.6316 8.88599C9.30277 8.88599 8.22555 9.96321 8.22555 11.292C8.22555 12.6208 9.30277 13.6981 10.6316 13.6981Z" fill="url(#paint7_linear_63_249)"/>
<path d="M10.311 14.9111C7.75337 15.0771 5.81957 17.3147 5.81957 19.8777V21.5174C5.81957 21.8494 6.08907 22.1189 6.4211 22.1189H14.8421C15.1742 22.1189 15.4437 21.8494 15.4437 21.5174V19.7129C15.4437 16.949 13.114 14.7301 10.311 14.9111Z" fill="url(#paint8_linear_63_249)"/>
<defs>
<linearGradient id="paint0_linear_63_249" x1="11" y1="0.19043" x2="11" y2="22.1904" gradientUnits="userSpaceOnUse">
<stop offset="0.391413" stop-color="white"/>
<stop offset="1" stop-color="white" stop-opacity="0.33"/>
</linearGradient>
<linearGradient id="paint1_linear_63_249" x1="9.26662" y1="1.38802" x2="9.80022" y2="6.38135" gradientUnits="userSpaceOnUse">
<stop stop-color="#C3CDD9"/>
<stop offset="1" stop-color="#9FA7B0"/>
</linearGradient>
<linearGradient id="paint2_linear_63_249" x1="8.19319" y1="7.46719" x2="10.9108" y2="22.726" gradientUnits="userSpaceOnUse">
<stop stop-color="#C3CDD9"/>
<stop offset="1" stop-color="#9FA7B0"/>
</linearGradient>
<linearGradient id="paint3_linear_63_249" x1="16.7184" y1="3.20252" x2="17.2729" y2="8.3909" gradientUnits="userSpaceOnUse">
<stop stop-color="#C3CDD9"/>
<stop offset="1" stop-color="#9FA7B0"/>
</linearGradient>
<linearGradient id="paint4_linear_63_249" x1="15.9495" y1="9.4123" x2="18.2494" y2="22.6567" gradientUnits="userSpaceOnUse">
<stop stop-color="#C3CDD9"/>
<stop offset="1" stop-color="#9FA7B0"/>
</linearGradient>
<linearGradient id="paint5_linear_63_249" x1="2.71844" y1="3.20252" x2="3.27288" y2="8.3909" gradientUnits="userSpaceOnUse">
<stop stop-color="#C3CDD9"/>
<stop offset="1" stop-color="#9FA7B0"/>
</linearGradient>
<linearGradient id="paint6_linear_63_249" x1="1.9495" y1="9.4123" x2="4.2494" y2="22.6567" gradientUnits="userSpaceOnUse">
<stop stop-color="#C3CDD9"/>
<stop offset="1" stop-color="#9FA7B0"/>
</linearGradient>
<linearGradient id="paint7_linear_63_249" x1="8.99932" y1="9.65977" x2="12.3562" y2="13.0166" gradientUnits="userSpaceOnUse">
<stop stop-color="#0D61A9"/>
<stop offset="1" stop-color="#16528C"/>
</linearGradient>
<linearGradient id="paint8_linear_63_249" x1="7.36713" y1="16.0614" x2="12.2011" y2="22.5067" gradientUnits="userSpaceOnUse">
<stop stop-color="#0D61A9"/>
<stop offset="1" stop-color="#16528C"/>
</linearGradient>
</defs>
</svg>
'''


class Channel(models.Model):
    """ A mail.channel is a discussion group that may behave like a listener
    on documents. """
    _description = 'Discussion Channel'
    _name = 'mail.channel'
    _mail_flat_thread = False
    _mail_post_access = 'read'
    _inherit = ['mail.thread', 'mail.alias.mixin']

    MAX_BOUNCE_LIMIT = 10

    @api.model
    def default_get(self, fields):
        res = super(Channel, self).default_get(fields)
        if not res.get('alias_contact') and (not fields or 'alias_contact' in fields):
            res['alias_contact'] = 'everyone' if res.get('public', 'private') == 'public' else 'followers'
        return res

    @api.model
    def _generate_random_token(self):
        # Built to be shared on invitation link. It uses non-ambiguous characters and it is of a
        # reasonable length: enough to avoid brute force, but short enough to be shareable easily.
        # This token should not contain "mail.guest"._cookie_separator value.
        return ''.join(choice('abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ23456789') for _i in range(10))

    # description
    name = fields.Char('Name', required=True, translate=True)
    active = fields.Boolean(default=True, help="Set active to false to hide the channel without removing it.")
    channel_type = fields.Selection([
        ('chat', 'Chat'),
        ('channel', 'Channel'),
        ('group', 'Group')],
        string='Channel Type', default='channel', help="Chat is private and unique between 2 persons. Group is private among invited persons. Channel can be freely joined (depending on its configuration).")
    is_chat = fields.Boolean(string='Is a chat', compute='_compute_is_chat')
    default_display_mode = fields.Selection(string="Default Display Mode", selection=[('video_full_screen', "Full screen video")], help="Determines how the channel will be displayed by default when opening it from its invitation link. No value means display text (no voice/video).")
    description = fields.Text('Description')
    image_128 = fields.Image("Image", max_width=128, max_height=128)
    avatar_128 = fields.Image("Avatar", max_width=128, max_height=128, compute='_compute_avatar_128')
    channel_partner_ids = fields.Many2many(
        'res.partner', string='Members',
        compute='_compute_channel_partner_ids', inverse='_inverse_channel_partner_ids',
        compute_sudo=True, search='_search_channel_partner_ids',
        groups='base.group_user')
    channel_last_seen_partner_ids = fields.One2many(
        'mail.channel.partner', 'channel_id', string='Last Seen',
        groups='base.group_user')
    rtc_session_ids = fields.One2many('mail.channel.rtc.session', 'channel_id', groups="base.group_system")
    is_member = fields.Boolean('Is Member', compute='_compute_is_member', compute_sudo=True)
    member_count = fields.Integer(string="Member Count", compute='_compute_member_count', compute_sudo=True, help="Excluding guests from count.")
    group_ids = fields.Many2many(
        'res.groups', string='Auto Subscription',
        help="Members of those groups will automatically added as followers. "
             "Note that they will be able to manage their subscription manually "
             "if necessary.")
    # access
    uuid = fields.Char('UUID', size=50, default=_generate_random_token, copy=False)
    public = fields.Selection([
        ('public', 'Everyone'),
        ('private', 'Invited people only'),
        ('groups', 'Selected group of users')], string='Privacy',
        required=True, default='groups',
        help='This group is visible by non members. Invisible groups can add members through the invite button.')
    group_public_id = fields.Many2one('res.groups', string='Authorized Group',
                                      default=lambda self: self.env.ref('base.group_user'))

    _sql_constraints = [
        ('uuid_unique', 'UNIQUE(uuid)', 'The channel UUID must be unique'),
    ]

    # CHAT CONSTRAINT

    @api.constrains('channel_last_seen_partner_ids', 'channel_partner_ids')
    def _constraint_partners_chat(self):
        for ch in self.sudo().filtered(lambda ch: ch.channel_type == 'chat'):
            if len(ch.channel_last_seen_partner_ids) > 2 or len(ch.channel_partner_ids) > 2:
                raise ValidationError(_("A channel of type 'chat' cannot have more than two users."))

    # COMPUTE / INVERSE

    @api.depends('channel_type')
    def _compute_is_chat(self):
        for record in self:
            record.is_chat = record.channel_type == 'chat'

    @api.depends('channel_type', 'image_128', 'uuid')
    def _compute_avatar_128(self):
        for record in self:
            record.avatar_128 = record.image_128 or record._generate_avatar()

    def _generate_avatar(self):
        if self.channel_type not in ('channel', 'group'):
            return False
        avatar = group_avatar if self.channel_type == 'group' else channel_avatar
        bgcolor = get_hsl_from_seed(self.uuid)
        avatar = avatar.replace('fill="#136dc7"', f'fill="{bgcolor}"')
        return base64.b64encode(avatar.encode())

    @api.depends('channel_last_seen_partner_ids.partner_id')
    def _compute_channel_partner_ids(self):
        for channel in self:
            channel.channel_partner_ids = channel.channel_last_seen_partner_ids.partner_id

    def _inverse_channel_partner_ids(self):
        new_members = []
        outdated = self.env['mail.channel.partner']
        for channel in self:
            current_members = channel.channel_last_seen_partner_ids
            partners = channel.channel_partner_ids
            partners_new = partners - current_members.partner_id

            new_members += [{
                'channel_id': channel.id,
                'partner_id': partner.id,
            } for partner in partners_new]
            outdated += current_members.filtered(lambda m: m.partner_id not in partners)

        if new_members:
            self.env['mail.channel.partner'].create(new_members)
        if outdated:
            outdated.sudo().unlink()

    def _search_channel_partner_ids(self, operator, operand):
        return [(
            'channel_last_seen_partner_ids',
            'in',
            self.env['mail.channel.partner'].sudo()._search([
                ('partner_id', operator, operand)
            ])
        )]

    @api.depends('channel_partner_ids')
    def _compute_is_member(self):
        for channel in self:
            channel.is_member = self.env.user.partner_id in channel.channel_partner_ids

    @api.depends('channel_partner_ids')
    def _compute_member_count(self):
        read_group_res = self.env['mail.channel.partner'].read_group(domain=[('channel_id', 'in', self.ids)], fields=['channel_id'], groupby=['channel_id'])
        member_count_by_channel_id = {item['channel_id'][0]: item['channel_id_count'] for item in read_group_res}
        for channel in self:
            channel.member_count = member_count_by_channel_id.get(channel.id, 0)

    # ONCHANGE

    @api.onchange('public')
    def _onchange_public(self):
        if self.public != 'public' and self.alias_contact == 'everyone':
            self.alias_contact = 'followers'

    # ------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        defaults = self.default_get(['public'])

        access_types = []
        for vals in vals_list:
            # find partners to add from partner_ids
            partner_ids_cmd = vals.get('channel_partner_ids') or []
            if any(cmd[0] not in (4, 6) for cmd in partner_ids_cmd):
                raise ValidationError(_('Invalid value when creating a channel with members, only 4 or 6 are allowed.'))
            partner_ids = [cmd[1] for cmd in partner_ids_cmd if cmd[0] == 4]
            partner_ids += [cmd[2] for cmd in partner_ids_cmd if cmd[0] == 6]

            # find partners to add from channel_last_seen_partner_ids
            membership_ids_cmd = vals.get('channel_last_seen_partner_ids') or []
            if any(cmd[0] != 0 for cmd in membership_ids_cmd):
                raise ValidationError(_('Invalid value when creating a channel with memberships, only 0 is allowed.'))
            membership_pids = [cmd[2]['partner_id'] for cmd in membership_ids_cmd if cmd[0] == 0]

            # always add current user to new channel to have right values for
            # is_pinned + ensure he has rights to see channel
            partner_ids_to_add = list(set(partner_ids + [self.env.user.partner_id.id]))
            vals['channel_last_seen_partner_ids'] = membership_ids_cmd + [
                (0, 0, {'partner_id': pid})
                for pid in partner_ids_to_add if pid not in membership_pids
            ]

            # save visibility, apply public visibility for create then set back after creation
            # to avoid ACLS issue
            access_type = vals.pop('public', defaults['public'])
            access_types.append(access_type)
            vals['public'] = 'public'
            if not vals.get('alias_contact') and access_type != 'public':
                vals['alias_contact'] = 'followers'

            # clean vals
            vals.pop('channel_partner_ids', False)

        # Create channel and alias
        channels = super(Channel, self.with_context(mail_create_nolog=True, mail_create_nosubscribe=True)).create(vals_list)

        for access_type, channel in zip(access_types, channels):
            if access_type != 'public':
                channel.sudo().public = access_type

        channels._subscribe_users_automatically()

        return channels

    @api.ondelete(at_uninstall=False)
    def _unlink_except_all_employee_channel(self):
        # Delete mail.channel
        try:
            all_emp_group = self.env.ref('mail.channel_all_employees')
        except ValueError:
            all_emp_group = None
        if all_emp_group and all_emp_group in self:
            raise UserError(_('You cannot delete those groups, as the Whole Company group is required by other modules.'))

    def write(self, vals):
        result = super(Channel, self).write(vals)
        if vals.get('group_ids'):
            self._subscribe_users_automatically()
        if 'image_128' in vals:
            notifications = []
            for channel in self:
                notifications.append([channel, 'mail.channel/insert', {
                    'id': channel.id,
                    'avatarCacheKey': channel._get_avatar_cache_key(),
                }])
            self.env['bus.bus']._sendmany(notifications)
        return result

    def init(self):
        self._cr.execute('SELECT indexname FROM pg_indexes WHERE indexname = %s', ('mail_channel_partner_seen_message_id_idx',))
        if not self._cr.fetchone():
            self._cr.execute('CREATE INDEX mail_channel_partner_seen_message_id_idx ON mail_channel_partner (channel_id,partner_id,seen_message_id)')

    # ------------------------------------------------------------
    # MEMBERS MANAGEMENT
    # ------------------------------------------------------------

    def _subscribe_users_automatically(self):
        new_members = self._subscribe_users_automatically_get_members()
        if new_members:
            to_create = [
                {'channel_id': channel_id, 'partner_id': partner_id}
                for channel_id in new_members
                for partner_id in new_members[channel_id]
            ]
            self.env['mail.channel.partner'].sudo().create(to_create)

    def _subscribe_users_automatically_get_members(self):
        """ Return new members per channel ID """
        return dict(
            (channel.id, (channel.group_ids.users.partner_id - channel.channel_partner_ids).ids)
            for channel in self
        )

    def action_unfollow(self):
        return self._action_unfollow(self.env.user.partner_id)

    def _action_unfollow(self, partner):
        self.message_unsubscribe(partner.ids)
        if partner not in self.with_context(active_test=False).channel_partner_ids:
            return True
        channel_info = self.channel_info()[0]  # must be computed before leaving the channel (access rights)
        result = self.write({'channel_partner_ids': [Command.unlink(partner.id)]})
        # side effect of unsubscribe that wasn't taken into account because
        # channel_info is called before actually unpinning the channel
        channel_info['is_pinned'] = False
        self.env['bus.bus']._sendone(partner, 'mail.channel/leave', channel_info)
        notification = _('<div class="o_mail_notification">left the channel</div>')
        # post 'channel left' message as root since the partner just unsubscribed from the channel
        self.sudo().message_post(body=notification, subtype_xmlid="mail.mt_comment", author_id=partner.id)
        self.env['bus.bus']._sendone(self, 'mail.channel/insert', {
            'id': self.id,
            'memberCount': self.member_count,
            'members': [('insert-and-unlink', {'id': partner.id})],
        })
        return result

    def add_members(self, partner_ids=None, guest_ids=None, invite_to_rtc_call=False):
        """ Adds the given partner_ids and guest_ids as member of self channels. """
        self.check_access_rights('write')
        self.check_access_rule('write')
        partners = self.env['res.partner'].browse(partner_ids or []).exists()
        guests = self.env['mail.guest'].browse(guest_ids or []).exists()
        for channel in self:
            members_to_create = []
            if channel.public == 'groups':
                invalid_partners = partners.filtered(lambda partner: channel.group_public_id not in partner.user_ids.groups_id)
                if invalid_partners:
                    raise UserError(_(
                        'Channel "%(channel_name)s" only accepts members of group "%(group_name)s". Forbidden for: %(partner_names)s',
                        channel_name=channel.name,
                        group_name=channel.group_public_id.name,
                        partner_names=', '.join(partner.name for partner in invalid_partners)
                    ))
                if guests:
                    raise UserError(_(
                        'Channel "%(channel_name)s" only accepts members of group "%(group_name)s". Forbidden for: %(guest_names)s',
                        channel_name=channel.name,
                        group_name=channel.group_public_id.name,
                        guest_names=', '.join(guest.name for guest in guests)
                    ))
            existing_partners = self.env['res.partner'].search([('id', 'in', partners.ids), ('channel_ids', 'in', channel.id)])
            members_to_create += [{
                'partner_id': partner.id,
                'channel_id': channel.id,
            } for partner in partners - existing_partners]
            existing_guests = self.env['mail.guest'].search([('id', 'in', guests.ids), ('channel_ids', 'in', channel.id)])
            members_to_create += [{
                'guest_id': partner.id,
                'channel_id': channel.id,
            } for partner in guests - existing_guests]
            new_members = self.env['mail.channel.partner'].sudo().create(members_to_create)
            members_data = []
            guest_members_data = []
            for channel_partner in new_members.filtered(lambda channel_partner: channel_partner.partner_id):
                user = channel_partner.partner_id.user_ids[0] if channel_partner.partner_id.user_ids else self.env['res.users']
                # notify invited members through the bus
                if user:
                    self.env['bus.bus']._sendone(channel_partner.partner_id, 'mail.channel/joined', {
                        'channel': channel_partner.channel_id.with_user(user).with_context(allowed_company_ids=user.company_ids.ids).sudo().channel_info()[0],
                        'invited_by_user_id': self.env.user.id,
                    })
                # notify existing members with a new message in the channel
                if channel_partner.partner_id == self.env.user.partner_id:
                    notification = _('<div class="o_mail_notification">joined the channel</div>')
                else:
                    notification = _(
                        '<div class="o_mail_notification">invited <a href="#" data-oe-model="res.partner" data-oe-id="%(new_partner_id)d">%(new_partner_name)s</a> to the channel</div>',
                        new_partner_id=channel_partner.partner_id.id,
                        new_partner_name=channel_partner.partner_id.name,
                    )
                channel_partner.channel_id.message_post(body=notification, message_type="notification", subtype_xmlid="mail.mt_comment", notify_by_email=False)
                members_data.append({
                    'id': channel_partner.partner_id.id,
                    'im_status': channel_partner.partner_id.im_status,
                    'name': channel_partner.partner_id.name,
                })
            for channel_partner in new_members.filtered(lambda channel_partner: channel_partner.guest_id):
                channel_partner.channel_id.message_post(body=_('<div class="o_mail_notification">joined the channel</div>'), message_type="notification", subtype_xmlid="mail.mt_comment", notify_by_email=False)
                guest_members_data.append({
                    'id': channel_partner.guest_id.id,
                    'name': channel_partner.guest_id.name,
                })
                guest = channel_partner.guest_id
                if guest:
                    self.env['bus.bus']._sendone(guest, 'mail.channel/joined', {
                        'channel': channel_partner.channel_id.sudo().channel_info()[0],
                    })
            self.env['bus.bus']._sendone(channel, 'mail.channel/insert', {
                'id': channel.id,
                'guestMembers': [('insert', guest_members_data)],
                'memberCount': channel.member_count,
                'members': [('insert', members_data)],
            })
        if invite_to_rtc_call:
            if self.env.user._is_public() and 'guest' in self.env.context:
                guest = self.env.context.get('guest')
                partner = self.env['res.partner']
            else:
                guest = self.env['mail.guest']
                partner = self.env.user.partner_id
            for channel in self:
                current_channel_partner = self.env['mail.channel.partner'].sudo().search([('channel_id', '=', channel.id), ('partner_id', '=', partner.id), ('guest_id', '=', guest.id)])
                if current_channel_partner and current_channel_partner.rtc_session_ids:
                    current_channel_partner._rtc_invite_members(partner_ids=partners.ids, guest_ids=guests.ids)

    def _action_remove_members(self, partners):
        """ Private implementation to remove members from channels. Done as sudo
        to avoid ACLs issues with channel partners. """
        self.env['mail.channel.partner'].sudo().search([
            ('partner_id', 'in', partners.ids),
            ('channel_id', 'in', self.ids)
        ]).unlink()
        self.invalidate_cache(fnames=['channel_partner_ids', 'channel_last_seen_partner_ids'])

    def _can_invite(self, partner_id):
        """Return True if the current user can invite the partner to the channel.

          * public: ok;
          * private: must be member;
          * group: both current user and target must have group;

        :return boolean: whether inviting is ok"""
        partner = self.env['res.partner'].browse(partner_id)

        for channel in self.sudo():
            if channel.public == 'private' and not channel.is_member:
                return False
            if channel.public == 'groups':
                if not partner.user_ids or channel.group_public_id not in partner.user_ids.groups_id:
                    return False
                if channel.group_public_id not in self.env.user.groups_id:
                    return False
        return True

    # ------------------------------------------------------------
    # RTC
    # ------------------------------------------------------------

    def _rtc_cancel_invitations(self, partner_ids=None, guest_ids=None):
        """ Cancels the invitations of the RTC call from all invited members (or the specified partner_ids).
            :param list partner_ids: list of the partner ids from which the invitation has to be removed
            :param list guest_ids: list of the guest ids from which the invitation has to be removed
            if either partner_ids or guest_ids is set, only the specified ids will be invited.
        """
        self.ensure_one()
        channel_partner_domain = [
            ('channel_id', '=', self.id),
            ('rtc_inviting_session_id', '!=', False),
        ]
        if partner_ids or guest_ids:
            channel_partner_domain = expression.AND([channel_partner_domain, [
                '|',
                ('partner_id', 'in', partner_ids or []),
                ('guest_id', 'in', guest_ids or []),
            ]])
        invited_partners = self.env['res.partner']
        invited_guests = self.env['mail.guest']
        invitation_notifications = []
        for member in self.env['mail.channel.partner'].search(channel_partner_domain):
            member.rtc_inviting_session_id = False
            if member.partner_id:
                invited_partners |= member.partner_id
                target = member.partner_id
            else:
                invited_guests |= member.guest_id
                target = member.guest_id
            invitation_notifications.append((target, 'mail.channel/insert', {
                'id': self.id,
                'rtcInvitingSession': [('unlink',)],
            }))
        self.env['bus.bus']._sendmany(invitation_notifications)
        channel_data = {'id': self.id}
        if invited_guests:
            channel_data['invitedGuests'] = [('insert-and-unlink', [{'id': guest.id} for guest in invited_guests])]
        if invited_partners:
            channel_data['invitedPartners'] = [('insert-and-unlink', [{'id': partner.id} for partner in invited_partners])]
        if invited_partners or invited_guests:
            self.env['bus.bus']._sendone(self, 'mail.channel/insert', channel_data)
        return channel_data

    # ------------------------------------------------------------
    # MAILING
    # ------------------------------------------------------------

    def _alias_get_creation_values(self):
        values = super(Channel, self)._alias_get_creation_values()
        values['alias_model_id'] = self.env['ir.model']._get('mail.channel').id
        if self.id:
            values['alias_force_thread_id'] = self.id
        return values

    def _alias_get_error_message(self, message, message_dict, alias):
        if alias.alias_contact == 'followers' and self.ids:
            author = self.env['res.partner'].browse(message_dict.get('author_id', False))
            if not author or author not in self.channel_partner_ids:
                return _('restricted to channel members')
            return False
        return super(Channel, self)._alias_get_error_message(message, message_dict, alias)

    def _notify_compute_recipients(self, message, msg_vals):
        """ Override recipients computation as channel is not a standard
        mail.thread document. Indeed there are no followers on a channel.
        Instead of followers it has members that should be notified.

        :param message: see ``MailThread._notify_compute_recipients()``;
        :param msg_vals: see ``MailThread._notify_compute_recipients()``;

        :return recipients: structured data holding recipients data. See
          ``MailThread._notify_thread()`` for more details about its content
          and use;
        """
        # get values from msg_vals or from message if msg_vals doen't exists
        msg_sudo = message.sudo()
        message_type = msg_vals.get('message_type', 'email') if msg_vals else msg_sudo.message_type
        pids = msg_vals.get('partner_ids', []) if msg_vals else msg_sudo.partner_ids.ids

        # notify only user input (comment or incoming emails)
        if message_type not in ('comment', 'email'):
            return []
        # notify only mailing lists or if mentioning recipients
        if not pids:
            return []

        email_from = tools.email_normalize(msg_vals.get('email_from') or msg_sudo.email_from)
        author_id = msg_vals.get('author_id') or msg_sudo.author_id.id

        recipients_data = []
        if pids:
            self.env['res.partner'].flush(fnames=['active', 'email', 'partner_share'])
            self.env['res.users'].flush(fnames=['notification_type', 'partner_id'])
            sql_query = """
                SELECT DISTINCT ON (partner.id) partner.id,
                       partner.partner_share,
                       users.notification_type
                  FROM res_partner partner
             LEFT JOIN res_users users on partner.id = users.partner_id
                 WHERE partner.active IS TRUE
                       AND partner.email != %s
                       AND partner.id = ANY(%s) AND partner.id != ANY(%s)"""
            self.env.cr.execute(
                sql_query,
                (email_from or '', list(pids), [author_id] if author_id else [], )
            )
            for partner_id, partner_share, notif in self._cr.fetchall():
                # ocn_client: will add partners to recipient recipient_data. more ocn notifications. We neeed to filter them maybe
                recipients_data.append({
                    'id': partner_id,
                    'share': partner_share,
                    'active': True,
                    'notif': notif or 'email',
                    'type': 'user' if not partner_share and notif else 'customer',
                    'groups': [],
                })

        return recipients_data

    def _notify_get_groups(self, msg_vals=None):
        """ All recipients of a message on a channel are considered as partners.
        This means they will receive a minimal email, without a link to access
        in the backend. Mailing lists should indeed send minimal emails to avoid
        the noise. """
        groups = super(Channel, self)._notify_get_groups(msg_vals=msg_vals)
        for (index, (group_name, group_func, group_data)) in enumerate(groups):
            if group_name != 'customer':
                groups[index] = (group_name, lambda partner: False, group_data)
        return groups

    def _notify_thread(self, message, msg_vals=False, **kwargs):
        # link message to channel
        rdata = super(Channel, self)._notify_thread(message, msg_vals=msg_vals, **kwargs)

        message_format_values = message.message_format()[0]
        bus_notifications = self._channel_message_notifications(message, message_format_values)
        self.env['bus.bus'].sudo()._sendmany(bus_notifications)
        # Last interest is updated for a chat when posting a message.
        # So a notification is needed to update UI.
        if self.is_chat or self.channel_type == 'group':
            notifications = []
            for channel_partners in self.channel_last_seen_partner_ids.filtered('partner_id'):
                notifications.append([channel_partners.partner_id, 'mail.channel/last_interest_dt_changed', {
                    'id': self.id,
                    'last_interest_dt': channel_partners.last_interest_dt,
                }])
            self.env['bus.bus']._sendmany(notifications)
        return rdata

    def _message_receive_bounce(self, email, partner):
        """ Override bounce management to unsubscribe bouncing addresses """
        for p in partner:
            if p.message_bounce >= self.MAX_BOUNCE_LIMIT:
                self._action_unfollow(p)
        return super(Channel, self)._message_receive_bounce(email, partner)

    def _message_compute_author(self, author_id=None, email_from=None, raise_exception=False):
        return super()._message_compute_author(author_id=author_id, email_from=email_from, raise_exception=False)

    def _message_compute_parent_id(self, parent_id):
        # super() unravels the chain of parents to set parent_id as the first
        # ancestor. We don't want that in channel.
        if not parent_id:
            return parent_id
        return self.env['mail.message'].search(
            [('id', '=', parent_id),
             ('model', '=', self._name),
             ('res_id', '=', self.id)
            ]).id

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, *, message_type='notification', **kwargs):
        self.filtered(lambda channel: channel.is_chat or channel.channel_type == 'group').mapped('channel_last_seen_partner_ids').sudo().write({
            'is_pinned': True,
            'last_interest_dt': fields.Datetime.now(),
        })

        # mail_post_autofollow=False is necessary to prevent adding followers
        # when using mentions in channels. Followers should not be added to
        # channels, and especially not automatically (because channel membership
        # should be managed with channel.partner instead).
        # The current client code might be setting the key to True on sending
        # message but it is only useful when targeting customers in chatter.
        # This value should simply be set to False in channels no matter what.
        return super(Channel, self.with_context(mail_create_nosubscribe=True, mail_post_autofollow=False)).message_post(message_type=message_type, **kwargs)

    def _message_post_after_hook(self, message, msg_vals):
        """
        Automatically set the message posted by the current user as seen for himself.
        """
        self._set_last_seen_message(message)
        return super()._message_post_after_hook(message=message, msg_vals=msg_vals)

    def _check_can_update_message_content(self, message):
        """ We don't call super in this override as we want to ignore the
        mail.thread behavior completely """
        if not message.message_type == 'comment':
            raise UserError(_("Only messages type comment can have their content updated on model 'mail.channel'"))

    def _message_update_content_after_hook(self, message):
        self.ensure_one()
        self.env['bus.bus']._sendone(self, 'mail.message/insert', {
            'id': message.id,
            'body': message.body,
            'attachments': [('insert-and-replace', message.attachment_ids._attachment_format(commands=True))],
        })
        return super()._message_update_content_after_hook(message=message)

    def _message_add_reaction_after_hook(self, message, content):
        self.ensure_one()
        if self.env.user._is_public() and 'guest' in self.env.context:
            guests = [('insert', {'id': self.env.context.get('guest').id})]
            partners = []
        else:
            guests = []
            partners = [('insert', {'id': self.env.user.partner_id.id})]
        reactions = self.env['mail.message.reaction'].sudo().search([('message_id', '=', message.id), ('content', '=', content)])
        self.env['bus.bus']._sendone(self, 'mail.message/insert', {
            'id': message.id,
            'messageReactionGroups': [('insert' if len(reactions) > 0 else 'insert-and-unlink', {
                'messageId': message.id,
                'content': content,
                'count': len(reactions),
                'guests': guests,
                'partners': partners,
            })],
        })
        return super()._message_add_reaction_after_hook(message=message, content=content)

    def _message_remove_reaction_after_hook(self, message, content):
        self.ensure_one()
        if self.env.user._is_public() and 'guest' in self.env.context:
            guests = [('insert-and-unlink', {'id': self.env.context.get('guest').id})]
            partners = []
        else:
            guests = []
            partners = [('insert-and-unlink', {'id': self.env.user.partner_id.id})]
        reactions = self.env['mail.message.reaction'].sudo().search([('message_id', '=', message.id), ('content', '=', content)])
        self.env['bus.bus']._sendone(self, 'mail.message/insert', {
            'id': message.id,
            'messageReactionGroups': [('insert' if len(reactions) > 0 else 'insert-and-unlink', {
                'messageId': message.id,
                'content': content,
                'count': len(reactions),
                'guests': guests,
                'partners': partners,
            })],
        })
        return super()._message_remove_reaction_after_hook(message=message, content=content)

    def _message_subscribe(self, partner_ids=None, subtype_ids=None, customer_ids=None):
        """ Do not allow follower subscription on channels. Only members are
        considered. """
        raise UserError(_('Adding followers on channels is not possible. Consider adding members instead.'))

    # ------------------------------------------------------------
    # BROADCAST
    # ------------------------------------------------------------

    # Anonymous method
    def _broadcast(self, partner_ids):
        """ Broadcast the current channel header to the given partner ids
            :param partner_ids : the partner to notify
        """
        notifications = self._channel_channel_notifications(partner_ids)
        self.env['bus.bus']._sendmany(notifications)

    def _channel_channel_notifications(self, partner_ids):
        """ Generate the bus notifications of current channel for the given partner ids
            :param partner_ids : the partner to send the current channel header
            :returns list of bus notifications (tuple (bus_channe, message_content))
        """
        notifications = []
        for partner in self.env['res.partner'].browse(partner_ids):
            user_id = partner.user_ids and partner.user_ids[0] or False
            if user_id:
                user_channels = self.with_user(user_id).with_context(
                    allowed_company_ids=user_id.company_ids.ids
                )
                for channel_info in user_channels.channel_info():
                    notifications.append((partner, 'mail.channel/legacy_insert', channel_info))
        return notifications

    def _channel_message_notifications(self, message, message_format=False):
        """ Generate the bus notifications for the given message
            :param message : the mail.message to sent
            :returns list of bus notifications (tuple (bus_channe, message_content))
        """
        message_format = message_format or message.message_format()[0]
        notifications = []
        for channel in self:
            payload = {
                'id': channel.id,
                'message': dict(message_format),
            }
            notifications.append((channel, 'mail.channel/new_message', payload))
            # add uuid to allow anonymous to listen
            if channel.public == 'public':
                notifications.append((channel.uuid, 'mail.channel/new_message', payload))
        return notifications

    # ------------------------------------------------------------
    # INSTANT MESSAGING API
    # ------------------------------------------------------------
    # A channel header should be broadcasted:
    #   - when adding user to channel (only to the new added partners)
    #   - when folding/minimizing a channel (only to the user making the action)
    # A message should be broadcasted:
    #   - when a message is posted on a channel (to the channel, using _notify() method)
    # ------------------------------------------------------------

    def channel_info(self):
        """ Get the informations header for the current channels
            :returns a list of channels values
            :rtype : list(dict)
        """
        if not self:
            return []
        channel_infos = []
        rtc_sessions_by_channel = self.sudo().rtc_session_ids._mail_rtc_session_format_by_channel()
        channel_last_message_ids = dict((r['id'], r['message_id']) for r in self._channel_last_message_ids())
        all_needed_members_domain = expression.OR([
            [('channel_id.channel_type', '!=', 'channel')],
            [('rtc_inviting_session_id', '!=', False)],
            [('partner_id', '=', self.env.user.partner_id.id)] if self.env.user and self.env.user.partner_id else expression.FALSE_LEAF,
        ])
        all_needed_members = self.env['mail.channel.partner'].search(expression.AND([[('channel_id', 'in', self.ids)], all_needed_members_domain]))
        partner_format_by_partner = all_needed_members.partner_id.mail_partner_format()
        members_by_channel = defaultdict(lambda: self.env['mail.channel.partner'])
        invited_members_by_channel = defaultdict(lambda: self.env['mail.channel.partner'])
        member_of_current_user_by_channel = defaultdict(lambda: self.env['mail.channel.partner'])
        for member in all_needed_members:
            members_by_channel[member.channel_id] |= member
            if member.rtc_inviting_session_id:
                invited_members_by_channel[member.channel_id] |= member
            if self.env.user and self.env.user.partner_id and member.partner_id == self.env.user.partner_id:
                member_of_current_user_by_channel[member.channel_id] = member
        for channel in self:
            info = {
                'avatarCacheKey': channel._get_avatar_cache_key(),
                'id': channel.id,
                'name': channel.name,
                'defaultDisplayMode': channel.default_display_mode,
                'description': channel.description,
                'uuid': channel.uuid,
                'state': 'open',
                'is_minimized': False,
                'channel_type': channel.channel_type,
                'public': channel.public,
                'group_based_subscription': bool(channel.group_ids),
                'create_uid': channel.create_uid.id,
            }
            # add last message preview (only used in mobile)
            info['last_message_id'] = channel_last_message_ids.get(channel.id, False)
            info['memberCount'] = channel.member_count
            # find the channel partner state, if logged user
            if self.env.user and self.env.user.partner_id:
                info['message_needaction_counter'] = channel.message_needaction_counter
                info['message_unread_counter'] = channel.message_unread_counter
                partner_channel = member_of_current_user_by_channel.get(channel, self.env['mail.channel.partner'])
                if partner_channel:
                    partner_channel = partner_channel[0]
                    info['state'] = partner_channel.fold_state or 'open'
                    info['is_minimized'] = partner_channel.is_minimized
                    info['seen_message_id'] = partner_channel.seen_message_id.id
                    info['custom_channel_name'] = partner_channel.custom_channel_name
                    info['is_pinned'] = partner_channel.is_pinned
                    info['last_interest_dt'] = partner_channel.last_interest_dt.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
                    if partner_channel.rtc_inviting_session_id:
                        info['rtc_inviting_session'] = {'id': partner_channel.rtc_inviting_session_id.id}
            # add members info
            if channel.channel_type != 'channel':
                # avoid sending potentially a lot of members for big channels
                # exclude chat and other small channels from this optimization because they are
                # assumed to be smaller and it's important to know the member list for them
                info['members'] = sorted(list(channel._channel_info_format_member(member.partner_id, partner_format_by_partner[member.partner_id]) for member in members_by_channel[channel] if member.partner_id), key=lambda p: p['id'])
                info['seen_partners_info'] = sorted([{
                    'id': cp.id,
                    'partner_id': cp.partner_id.id,
                    'fetched_message_id': cp.fetched_message_id.id,
                    'seen_message_id': cp.seen_message_id.id,
                } for cp in members_by_channel[channel] if cp.partner_id], key=lambda p: p['partner_id'])
                info['guestMembers'] = [('insert', sorted([{
                    'id': member.guest_id.id,
                    'name': member.guest_id.name,
                } for member in members_by_channel[channel] if member.guest_id], key=lambda g: g['id']))]

            # add RTC sessions info
            info.update({
                'invitedGuests': [('insert', [{'id': member.guest_id.id, 'name': member.guest_id.name} for member in invited_members_by_channel[channel] if member.guest_id])],
                'invitedPartners': [('insert', [{'id': member.partner_id.id, 'name': member.partner_id.name} for member in invited_members_by_channel[channel] if member.partner_id])],
                'rtcSessions': [('insert', rtc_sessions_by_channel.get(channel, []))],
            })

            channel_infos.append(info)
        return channel_infos

    def _channel_info_format_member(self, partner, partner_info):
        """Returns member information in the context of self channel."""
        self.ensure_one()
        return partner_info

    def _channel_fetch_message(self, last_id=False, limit=20):
        """ Return message values of the current channel.
            :param last_id : last message id to start the research
            :param limit : maximum number of messages to fetch
            :returns list of messages values
            :rtype : list(dict)
        """
        self.ensure_one()
        domain = ["&", ("model", "=", "mail.channel"), ("res_id", "in", self.ids)]
        if last_id:
            domain.append(("id", "<", last_id))
        return self.env['mail.message']._message_fetch(domain=domain, limit=limit)

    # User methods
    @api.model
    def channel_get(self, partners_to, pin=True):
        """ Get the canonical private channel between some partners, create it if needed.
            To reuse an old channel (conversation), this one must be private, and contains
            only the given partners.
            :param partners_to : list of res.partner ids to add to the conversation
            :param pin : True if getting the channel should pin it for the current user
            :returns: channel_info of the created or existing channel
            :rtype: dict
        """
        if self.env.user.partner_id.id not in partners_to:
            partners_to.append(self.env.user.partner_id.id)
        if len(partners_to) > 2:
            raise UserError(_("A chat should not be created with more than 2 persons. Create a group instead."))
        # determine type according to the number of partner in the channel
        self.flush()
        self.env.cr.execute("""
            SELECT P.channel_id
            FROM mail_channel C, mail_channel_partner P
            WHERE P.channel_id = C.id
                AND C.public LIKE 'private'
                AND P.partner_id IN %s
                AND C.channel_type LIKE 'chat'
                AND NOT EXISTS (
                    SELECT *
                    FROM mail_channel_partner P2
                    WHERE P2.channel_id = C.id
                        AND P2.partner_id NOT IN %s
                )
            GROUP BY P.channel_id
            HAVING ARRAY_AGG(DISTINCT P.partner_id ORDER BY P.partner_id) = %s
            LIMIT 1
        """, (tuple(partners_to), tuple(partners_to), sorted(list(partners_to)),))
        result = self.env.cr.dictfetchall()
        if result:
            # get the existing channel between the given partners
            channel = self.browse(result[0].get('channel_id'))
            # pin up the channel for the current partner
            if pin:
                self.env['mail.channel.partner'].search([('partner_id', '=', self.env.user.partner_id.id), ('channel_id', '=', channel.id)]).write({
                    'is_pinned': True,
                    'last_interest_dt': fields.Datetime.now(),
                })
            channel._broadcast(self.env.user.partner_id.ids)
        else:
            # create a new one
            channel = self.create({
                'channel_partner_ids': [Command.link(partner_id) for partner_id in partners_to],
                'public': 'private',
                'channel_type': 'chat',
                'name': ', '.join(self.env['res.partner'].sudo().browse(partners_to).mapped('name')),
            })
            channel._broadcast(partners_to)
        return channel.channel_info()[0]

    @api.model
    def channel_fold(self, uuid, state=None):
        """ Update the fold_state of the given session. In order to syncronize web browser
            tabs, the change will be broadcast to himself (the current user channel).
            Note: the user need to be logged
            :param state : the new status of the session for the current user.
        """
        domain = [('partner_id', '=', self.env.user.partner_id.id), ('channel_id.uuid', '=', uuid)]
        for session_state in self.env['mail.channel.partner'].search(domain):
            if not state:
                state = session_state.fold_state
                if session_state.fold_state == 'open':
                    state = 'folded'
                else:
                    state = 'open'
            is_minimized = bool(state != 'closed')
            vals = {}
            if session_state.fold_state != state:
                vals['fold_state'] = state
            if session_state.is_minimized != is_minimized:
                vals['is_minimized'] = is_minimized
            if vals:
                session_state.write(vals)
            self.env['bus.bus']._sendone(self.env.user.partner_id, 'mail.channel/insert', {
                'id': session_state.channel_id.channel_info()[0]['id'],
                'serverFoldState': state,
            })

    @api.model
    def channel_pin(self, uuid, pinned=False):
        # add the person in the channel, and pin it (or unpin it)
        channel = self.search([('uuid', '=', uuid)])
        channel._execute_channel_pin(pinned)

    def _execute_channel_pin(self, pinned=False):
        """ Hook for website_livechat channel unpin and cleaning """
        self.ensure_one()
        channel_partners = self.env['mail.channel.partner'].search(
            [('partner_id', '=', self.env.user.partner_id.id), ('channel_id', '=', self.id), ('is_pinned', '!=', pinned)])
        if channel_partners:
            channel_partners.write({'is_pinned': pinned})
        if not pinned:
            self.env['bus.bus']._sendone(self.env.user.partner_id, 'mail.channel/unpin', {'id': self.id})
        else:
            self.env['bus.bus']._sendone(self.env.user.partner_id, 'mail.channel/legacy_insert', self.channel_info()[0])

    def _channel_seen(self, last_message_id=None):
        """
        Mark channel as seen by updating seen message id of the current logged partner
        :param last_message_id: the id of the message to be marked as seen, last message of the
        thread by default. This param SHOULD be required, the default behaviour is DEPRECATED and
        kept only for compatibility reasons.
        """
        self.ensure_one()
        domain = ["&", ("model", "=", "mail.channel"), ("res_id", "in", self.ids)]
        if last_message_id:
            domain = expression.AND([domain, [('id', '<=', last_message_id)]])
        last_message = self.env['mail.message'].search(domain, order="id DESC", limit=1)
        if not last_message:
            return
        self._set_last_seen_message(last_message)
        data = {
            'channel_id': self.id,
            'last_message_id': last_message.id,
            'partner_id': self.env.user.partner_id.id,
        }
        target = self if self.channel_type == 'chat' else self.env.user.partner_id
        self.env['bus.bus']._sendone(target, 'mail.channel.partner/seen', data)
        return last_message.id

    def _set_last_seen_message(self, last_message):
        """
        Set last seen message of `self` channels for the current user.
        :param last_message: the message to set as last seen message
        """
        channel_partner_domain = expression.AND([
            [('channel_id', 'in', self.ids)],
            [('partner_id', '=', self.env.user.partner_id.id)],
            expression.OR([
                [('seen_message_id', '=', False)],
                [('seen_message_id', '<', last_message.id)]
            ])
        ])
        channel_partner_domain = expression.AND([channel_partner_domain, [('partner_id', '=', self.env.user.partner_id.id)]])
        channel_partner = self.env['mail.channel.partner'].search(channel_partner_domain)
        channel_partner.write({
            'fetched_message_id': last_message.id,
            'seen_message_id': last_message.id,
        })

    def channel_fetched(self):
        """ Broadcast the channel_fetched notification to channel members
        """
        for channel in self:
            if not channel.message_ids.ids:
                return
            if channel.channel_type != 'chat':
                return
            last_message_id = channel.message_ids.ids[0] # zero is the index of the last message
            channel_partner = self.env['mail.channel.partner'].search([('channel_id', '=', channel.id), ('partner_id', '=', self.env.user.partner_id.id)], limit=1)
            if channel_partner.fetched_message_id.id == last_message_id:
                # last message fetched by user is already up-to-date
                return
            channel_partner.write({
                'fetched_message_id': last_message_id,
            })
            self.env['bus.bus']._sendone(channel, 'mail.channel.partner/fetched', {
                'channel_id': channel.id,
                'id': channel_partner.id,
                'last_message_id': last_message_id,
                'partner_id': self.env.user.partner_id.id,
            })

    def channel_set_custom_name(self, name):
        self.ensure_one()
        channel_partner = self.env['mail.channel.partner'].search([('partner_id', '=', self.env.user.partner_id.id), ('channel_id', '=', self.id)])
        channel_partner.write({'custom_channel_name': name})
        self.env['bus.bus']._sendone(channel_partner.partner_id, 'mail.channel/insert', {
            'id': self.id,
            'custom_channel_name': name,
        })

    def channel_rename(self, name):
        self.ensure_one()
        self.write({'name': name})
        self.env['bus.bus']._sendone(self, 'mail.channel/insert', {
            'id': self.id,
            'name': name,
        })

    def channel_change_description(self, description):
        self.ensure_one()
        self.write({'description': description})
        self.env['bus.bus']._sendone(self, 'mail.channel/insert', {
            'id': self.id,
            'description': description
        })

    def notify_typing(self, is_typing):
        """ Broadcast the typing notification to channel members
            :param is_typing: (boolean) tells whether the current user is typing or not
        """
        notifications = []
        for channel in self:
            data = dict({
                'channel_id': channel.id,
                'is_typing': is_typing,
            }, **channel._notify_typing_partner_data())
            notifications.append([channel, 'mail.channel.partner/typing_status', data])  # notify backend users
            notifications.append([channel.uuid, 'mail.channel.partner/typing_status', data])  # notify frontend users
        self.env['bus.bus']._sendmany(notifications)

    def _notify_typing_partner_data(self):
        """Returns typing partner data for self channel."""
        self.ensure_one()
        return {
            'partner_id': self.env.user.partner_id.id,
            'partner_name': self.env.user.partner_id.name,
        }

    @api.model
    def channel_search_to_join(self, name=None, domain=None):
        """ Return the channel info of the channel the current partner can join
            :param name : the name of the researched channels
            :param domain : the base domain of the research
            :returns dict : channel dict
        """
        if not domain:
            domain = []
        domain = expression.AND([
            [('channel_type', '=', 'channel')],
            [('channel_partner_ids', 'not in', [self.env.user.partner_id.id])],
            [('public', '!=', 'private')],
            domain
        ])
        if name:
            domain = expression.AND([domain, [('name', 'ilike', '%'+name+'%')]])
        return self.search(domain).read(['name', 'public', 'uuid', 'channel_type'])

    def channel_join(self):
        """ Shortcut to add the current user as member of self channels.
        Prefer calling add_members() directly when possible.
        """
        self.add_members(self.env.user.partner_id.ids)

    @api.model
    def channel_create(self, name, privacy='groups'):
        """ Create a channel and add the current partner, broadcast it (to make the user directly
            listen to it when polling)
            :param name : the name of the channel to create
            :param privacy : privacy of the channel. Should be 'public' or 'private'.
            :return dict : channel header
        """
        # create the channel
        new_channel = self.create({
            'name': name,
            'public': privacy,
        })
        notification = _('<div class="o_mail_notification">created <a href="#" class="o_channel_redirect" data-oe-id="%s">#%s</a></div>', new_channel.id, new_channel.name)
        new_channel.message_post(body=notification, message_type="notification", subtype_xmlid="mail.mt_comment")
        channel_info = new_channel.channel_info()[0]
        self.env['bus.bus']._sendone(self.env.user.partner_id, 'mail.channel/legacy_insert', channel_info)
        return channel_info

    @api.model
    def create_group(self, partners_to, default_display_mode=False):
        """ Create a group channel.
            :param partners_to : list of res.partner ids to add to the conversation
            :returns: channel_info of the created channel
            :rtype: dict
        """
        channel = self.create({
            'channel_last_seen_partner_ids': [Command.create({'partner_id': partner_id}) for partner_id in partners_to],
            'channel_type': 'group',
            'default_display_mode': default_display_mode,
            'name': '',  # default name is computed client side from the list of members
            'public': 'private',
        })
        channel._broadcast(partners_to)
        return channel.channel_info()[0]

    @api.model
    def get_mention_suggestions(self, search, limit=8):
        """ Return 'limit'-first channels' id, name and public fields such that the name matches a
            'search' string. Exclude channels of type chat (DM), and private channels the current
            user isn't registered to. """
        domain = expression.AND([
                        [('name', 'ilike', search)],
                        [('channel_type', '=', 'channel')],
                        expression.OR([
                            [('public', '!=', 'private')],
                            [('channel_partner_ids', 'in', [self.env.user.partner_id.id])]
                        ])
                    ])
        return self.search_read(domain, ['id', 'name', 'public', 'channel_type'], limit=limit)

    @api.model
    def channel_fetch_listeners(self, uuid):
        """ Return the id, name and email of partners listening to the given channel """
        self._cr.execute("""
            SELECT P.id, P.name, P.email
            FROM mail_channel_partner CP
                INNER JOIN res_partner P ON CP.partner_id = P.id
                INNER JOIN mail_channel C ON CP.channel_id = C.id
            WHERE C.uuid = %s""", (uuid,))
        return self._cr.dictfetchall()

    def channel_fetch_preview(self):
        """ Return the last message of the given channels """
        if not self:
            return []
        channels_last_message_ids = self._channel_last_message_ids()
        channels_preview = dict((r['message_id'], r) for r in channels_last_message_ids)
        last_messages = self.env['mail.message'].browse(channels_preview).message_format()
        for message in last_messages:
            channel = channels_preview[message['id']]
            del(channel['message_id'])
            channel['last_message'] = message
        return list(channels_preview.values())

    def _channel_last_message_ids(self):
        """ Return the last message of the given channels."""
        if not self:
            return []
        self.flush()
        self.env.cr.execute("""
            SELECT res_id AS id, MAX(id) AS message_id
            FROM mail_message
            WHERE model = 'mail.channel' AND res_id IN %s
            GROUP BY res_id
            """, (tuple(self.ids),))
        return self.env.cr.dictfetchall()

    def load_more_members(self, known_member_ids):
        self.ensure_one()
        partners = self.env['res.partner'].with_context(active_test=False).search_read(
            domain=[('id', 'not in', known_member_ids), ('channel_ids', 'in', self.id)],
            fields=['id', 'name', 'im_status'],
            limit=30
        )
        return [('insert', partners)]

    def _get_avatar_cache_key(self):
        if not self.avatar_128:
            return 'no-avatar'
        return sha512(self.avatar_128).hexdigest()

    # ------------------------------------------------------------
    # COMMANDS
    # ------------------------------------------------------------

    def _send_transient_message(self, partner_to, content):
        """ Notifies partner_to that a message (not stored in DB) has been
            written in this channel.
            `content` is HTML, dynamic parts should be escaped by the caller.
        """
        self.env['bus.bus']._sendone(partner_to, 'mail.channel/transient_message', {
            'body': "<span class='o_mail_notification'>" + content + "</span>",
            'model': self._name,
            'res_id': self.id,
        })

    def execute_command_help(self, **kwargs):
        partner = self.env.user.partner_id
        if self.channel_type == 'channel':
            msg = _("You are in channel <b>#%s</b>.", self.name)
            if self.public == 'private':
                msg += _(" This channel is private. People must be invited to join it.")
        else:
            all_channel_partners = self.env['mail.channel.partner'].with_context(active_test=False)
            channel_partners = all_channel_partners.search([('partner_id', '!=', partner.id), ('channel_id', '=', self.id)])
            msg = _("You are in a private conversation with <b>@%s</b>.", html_escape(channel_partners[0].partner_id.name if channel_partners else _('Anonymous')))
        msg += self._execute_command_help_message_extra()

        self._send_transient_message(partner, msg)

    def _execute_command_help_message_extra(self):
        msg = _("""<br><br>
            Type <b>@username</b> to mention someone, and grab his attention.<br>
            Type <b>#channel</b> to mention a channel.<br>
            Type <b>/command</b> to execute a command.<br>""")
        return msg

    def execute_command_leave(self, **kwargs):
        if self.channel_type in ('channel', 'group'):
            self.action_unfollow()
        else:
            self.channel_pin(self.uuid, False)

    def execute_command_who(self, **kwargs):
        partner = self.env.user.partner_id
        members = [
            f'<a href="#" data-oe-id={str(p.id)} data-oe-model="res.partner">@{html_escape(p.name)}</a>'
            for p in self.channel_partner_ids[:30] if p != partner
        ]
        if len(members) == 0:
            msg = _("You are alone in this channel.")
        else:
            dots = "..." if len(members) != len(self.channel_partner_ids) - 1 else ""
            msg = _("Users in this channel: %(members)s %(dots)s and you.", members=", ".join(members), dots=dots)

        self._send_transient_message(partner, msg)
