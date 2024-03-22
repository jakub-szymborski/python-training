"""
Defines URL patterns for learning_log_app
"""
from django.urls import path
from . import views

app_name = 'learning_log_app'
urlpatterns = [
	# home page
	path('',views.index, name ='index'),
	
	# show all topics
	path('topics/', views.topics, name='topics'),
	# particular topics:
	path('topics/<int:topic_id>/', views.topic, name='topic'),
]
