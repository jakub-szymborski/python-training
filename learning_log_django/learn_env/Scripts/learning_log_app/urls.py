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
	
	# new topics:
	path('new_topic/', views.new_topic, name = 'new_topic'),
	
	# new entry:
	path('new_entry/<int:topic_id>/', views.new_entry, name ='new_entry'),
]
