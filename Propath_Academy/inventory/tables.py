from django.db.models import Q
from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol, StringCol
from .forms import KitForm, VendorForm, ItemForm, LogForm, OrderForm, SchoolOrderForm
from .models import Kit, Vendor, Item, Log, Order, SchoolOrder
from .details import OrderDetail, SchoolOrderDetail, LogDetail, KitDetail, ItemDetail, OrderDetail
from .utils import json_to_html_table
import json
class KitTable(ModelTable):
    name = ModelCol(display_as="Kit Name", sortable=True, searchable=True)
    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Kit",
            "type": "form",
            "form": KitForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = Kit
        detail_class = KitDetail
        fields = ["name"]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
    
class VendorTable(ModelTable):
    name = ModelCol(display_as="Vendor Name", searchable=True, sortable=True)
    contact = ModelCol(display_as="Contact", searchable=True, sortable=True)
    location = ModelCol(display_as="Location", searchable=True ,sortable=True)
    table_actions = []
    row_actions =[
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Vendor",
            "type": "form",
            "form": VendorForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = Vendor
        fields = [
            "name",
            "contact",
            "location"
        ]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()

class ItemTable(ModelTable):
    name = ModelCol(display_as="Item Name", searchable=True, sortable=True)
    description = ModelCol(display_as="Description", searchable=True, sortable=True)
    qty = ModelCol(display_as="Quantity", searchable=True, sortable=True)
    last_purchase_price = ModelCol(display_as="Last Purchase Price", searchable=True, sortable=True)
    kit = ModelCol(display_as="Kit Name", searchable=True, sortable=True)
    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Item",
            "type": "form",
            "form": ItemForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = Item
        detail_class = ItemDetail
        fields = [
            "name",
            "description",
            "qty",
            "last_purchase_price",
            "kit",
        ]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
    
    def kit_getval(self, obj):
        return obj.kit.name

class LogTable(ModelTable):
    vendor = ModelCol(display_as="Vendor Name", searchable=True, sortable=True)
    date = ModelCol(display_as="Date", searchable=True, sortable=True)
    items = ModelCol(display_as="Items", searchable=True, sortable=True)
    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Logs",
            "type": "form",
            "form": LogForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = Log
        detail_class = LogDetail
        fields = [
            "vendor",
            "date",
            "items"
        ]

    def items_getval(self, obj):
        html = json_to_html_table(obj.items)
        return html
    
    def vendor_getval(self, obj):
        return f"{obj.vendor.name}"

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
    
class OrderTable(ModelTable):
    id = ModelCol(display_as="DC Number", searchable=True, sortable=True)
    franchise = ModelCol(display_as="Franchise", searchable=True, sortable=True, user_roles=["Admin"])
    kits = ModelCol(display_as="Kits", searchable=True, sortable=True)
    items = ModelCol(display_as="Items", searchable=True, sortable=True)
    order_date = ModelCol(display_as="Order Date", searchable=True, sortable=True)
    table_actions = []
    row_actions = []

    class Meta:
        model = Order
        detail_class = OrderDetail
        fields = [
            "id",
            "franchise",
            "kits",
            "items",
            "order_date",
        ]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
    
    def kits_getval(self, obj):
        if obj.kits != None:
            html = json_to_html_table(obj.kits)
            return html
        return "None"
    
    def items_getval(self, obj):
        if obj.items != None:
            html = json_to_html_table(obj.items)
            return html
        return "None"
    
class SchoolOrderTable(OrderTable):
    id = ModelCol(display_as="Order ID", searchable=True, sortable=True)
    school = ModelCol(display_as="School", searchable=True, sortable=True)
    kits = ModelCol(display_as="Kits", searchable=True, sortable=True)
    items = ModelCol(display_as="Items", searchable=True, sortable=True)
    order_date = ModelCol(display_as="Order Date", searchable=True, sortable=True)
    table_actions = []
    row_actions = []

    class Meta:
        model = SchoolOrder
        detail_class = SchoolOrderDetail
        fields = [
            "id",
            "school",
            "kits",
            "items",
            "order_date",
        ]

    def kits_getval(self, obj):
        if obj.kits != None:
            html = json_to_html_table(obj.kits)
            return html
        return "None"
    
    def items_getval(self, obj):
        if obj.items != None:
            html = json_to_html_table(obj.items)
            return html
        return "None"
    
    def school_getval(self, obj):
        return obj.school.name
    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
