from django.db.models import Q
from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol, StringCol
from .models import Competition, CompetitionResult, CompetitionStudent, School, SchoolStudent, Enquiry, Event
from .forms import CompetitionForm, CompetitionResultForm, SchoolForm, SchoolStudentForm, EventForm
from ..franchise.forms import CompetitionStudentForm
from . details import EventDetail, EnquiryDetail, CompetitionDetail, CompetitionResultDetail, SchoolDetail, SchoolStudentDetail
from django.db.models import F, Value, CharField
from django.db.models.functions import Concat

class EventTable(ModelTable):
    name = ModelCol(display_as="Name", sortable=True, searchable=True)
    date = ModelCol(display_as="Date", sortable=True, searchable=True)
    photo = ModelCol(display_as="Photo", sortable=True, searchable=True)
    details = ModelCol(display_as="Details", sortable=True, searchable=True)
    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Event",
            "type": "form",
            "form": EventForm,  # Specify the form to use for editing
            "roles": [
                "Admin", "AnonymousUsers"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = Event
        detail_class = EventDetail
        fields = [
            "name",
            "date",
            "photo",
            "details"
        ]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()

class EnquiryTable(ModelTable):
    name = ModelCol(display_as="Name", sortable=True, searchable=True)
    mail = ModelCol(display_as="Mail", sortable=True, searchable=True)
    type = ModelCol(display_as="Type", sortable=True, searchable=True)
    phone_country_code = ModelCol(display_as="Phone Country Code", sortable=True, searchable=True)
    phone_number = ModelCol(display_as="Phone Number", sortable=True, searchable=True)
    city = ModelCol(display_as="City", sortable=True, searchable=True)
    pin = ModelCol(display_as="Pin", sortable=True, searchable=True)
    state = ModelCol(display_as="State", sortable=True, searchable=True)
    country = ModelCol(display_as="Country", sortable=True, searchable=True)
    date = ModelCol(display_as="Date", sortable=True, searchable=True)
    table_actions = []
    row_actions = []

    class Meta:
        model = Enquiry
        detail_class = EnquiryDetail
        fields = [
            "name",
            "mail",
            "type",
            "phone_country_code",
            "phone_number",
            "city",
            "pin",
            "state",
            "country",
            "date",
        ]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()

class CompetitionTable(ModelTable):
    circular_no = ModelCol(display_as="Circular Number", sortable=True, searchable=True)
    name = ModelCol(display_as="Name", sortable=True, searchable=True)
    level_cutoff_date = ModelCol(display_as="Level Cut off Date", sortable=True, searchable=True)
    pdf_file = ModelCol(display_as="PDF File", sortable=True, searchable=True)
    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Competition",
            "type": "form",
            "form": CompetitionForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        },
        {
            "name": "Register",
            "key": "register_students",
            "description": "Register students for competition",
            "type": "form",
            "form": CompetitionStudentForm,  # Specify the form to use for editing
            "roles": [
                "Franchisee", "AnonymousUsers"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = Competition
        detail_class = CompetitionDetail
        fields = [
            "circular_no",
            "name",
            "level_cutoff_date",
            "pdf_file",
        ]
        # row_selector = {"enabled": True, "multi": False}

    def can_perform_row_action_edit(self, request, obj):
        # Implement logic to check if the user can perform the Edit action
        # Example: Check if the user has the necessary permissions to edit records
        return True
    

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()

class CompetitionResultTable(ModelTable):
    competition = ModelCol(display_as="Competition", sortable=True, searchable=True)
    student  = ModelCol(display_as="Student", sortable=True, searchable=True)
    franchise = StringCol(display_as="Franchise", sortable=True, searchable=True, user_roles = ["Admin"])
    rank = ModelCol(display_as="Rank", sortable=True, searchable=True)

    table_actions = []
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Competition Results",
            "type": "form",
            "form": CompetitionResultForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = CompetitionResult
        detail_class = CompetitionResultDetail
        fields = [
            "competition",
            "student",
            "rank",
        ]
        # row_selector = {"enabled": True, "multi": False}
    
    def competition_getval(self, obj):
        return f"{obj.competition.circular_no} - {obj.competition.name}"
    def student_getval(self, obj):
        return f"{obj.student.s_id} - {obj.student.name}"
    def franchise_getval(self, obj):
        return obj.student.franchise.name
    def can_perform_row_action_edit(self, request, obj):
        # Implement logic to check if the user can perform the Edit action
        # Example: Check if the user has the necessary permissions to edit records
        return True

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()    
class CompetitionStudentTable(ModelTable):
    circular_no = StringCol(display_as="Circular Number", sortable=False, searchable=True)
    franchise = StringCol(display_as="Franchise", sortable=True, searchable=True)
    student = StringCol(display_as="Students", sortable=True, searchable=True)
    date = ModelCol(display_as="Date", sortable=True, searchable=True)
    table_actions = []
    row_actions = []    
    class Meta:
        model = CompetitionStudent
        fields = [
            "franchise",
            "student",
            "date",
        ]
        # row_selector = {"enabled": True, "multi": False}

    def circular_no_getval(self, obj):
        return obj.competition.circular_no
    
    def franchise_getval(self, obj):
        return obj.franchise.name
    
    def student_getval(self, obj):
        return f'{obj.student.s_id} - {obj.student.name}'
    
    # def get_table_data_queryset(self):
    #     query = CompetitionStudent.objects.values('competition', 'franchise', 'date', 'modified_at', 'created_at').distinct()
    #     print(query, flush=True)
    #     return query
    def get_table_data_queryset(self):
        annotated_queryset = CompetitionStudent.objects.annotate(composite_key=Concat(F('competition'), Value('-'), F('franchise')))
        distinct_entries = annotated_queryset.filter(composite_key__in=annotated_queryset.values('composite_key').distinct())
        return distinct_entries    
    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()

class SchoolTable(ModelTable):
    name = ModelCol(display_as="Name", searchable=True, sortable=True)
    contact = ModelCol(display_as="Contact", searchable=True, sortable=True)
    mail = ModelCol(display_as="Mail", searchable=True, sortable=True)
    location = ModelCol(display_as="Location", searchable=True, sortable=True)
    table_actions = []
    row_actions =[
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit School Details",
            "type": "form",
            "form": SchoolForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = School
        detail_class = SchoolDetail
        fields = [
            "name",
            "contact",
            "mail",
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
    
    def can_perform_row_action_edit(self, request, obj):
        # Implement logic to check if the user can perform the Edit action
        # Example: Check if the user has the necessary permissions to edit records
        return True
    
class SchoolStudentTable(ModelTable):
    name = ModelCol(display_as="Name", searchable=True, sortable=True)
    school = ModelCol(display_as="School", searchable=True, sortable=True)
    course = ModelCol(display_as="Course", searchable=True, sortable=True)
    programme = ModelCol(display_as="Programme", searchable=True, sortable=True)
    level = ModelCol(display_as="Level", searchable=True, sortable=True)
    dob = ModelCol(display_as="Dob", searchable=True, sortable=True)
    contact = ModelCol(display_as="Contact", searchable=True, sortable=True)
    table_actions = []
    row_actions =[
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit School Details",
            "type": "form",
            "form": SchoolStudentForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        }
    ]

    class Meta:
        model = SchoolStudent
        detail_class = SchoolStudentDetail
        fields = [
            "name",
            "school",
            "course",
            "programme",
            "level",
            "dob",
            "contact",
        ]

    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
    
    def can_perform_row_action_edit(self, request, obj):
        # Implement logic to check if the user can perform the Edit action
        # Example: Check if the user has the necessary permissions to edit records
        return True
    
    def school_getval(self, obj):
        return f"{obj.school.name}"
    
 