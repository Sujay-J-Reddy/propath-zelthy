from django.shortcuts import render
from ..packages.crud.base import BaseFormOnlyView
from django.views.generic import TemplateView, FormView
from .forms import EnquiryForm
from ..academy.models import Event, Stat

class LandingView(TemplateView):
    template_name = 'landing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events_queryset = Event.objects.all().order_by('-date')[:3]
        numbers = Stat.objects.latest('created_at')
        context['event1'] = events_queryset[0]
        context['event2'] = events_queryset[1]
        context['event3'] = events_queryset[2]
        context['numbers'] = numbers
        return context

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



