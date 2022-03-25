"""drf_tut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import *


urlpatterns = [
    path('customers/', CustomerList.as_view()),
    path('customers/<pk>', CustomerDetails.as_view()),
    path('orders/', OrderList.as_view()),
    path('orders/<pk>', OrderDetails.as_view())
]



"""
urlpatterns = [
    path('courses/', views.CourseList.as_view()),
    path('courses/<int:pk>', views.CourseDetails.as_view())
]

"""
