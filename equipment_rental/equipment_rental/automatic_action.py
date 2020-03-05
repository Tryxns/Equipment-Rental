from __future__ import unicode_literals
import frappe
from frappe.utils.file_manager import save_url


def create_equipment_for_rent_entry(asset_doc, method):
    if asset_doc.docstatus == 1 and (not len(frappe.get_all("Equipment for rent", filters={
        "asset_item": asset_doc.name
    })) and asset_doc.create_equipment_for_rent_entry == 1):

        eq_rent_item = frappe.get_doc({
            "doctype": "Equipment for rent",
            # "title": asset_doc.asset_name,
            "title": 'RENT-EQ-0000000005',
            "asset_item": asset_doc.name
        })

        eq_rent_item.insert(True)

        if asset_doc.image:
            attach = frappe.db.get_value("File", {"file_url": asset_doc.image}, ["file_name", "file_url", "is_private"], as_dict=1)
            newFile = save_url(attach.file_url, asset_doc.image, "Equipment for rent", eq_rent_item.name, "Home/Attachments", False)
            eq_rent_item.picture_attachment = newFile.file_url
            eq_rent_item.save()
