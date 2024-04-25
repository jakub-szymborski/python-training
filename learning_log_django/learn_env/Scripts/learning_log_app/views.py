from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic 
from .forms import TopicForm, EntryForm
# .models means relative import, from '1 level above' current dir

# Create your views here.

def index(request):
    # Home page for learning_log_app
    return render(request, 'learning_log_app/index.html')


def topics(request):
    # show all topics
    
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_log_app/topics.html', context)


def topic(request, topic_id):
    # show a single topic 
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic, 'entries':entries}
    
    return render(request, 'learning_log_app/topic.html', context)
	
def new_topic(request):
	# Add a new topic
	if request.method != 'POST':
		#No data submitted, create blank form 
		form = TopicForm()
	else:
		# POST data submitted, process data
		form = TopicForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_log_app:topics'))
	
	context = {'form':form}
	return render(request, 'learning_log_app/new_topic.html', context)
	
def new_entry(request, topic_id):
	# add a new entry for given topic
	topic = Topic.objects.get(id=topic_id)
	
	if request.method != 'POST':
		#No data submitted, create blank form 
		form = EntryForm()
	else:
		# POST data submitted, process data
		form = EntryForm(data = request.POST)
		if form.is_valid():
			new_entry = form.save(commit = False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_log_app:topic', args=[topic_id]))
			
	context = {'topic':topic, 'form':form}
	return render(request, 'learning_log_app/new_entry.html', context)
		