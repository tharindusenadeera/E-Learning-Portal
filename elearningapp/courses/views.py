from django.shortcuts import render
from django.http import HttpResponse


def my_first_view(request):
    return HttpResponse("Hello Students !!!")
