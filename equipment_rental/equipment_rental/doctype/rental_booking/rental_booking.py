# -*- coding: utf-8 -*-
# Copyright (c) 2020, Jevon and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class RentalBooking(Document):
    def validate(self):
        print('Rentalbooking')
        rules = frappe.get_all("Rental Booking", filters=[
            ['status', 'in', ['booked', 'out']],
            ['booking_date', '>=', self.booking_date],
            ['booking_date', '<=', self.return_date],
            ['return_date', '>=', self.booking_date],
            ['return_date', '<=', self.return_date],
            ['name', '!=', self.name],
            ['item_to_rent', '=', self.item_to_rent],
            ['docstatus', '=', 1],
        ])

        violations = []
        for x in rules:
            violations.append(x)

        if len(violations) > 0:
            frappe.msgprint('invalid!', raise_exception=1)
