from ..packages.crud.forms import BaseForm
from ..packages.crud.form_fields import ModelField, CustomSchemaField
from .models import Competition, CompetitionResult, School, SchoolStudent, Event
from ..notifications.models import Notification
from django import forms

class EventForm(BaseForm):
    name = ModelField(placeholder="Name", required=True, required_msg="This field is required")
    date = ModelField(placeholder="Date", required=True, required_msg="This field is required")
    photo = ModelField(placeholder="Photo", required=True, required_msg="This field is required")
    details = ModelField(placeholder="Details", required=True, required_msg="This field is required")

    class Meta:
        model = Event
        title = "Event Details"
        order = [
            "name",
            "date",
            "photo",
            "details",
        ]


      
class CompetitionForm(BaseForm):
    circular_no = ModelField(placeholder="Circular Number", required=True, required_msg="This field is required")
    name  = ModelField(placeholder="Name", required=True, required_msg="This field is required")
    level_cutoff_date = ModelField(placeholder="Level cutoff date", required=True, required_msg="This field is required")
    pdf_file = ModelField(placeholder="Circular PDF", required=True, required_msg="This field is required")

    class Meta:
        model = Competition
        title = "Add new competition"
        order =[
            "circular_no",
            "name",
            "level_cutoff_date",
            "pdf_file"
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            Notification.objects.create(
                account_type = "franchise",
                notification_type = "competition_announcement",
                details = "Dear Franchisee, a new competition has been scheduled, please visit the Competitions page for more details and registration."
            )
            instance.save()
        return instance

class CompetitionResultForm(BaseForm):
    competition = ModelField(placeholder="Competition", required=True, required_msg="This field is required")
    student = ModelField(placeholder="Student", required=True, required_msg="This field is required")
    rank = ModelField(placeholder="Rank", required=True, required_msg="This field is required")

    class Meta:
        model = CompetitionResult
        title = "Announce Competition Results"
        order = [
            "competition",
            "student",
            "rank"
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        franchise = instance.student.franchise
        if commit:
            Notification.objects.create(
                account_type = "franchise",
                notification_type = "competition_announcement",
                franchise_id = franchise.id,
                details = f'Dear {franchise.name}, Results of competition ({instance.competition.circular_no}) has been announced, visit the Competition results in Competition Page for more information.'
            )
            instance.save()
        return instance

class SchoolForm(BaseForm):
    name  = ModelField(placeholder="School Name", required=True, required_msg="This field is required")
    contact = ModelField(placeholder="Contact", required=True, required_msg="This field is required")
    mail = ModelField(placeholder="Mail", required=True, required_msg="This field is required")
    location = ModelField(placeholder="Location", required=True, required_msg="This field is required")

    class Meta:
        model = School
        title = "School Details"
        order = [
            "name",
            "contact",
            "mail",
            "location"
        ]

class SchoolStudentForm(BaseForm):
    name = ModelField(placeholder="Student Name", required=True, required_msg="This field is required")
    school = ModelField(placeholder="School", required=True, required_msg="This field is required")
    course = ModelField(placeholder="Course", required=True, required_msg="This field is required")
    programme = ModelField(placeholder="Program", required=True, required_msg="This field is required")
    level = ModelField(placeholder="Level", required=True, required_msg="This field is required")
    dob = ModelField(placeholder="Dob", required=True, required_msg="This field is required")
    contact = ModelField(placeholder="Contact", required=True, required_msg="This field is required")
    # school_names = CustomSchemaField(
    #     required=True,
    #     schema={
    #         "type": "string",
    #         "title": "School",
    #                         },
    #     ui_schema={
            
         
    #       "ui:tooltip": "School Name",
    #       "ui:classNames": "col-span-12 sm:col-span-6",
    #       "ui:widget": "select",
    #       "ui:placeholder": "Choose a School",
    #       "ui:errorMessages": {
    #         "required": "This field is required."
    #       }
        
      
    #     }
    # )
    class Meta:
        model = SchoolStudent
        title = "School Student Details"
        order = [
            "name",
            "school",
            "course",
            "programme",
            "level",
            "dob",
            "contact"
        ]

    # def __init__(self, *args, **kwargs):
    #     super(SchoolStudentForm, self).__init__(*args, **kwargs)
    #     instance = kwargs.get("instance")
    #     schools = [str(school.pk) for school in School.objects.all()]
    #     self.custom_schema_fields["school_names"].schema["enum"] = schools
    #     self.custom_schema_fields["school_names"].schema["enumNames"] = [obj.name for obj in School.objects.all()]
    #     if instance is not None:
    #         self.update = True
    #         items = School.objects.all().values_list("id")
    #         self.custom_schema_fields["school_names"].schema["enum"] = schools
    #         self.custom_schema_fields["school_names"].schema["enumOptions"] = [obj.name for obj in School.objects.all().values_list("name")]
        
