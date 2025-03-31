from django.shortcuts import render

def index(request):
    context = {"secret": "kakkulapio"}
    return render(request, 'hello/index.html', context)
