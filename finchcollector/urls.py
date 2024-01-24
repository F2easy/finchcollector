"""
URL configuration for finchcollector project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
     # first arg - url endpoint
  # second arg - the view to render
  # third arg(opt)- names the route
   path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for the index page of our cats
    path('finches/', views.finches_index, name='index'),
    # route for the detail page of our cats
    # we need an id, as well as way to refer to the id (a route parameter)
    path('finches/<int: finch_id>, ', views.finches_detail, name='detail')
 
]
