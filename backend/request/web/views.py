from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class DownloadsView(View):
    template_name = 'home/downloads.html'
    
    def get(self, request):
        context = {}
        return render (request, self.template_name, context)

class HomeView(View):
    template_name = 'home/home.html'

    def get(self, request):
        context = {}
        return render (request, self.template_name, context)


def accessible_page(request):
    return HttpResponse("Page Access Test Successful")
