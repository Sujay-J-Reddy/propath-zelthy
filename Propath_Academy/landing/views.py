from datetime import timedelta
from django.shortcuts import render
from ..packages.crud.base import BaseFormOnlyView
from django.views.generic import TemplateView, FormView
from .forms import EnquiryForm
from ..academy.models import Event, Stat
from django.utils.timezone import now
from zelthy.apps.shared.tenancy.templatetags.zstatic import zstatic

class LandingView(TemplateView):
    template_name = 'landing/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        default_photo = zstatic({"request": self.request},'packages/styles/images/landing/hero1.jpg')
        context['default_photo_url'] = default_photo
        events_queryset = Event.objects.all().order_by('-date')[:3]
        sample_events = [
            Event(name="Sample Event 1", date=now().date() - timedelta(days=1), details="Details of Sample Event 1"),
            Event(name="Sample Event 2", date=now().date() - timedelta(days=2), details="Details of Sample Event 2"),
            Event(name="Sample Event 3", date=now().date() - timedelta(days=3), details="Details of Sample Event 3"),
        ]

        actual_events = list(events_queryset)
        for i in range(3):
            if i < len(actual_events):
                context[f'event{i+1}'] = actual_events[i]
            else:
                context[f'event{i+1}'] = sample_events[i]

        try:
            numbers = Stat.objects.latest('created_at')
        except Stat.DoesNotExist:
            numbers = Stat(students=0, teachers=0, franchises=0)  

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



