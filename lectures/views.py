from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Lecture
# Create your views here.

class LectureListView(ListView):
    model = Lecture
    ordering = '-time'

class LectureDetailView(DetailView):
    model = Lecture

class LecturesByInstitution(ListView):
    def dispatch(self, request, *args, **kwargs):
        self.institution_id = kwargs.get('institution_id')
        # print self.institution_id
        return super(LecturesByInstitution, self).dispatch(
            request, *args, **kwargs)

    def get_queryset(self):
        return Lecture.objects.filter(
            institution_id = self.institution_id)
