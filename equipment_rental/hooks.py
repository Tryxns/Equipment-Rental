# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "equipment_rental"
app_title = "Equipment Rental"
app_publisher = "Jevon"
app_description = "My first app on vagrant"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "fabian.jevon@coway.id"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/equipment_rental/css/equipment_rental.css"
# app_include_js = "/assets/equipment_rental/js/equipment_rental.js"

# include js, css files in header of web template
# web_include_css = "/assets/equipment_rental/css/equipment_rental.css"
# web_include_js = "/assets/equipment_rental/js/equipment_rental.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "equipment_rental.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "equipment_rental.install.before_install"
# after_install = "equipment_rental.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "equipment_rental.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
    "Asset": {
        "on_submit": "equipment_rental.equipment_rental.automatic_action.create_equipment_for_rent_entry"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"equipment_rental.tasks.all"
# 	],
# 	"daily": [
# 		"equipment_rental.tasks.daily"
# 	],
# 	"hourly": [
# 		"equipment_rental.tasks.hourly"
# 	],
# 	"weekly": [
# 		"equipment_rental.tasks.weekly"
# 	]create_equipment_for_rent_entry
# }

# Testing
# -------

# before_tests = "equipment_rental.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "equipment_rental.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "equipment_rental.task.get_dashboard_data"
# }

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name", "in",
                [
                    "Asset-create_equipment_for_rent_entry",
                ]
            ]
        ]
    }
]
