from django.http import HttpResponse, Http404

from django.shortcuts import render


def index(request):
    return HttpResponse()
    return render(request, 'blog/index.html', {'user_list': None})


def about(request, name='Павел', age=4):
    return render(request, 'blog/about.html')