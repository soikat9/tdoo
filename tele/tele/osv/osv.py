# -*- coding: utf-8 -*-
# Part of Tele. See LICENSE file for full copyright and licensing details.

from ..exceptions import except_orm
from ..models import Model, TransientModel, AbstractModel

# Deprecated, kept for backward compatibility.
except_osv = except_orm

# Deprecated, kept for backward compatibility.
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel # ;-)
