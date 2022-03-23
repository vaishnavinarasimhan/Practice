from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('signin', views.signin, name='signin'),
    path('signinfirst', views.signinfirst, name='signinfirst'),
    path('signout', views.signout, name='signout'),
    path('register', views.register, name='register'),
]