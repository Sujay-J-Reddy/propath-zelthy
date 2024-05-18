from ..packages.crud.detail.base import BaseDetail
from ..packages.crud.table.column import ModelCol, StringCol

class SchoolStudentDetail(BaseDetail):
    def get_title(self, obj, object_data):
        return f"{obj.name}"


class SchoolDetail(BaseDetail):
    def get_title(self, obj, object_data):
        return f"{obj.name}"

class CompetitionResultDetail(BaseDetail):
    def get_title(self, obj, object_data):
        return f"{obj.student.s_id} - {obj.student.name}'s Rank in {obj.competition.name}"

class CompetitionDetail(BaseDetail):
    def get_title(self, obj, object_data):
        return f"{obj.circular_no} - {obj.name}"

class EventDetail(BaseDetail):
    name = ModelCol(display_as="Name")
    date = ModelCol(display_as="Date")
    photo = ModelCol(display_as="Photo")
    details = ModelCol(display_as="Details")

    class Meta:
        fields = [
            "name",
            "date",
            "photo",
            "details",
        ]

    def photo_getval(self, obj):
        return f"<img src = {obj.photo.url}>"
    
    def get_title(self, obj, object_data):
        return f"{obj.name}"
    
class EnquiryDetail(BaseDetail):

    def get_title(self, obj, object_data):
        return f"{obj.name}' s Enquiry"