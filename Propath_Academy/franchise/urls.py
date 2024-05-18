from django.urls import path
from .views import FranchiseeCrudView, StudentCrudView, LevelCertificateCrudView

urlpatterns = [
    path('franchisees/', FranchiseeCrudView.as_view(), name='franchisee_crud'),
    path('students/', StudentCrudView.as_view(), name='students_crud'),
    path('certificates/', LevelCertificateCrudView.as_view(), name='certificates_crud')
]
