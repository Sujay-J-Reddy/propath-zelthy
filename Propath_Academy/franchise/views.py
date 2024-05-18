from zelthy.core.utils import get_current_role
from ..packages.crud.base import BaseCrudView
from .tables import FranchiseeTable, StudentTable, LevelCertificateTable
from .forms import FranchiseeForm, StudentForm, StudentLevelForm
from django.views import View
from django.http import HttpResponse


class FranchiseeCrudView(BaseCrudView):
    page_title = "Franchisee"
    add_btn_title = "Add New Francisee"
    table = FranchiseeTable
    form = FranchiseeForm

    def has_add_perm(self, request):
        return True

    def display_add_button_check(self, request):
        return get_current_role().name in ['Admin']
    
    def display_download_button_check(self, request):
        return get_current_role().name in ['Admin']

class StudentCrudView(BaseCrudView):
    page_title = "Student"
    add_btn_title = "Add New Student"
    table = StudentTable
    form = StudentForm

    def has_add_perm(self, request):
        return True

    def display_add_button_check(self, request):
        return get_current_role().name in [ 'Franchisee']
    
class LevelCertificateCrudView(BaseCrudView):
    page_title = "Level Certificate Requests"
    add_btn_title = "Add"
    table = LevelCertificateTable
    form = StudentLevelForm

    def has_add_perm(self, request):
        return True
    
    def display_add_button_check(self, request):
        return get_current_role().name in [ 'Franchisee']
    
# class TestView(View):
#     def get(self,request, *args, **kwargs):
#         return HttpResponse("")

