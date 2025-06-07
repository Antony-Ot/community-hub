from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('emergency_alerts/', views.emergency_alerts, name='emergency_alerts'),
    path('skill_building/', views.skill_building, name='skill_building'),
    path('cultural_preservation/', views.cultural_preservation, name='cultural_preservation'),
    path('discussion_forums/', views.discussion_forums, name='discussion_forums'),
    path('resource_directory/', views.resource_directory, name='resource_directory'),
    path('payment/', views.payment, name='payment'),
    path('payment/confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('report/', views.report, name='report'),
]
