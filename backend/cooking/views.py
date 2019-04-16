from django.shortcuts import render

def index(request):
    return render(request, 'cooking/index.html')

def variable_list(request):
    return render(request, 'cooking/show.html')