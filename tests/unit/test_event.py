# -*- coding: utf-8 -*-

from datetime import datetime

from odoo.tests.common import TransactionCase

class TestEvent(TransactionCase):

    TESTED_MODEL_NAME = 'agenda_esi.event'

    def test_valid_event_creation(self):
        start_datetime = datetime(2019, 1, 1, 12, 0, 0)
        end_datetime = datetime(2019, 1, 1, 13, 0, 0)
        record = self.env[self.TESTED_MODEL_NAME].create({
            'title': 'My Awesome Party',
            'periodicity': 'd',
            'start_datetime': start_datetime, 
            'end_datetime': end_datetime, 
            'capacity': 1
        })
        # TODO: We should be testing the start and end time.
        self.assertEqual(record.periodicity, 'd')
        self.assertEqual(record.capacity, 1)