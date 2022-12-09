# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from ..exceptions import except_orm
from ..models import Model, TransientModel, AbstractModel

# Deprecated, kept for backward compatibility.
except_osv = except_orm

# Deprecated, kept for backward compatibility.
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel # ;-)
