# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

try:
    # import for usage in phonenumbers_patch/region_*.py files
    from phonenumbers.phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata # pylint: disable=unused-import
except ImportError:
    pass
