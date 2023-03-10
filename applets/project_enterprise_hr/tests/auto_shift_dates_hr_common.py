# -*- coding: utf-8 -*-
# For full licensing and copyright information, see the LICENSE file - Tele, INC.

from dateutil.relativedelta import relativedelta

from tele.applets.project_enterprise.tests.auto_shift_dates_common import AutoShiftDatesCommon
from tele.fields import Command


class AutoShiftDatesHRCommon(AutoShiftDatesCommon):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.armande_employee = cls.env['hr.employee'].create({
            'name': 'Armande ProjectUser',
            'user_id': cls.user_projectuser.id,
            'tz': 'UTC',
        })
        cls.armande_employee_create_date = cls.task_3_planned_date_begin - relativedelta(months=1, hour=12, minute=0, second=0, microsecond=0)
        cls.env.cr.execute("UPDATE hr_employee SET create_date=%s WHERE id=%s",
                           (cls.armande_employee_create_date, cls.armande_employee.id))
        cls.calendar_morning = cls.env['resource.calendar'].create({
            'name': '20h calendar morning',
            'attendance_ids': [
                Command.create({'name': 'Monday Morning', 'dayofweek': '0', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                Command.create({'name': 'Tuesday Morning', 'dayofweek': '1', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                Command.create({'name': 'Wednesday Morning', 'dayofweek': '2', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                Command.create({'name': 'Thursday Morning', 'dayofweek': '3', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
                Command.create({'name': 'Friday Morning', 'dayofweek': '4', 'hour_from': 8, 'hour_to': 12, 'day_period': 'morning'}),
            ],
            'tz': 'UTC',
        })
        cls.calendar_afternoon = cls.env['resource.calendar'].create({
            'name': '20h calendar afternoon',
            'attendance_ids': [
                Command.create({'name': 'Monday Evening', 'dayofweek': '0', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                Command.create({'name': 'Tuesday Evening', 'dayofweek': '1', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                Command.create({'name': 'Wednesday Evening', 'dayofweek': '2', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                Command.create({'name': 'Thursday Evening', 'dayofweek': '3', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
                Command.create({'name': 'Friday Evening', 'dayofweek': '4', 'hour_from': 13, 'hour_to': 17, 'day_period': 'afternoon'}),
            ],
            'tz': 'UTC',
        })
        cls.armande_departure_date = cls.task_1_planned_date_end.date() + relativedelta(day=29)  # 2021 06 25
        cls.armande_employee.write({
            'departure_date': cls.armande_departure_date,
            'resource_calendar_id': cls.calendar_afternoon.id,
        })
