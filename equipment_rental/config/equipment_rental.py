from frappe import _


def get_data():
    return [{
        "label": _("Equipment Rental"),
        "items": [
            {
                "type": "docttype",
                "name": "rental booking"
            },
            {
                "type": "docttype",
                "name": "Equipment For Rent"
            }
        ]
    }]
