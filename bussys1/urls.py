"""
URL configuration for bussys1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from busenquiry import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/company/',views.TransportCompanyListCreate.as_view()),
    path('api/company/<int:pk>/',views.TransposrtCompanyRetrieveUpdateDestroy.as_view()),

    path('api/buses/',views.BusListCreate.as_view()),
    path('api/buses/<int:pk>/',views.BusRetrieveUpdateDestroy.as_view()),

    path('api/stops/',views.StopsListCreate.as_view()),
    path('api/stops/<int:pk>/',views.StopsRetrieveUpdateDestroy.as_view()),

    path('api/routes/',views.RoutesListCreate.as_view()),
    path('api/routes/<int:pk>/',views.RoutesRetrieveUpdateDestroy.as_view()),

    path('api/schedule/',views.ScheduleListCreate.as_view()),
    path('api/schedule/<int:pk>/',views.ScheduleRetrieveUpdateDestroy.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
