from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello, {}, voce tem {} anos </h1>'.format(nome, idade))
def gatos(request, gato1, gato2):
    return HttpResponse('Os nomes dos seus gatos são: {} e {}'.format(gato1, gato2))