"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django1.views import saludo, despedida, dameFecha, calculaEdad, saludo_2, saludo_3, saludo_4, saludo_5, saludo_6, saludo_7, hijo_1, hijo_2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosvemos/', despedida),
    path('fecha/', dameFecha),
    path('edades/<int:edad>/<int:agno>', calculaEdad),

    path('saludo2/', saludo_2),
    path('saludo3/', saludo_3),
    path('saludo4/', saludo_4),
    path('saludo5/', saludo_5),
    path('saludo6/', saludo_6),
    path('saludo7/', saludo_7),
    path('hijo1/', hijo_1),
    path('hijo2/', hijo_2),
]
