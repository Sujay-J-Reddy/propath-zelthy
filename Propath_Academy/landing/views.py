from django.shortcuts import render
from ..packages.crud.base import BaseFormOnlyView
from django.views.generic import TemplateView, FormView
from .forms import EnquiryForm
class LandingView(TemplateView):
    template_name = 'landing/base.html'

class CoursesView(TemplateView):
    template_name = 'landing/courses.html'

class ContactView(TemplateView):
    template_name = 'landing/contact.html'

class AbacusView(TemplateView):
    template_name = 'landing/abacus.html'

class AbacusCourseView(TemplateView):
    template_name = 'landing/abacuscourse.html'

class VedicMathsView(TemplateView):
    template_name = 'landing/vedicmaths.html'

class VedicCourseView(TemplateView):
    template_name = 'landing/vediccourse.html'
class AboutUsView(TemplateView):
    template_name = 'landing/about_us.html'

class HandwritingView(TemplateView):
    template_name = 'landing/handwriting.html'

class HandwritingCourseView(TemplateView):
    template_name = 'landing/handwritingcourse.html'

class EnquiryView(BaseFormOnlyView):
    form = EnquiryForm
    success_url = '/'
    page_title = "Enquiry Form"



