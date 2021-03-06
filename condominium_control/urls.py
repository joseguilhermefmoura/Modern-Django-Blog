"""condominium_control URL Configuration

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

import users.views
import visitors.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users.views.index, name="index"),
    path('visitantes/registrar-visitante/', visitors.views.register_visitor, name="registrar-visitante"),
    path('visitantes/<int:id>/', visitors.views.visitor_informations, name="visitante"),
]
