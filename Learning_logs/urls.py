"""Defines URL patterns for Learning_logs."""
from django.urls import path
from . import views

app_name = 'Learning_logs'
urlpatterns = [
    # home page.
    path('', views.index, name='index'),
    # page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single point.
    path('topics/<int:topic_id>/', views.topic, name='topic')
]
