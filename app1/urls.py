from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('profile',views.verify,name='verify'),
    path('signup',views.createacc,name='createacc'),
    path('verify',views.verify1,name='verify1'),
    path('about',views.about,name='about'),
    path('report',views.report,name='report')
]