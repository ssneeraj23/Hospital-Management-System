from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('doctor',views.doctor, name = 'doctor'),
    path('pl',views.pl,name = 'pl'),
    path('pi',views.pi,name = 'pi'),
    path('ri',views.ri,name = 'ri'),
    path('pr',views.pr,name = 'pr')
]