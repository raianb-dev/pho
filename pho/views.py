from django.shortcuts import render

def pagina_vendas (requests):
    return render(requests, 'sem-delay.html')
def pagina_vendas_delay (requests):
    return render(requests, 'com-delay.html')
