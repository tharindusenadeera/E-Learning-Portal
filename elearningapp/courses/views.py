from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, CreateView, ListView

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from courses.forms import CourseForm
from courses.models import Course, Section, UserAnswer, Question


# def my_first_view(request, who):
#     # return HttpResponse("Hello Students !!!")
#     return HttpResponse("Hello %s!!!" %who)


class CourseDetailView(DetailView):
    model = Course

course_detail = CourseDetailView.as_view()

def course_list(request):
    courses = Course.objects.prefetch_related('students')
    return render(request, 'courses/course_list.html', {
        'courses': courses,
    })

def course_add(request):
    if request.POST:
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            return HttpResponseRedirect(new_course.get_absolute_url())