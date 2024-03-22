from django.db import models

# Create your models here.
class Topic(models.Model):
    # a topic of log 
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        # return str of the model 
        return self.text
    
class Entry(models.Model):
    # an entry about a topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        # return txt of the model
        if len(self.text) > 50:
            return self.text[:50] + "..." 
        else: 
            return self.text
    