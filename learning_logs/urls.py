"""Defines URL patterns for learning_logs."""

from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path(r'', views.index, name='index'),

    # Show all topics
    path(r'topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path(r'topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding a new topic
    path(r'new_topic/', views.new_topic, name='new_topic'),

    # Page for adding a new entry
    path(r'new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Page for editing an entry
    path(r'edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]