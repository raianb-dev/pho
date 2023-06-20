"""infoprod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pho import views as views_pho
from appsecreto import views as views_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_pho.pagina_vendas, name='pvd'),
    path('profissao-homeoffice', views_pho.pagina_vendas, name='pv'),
    path('profissao-homeoffice/video', views_pho.pagina_vendas_delay, name='video'),
    path('app', views_app.redirect, name='app'),
]
