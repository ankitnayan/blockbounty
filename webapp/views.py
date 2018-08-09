from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    print ("Inside Index")
    return render(request, 'webapp/index.html')



def team(request):
    print ("Inside team")
    return render(request, 'webapp/team.html')