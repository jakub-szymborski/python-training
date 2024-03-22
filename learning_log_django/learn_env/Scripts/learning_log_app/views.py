from django.shortcuts import render

from .models import Topic 
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