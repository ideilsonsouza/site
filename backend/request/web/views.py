from django.shortcuts import render
from django.http import HttpResponse


def accessible_page(request):
    return HttpResponse("Page Access Test Successful")
