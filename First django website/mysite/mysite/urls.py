"""mysite URL Configuration

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
from . import  views


# Class 1
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     # These will acess index in views, second will access about in views
#     path('',views.index, name='index'),
#     path('about/',views.about, name='about')
# ]

# Class 2
urlpatterns = [
    path('admin/', admin.site.urls),

    # These will acess index in views, second will access about in views
    path('',views.index, name='index'),

    # We are using different end points
    # path('removepunc',views.removepunk, name='rempun'),
    # path('newlineremove',views.newlineremove, name='newlineremove'),
    # path('capitalizefirst',views.capfirst, name='capfirst'),
    # path('spaceremover',views.spaceremover, name='spaceremover'),
    # path('charcount',views.charcount, name='charcount'),

    # We decided that we will be using only one end point
    path('analyze',views.analyze, name='analyze'),
    # path('ex1',views.ex1, name='ex1')

]
