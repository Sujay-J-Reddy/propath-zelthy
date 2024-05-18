from ..packages.crud.table.base import ModelTable
from ..packages.crud.table.column import ModelCol, StringCol
from django.db.models import Q
from .models import Teacher, InstructorFeedback
from .forms import TeacherForm, TeacherLevelForm
from .utils import get_current_teacher
from zelthy.core.utils import get_current_role

class TeacherTable(ModelTable):
    name = ModelCol(display_as="Name", sortable=True, searchable=True)
    photo = ModelCol(display_as="Photo", sortable=True, searchable=True)
    centre_name = ModelCol(display_as="Centre Name", sortable=True, searchable=True)
    franchise = ModelCol(display_as="Franchise", sortable=True, searchable=True)
    program_name = ModelCol(display_as="Program Name", sortable=True, searchable=True)
    dob = ModelCol(display_as="Date of Birth", sortable=True, searchable=True)
    training_level = ModelCol(display_as="Training Level", sortable=True, searchable=True)
    due_date = ModelCol(display_as="Due Date", sortable=True, searchable=True)
    address = ModelCol(display_as="Address", sortable=True, searchable=True)
    city = ModelCol(display_as="City", sortable=True, searchable=True)
    state = ModelCol(display_as="State", sortable=True, searchable=True)
    contact_no = ModelCol(display_as="Contact Number", sortable=True, searchable=True)
    email = ModelCol(display_as="Email", sortable=True, searchable=True)
    table_actions =[]
    row_actions = [
        {
            "name": "Edit",
            "key": "edit",
            "description": "Edit Teacher Details",
            "type": "form",
            "form": TeacherForm,  # Specify the form to use for editing
            "roles": [
                "Admin"
            ],  # Specify roles that can perform the action
        },
        {
            "name": "Update Teacher Level",
            "key": "update_teacher_level",
            "description": "Update Teachers Training Level",
            "type": "form",
            "form": TeacherLevelForm,  # Specify the form to use for editing
            "roles": [
                "Admin",
            ],  
        }
    ]

    class Meta:
        model = Teacher
        fields = [
            "name",
            "photo",
            "centre_name",
            "franchise",
            "program_name",
            "dob",
            "training_level",
            "due_date",
            "address",
            "city",
            "state",
            "contact_no",
            "email",
        ]
    
    def can_perform_row_action_edit(self, request, obj):
        # Implement logic to check if the user can perform the Edit action
        # Example: Check if the user has the necessary permissions to edit records
        return True
    
    def can_perform_row_action_update_teacher_level(self, request, obj):
        # Implement logic to check if the user can perform the Edit action
        # Example: Check if the user has the necessary permissions to edit records
        return True
    
    def perform_row_action_edit(self, request, obj):
        pass

    def perform_row_action_update_teacher_level(self, request, obj):
        pass
    
    def id_Q_obj(self, search_term):
        try:
            modified_id = int(search_term) 
        except ValueError:
            modified_id = None  # Not an integer, ignore
        if modified_id is not None:
            return Q(id=modified_id)
        return Q()
    
    def get_table_data_queryset(self):
        queryset = super().get_table_data_queryset()
        role = get_current_role()
        if role.name == 'teacher':
            return queryset.filter(name=get_current_teacher().name)
        else:
            return queryset

class InstructorFeedbackTable(ModelTable):
    teacher = ModelCol(display_as = "Name", searchable = True, sortable = True)
    completed_level = ModelCol(display_as = "Level Completed", searchable = True, sortable = True)
    current_level = ModelCol(display_as = "Current Level", searchable = True, sortable = True)
    center_name = ModelCol(display_as = "Center Name", searchable = True, sortable = True)
    center_address = ModelCol(display_as = "Center Address", searchable = True, sortable = True)
    punctuality = ModelCol(display_as = "Punctuality", searchable = True, sortable = True)
    attention_to_instructor = ModelCol(display_as = "Attention To Instructor", searchable = True, sortable = True)
    problem_solving_skills = ModelCol(display_as = "Problem Solving Skills", searchable = True, sortable = True)
    innovative_method = ModelCol(display_as = "Innovative Methods Used", searchable = True, sortable = True)
    teaching_method = ModelCol(display_as = "Teaching Method", searchable = True, sortable = True)
    sharing_experiences = ModelCol(display_as = "Sharing Experiences", searchable = True, sortable = True)
    comments_suggestions = ModelCol(display_as = "Comments/Suggestions", searchable = True, sortable = True)
    date = ModelCol(display_as = "Date", searchable = True, sortable = True)
    table_actions = []
    row_actions = []

    class Meta:
        model = InstructorFeedback
        fields = [
            "teacher",
            "completed_level",
            "current_level",
            "center_name",
            "center_address",
            "punctuality",
            "attention_to_instructor",
            "problem_solving_skills",
            "innovative_method",
            "teaching_method",
            "sharing_experiences",
            "comments_suggestions",
            "date",
        ]

    def get_table_data_queryset(self):
        queryset = super().get_table_data_queryset()
        role = get_current_role()
        if role.name == 'teacher':
            return queryset.filter(name=get_current_teacher().name)
        else:
            return queryset    