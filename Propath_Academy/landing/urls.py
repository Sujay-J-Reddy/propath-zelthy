from django.urls import path
from .views import EnquiryView, LandingView

urlpatterns = [
    path('enquire/', EnquiryView.as_view(), name='enquiry'),
    path('/',LandingView.as_view(), name='landing')
]