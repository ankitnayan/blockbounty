from django.shortcuts import render

from django.http import HttpResponse


def index(request):

    return render(request, 'webapp/index.html')



def about(request):

    return render(request, 'webapp/about.html')