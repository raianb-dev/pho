from django.shortcuts import render

def redirect (request):
    return render(request, 'app.html')
