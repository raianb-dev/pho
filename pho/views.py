from django.shortcuts import render

def pagina_vendas (requests):
    return render(requests, 'index.html')

def pagina_vendas_delay (requests):
    return render(requests, 'com-delay.html')
