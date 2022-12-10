# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.


{
    'name': 'Appointment Lead Generation',
    'version': '1.0',
    'category': 'Marketing/Online Appointment',
    'sequence': 2150,
    'summary': 'Generate leads when prospects schedule appointments',
    'website': 'https://www.tele.studio/app/appointments',
    'description': """
Allow to generate lead from Scheduled Appointments through your Website
-----------------------------------------------------------------------

""",
    'depends': ['appointment', 'crm'],
    'data': [
        'views/calendar_appointment_type_views.xml',
        'data/crm_tag.xml',
    ],
    'application': False,
    'auto_install': True,
    'license': 'TEEL-1',
}
