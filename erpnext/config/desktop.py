from frappe import _

def get_data():
	return {
		"Accounts": {
            "label": _("Accounts"),
			"color": "#3498db",
			"icon": "icon-money",
			"type": "module"
		},
		"Activity": {
			"color": "#e67e22",
			"icon": "icon-play",
			"label": _("Activity"),
			"link": "activity",
			"type": "page"
		},
		"Buying": {
            "label": _("Buying"),
			"color": "#c0392b",
			"icon": "icon-shopping-cart",
			"type": "module"
		},
		"HR": {
			"color": "#2ecc71",
			"icon": "icon-group",
			"label": _("Human Resources"),
			"type": "module"
		},
		"Manufacturing": {
            "label": _("Manufacturing"),
			"color": "#7f8c8d",
			"icon": "icon-cogs",
			"type": "module"
		},
		"Notes": {
			"color": "#95a5a6",
			"doctype": "Note",
			"icon": "icon-file-alt",
			"label": _("Notes"),
			"link": "List/Note",
			"type": "list"
		},
		"Projects": {
            "label": _("Projects"),
			"color": "#8e44ad",
			"icon": "icon-puzzle-piece",
			"type": "module"
		},
		"Selling": {
            "label": _("Selling"),
			"color": "#1abc9c",
			"icon": "icon-tag",
			"type": "module"
		},
		"Stock": {
            "label": _("Stock"),
			"color": "#f39c12",
			"icon": "icon-truck",
			"type": "module"
		},
		"Support": {
            "label": _("Support"),
			"color": "#2c3e50",
			"icon": "icon-phone",
			"type": "module"
		}
	}
