from __future__ import unicode_literals

import frappe
import json

@frappe.whitelist()
def bulk_insert(data):
    data = frappe._dict(json.loads(data))
    equipments_for_rent = data["equipments_for_rent"]

    for eq in equipments_for_rent:
        new_equipment = frappe.get_doc({
            "doctype": "Equipment for rent",
            "title": eq["title"],
            "description": eq["description"]
        })

    new_equipment.save(True)
