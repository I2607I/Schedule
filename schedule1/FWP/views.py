from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, View, TemplateView
from .models import *
from .type_current_week import type_current_week

# Create your views here.

# def home(request):
#     #return HttpResponse(f"<h1>Расписание Елизаветы</h1>")
#     return render(request, 'FWP/index.html')


class SchView(ListView):
    model = Lesson
    template_name: str = 'FWP/sc.html'
    context_object_name = 'lessons'
    model2 = Day

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['days'] = list(Day.objects.all())
        context['numbers'] = NumberLesson.objects.all()
        context['parity'] = Parity.objects.filter(name='Even week')
        context['lections'] = TypeLesson.objects.filter(name='Lecture')
        context['seminars'] = TypeLesson.objects.filter(name='Seminar')
        context['time'] = Day.objects.filter(name='Time of lesson')
        context['number_of_lesson'] = NumberLesson.objects.all()
        return context

    def get_queryset(self):
        return Lesson.objects.filter(is_even__name__in=['Even week', 'Every week'])



class HomeView(TemplateView):
    template_name = "FWP/index.html"


class SchParityView(ListView):
    model = Lesson
    template_name: str = 'FWP/sc.html'
    context_object_name = 'lessons'
    model2 = Day

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['days'] = list(Day.objects.all())
        context['numbers'] = NumberLesson.objects.all()
        # context['parity'] = Parity.objects.filter(name=parity_slug)
        context['lections'] = TypeLesson.objects.filter(name='Lecture')
        context['seminars'] = TypeLesson.objects.filter(name='Seminar')
        context['time'] = Day.objects.filter(name='Time of lesson')
        context['number_of_lesson'] = NumberLesson.objects.all()
        context['cur_week'] = type_current_week()
        # print(context['parity_slug'])
        return context

    def get_queryset(self):
        if self.kwargs['parity_slug'] == 'odd':
            return Lesson.objects.filter(is_even__name__in=['Odd week', 'Every week'])
        if self.kwargs['parity_slug'] == 'even':
            return Lesson.objects.filter(is_even__name__in=['Even week', 'Every week'])



class SubjectView(ListView):
    model = Lesson
    template_name: str = 'FWP/lesson.html'
    context_object_name = 'lessons'
    slug_url_kwarg = 'subject_slug'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Subject'
        return context


    def get_queryset(self):
        return Lesson.objects.filter(subject__slug=self.kwargs['subject_slug'])
