from django.db import models

# Create your models here.
class Poll(models.Model):
    poll_question = models.CharField(max_length=255)
    publication_date = models.DateTimeField(auto_now_add=True)
    poll_description = models.TextField(blank=True) 

    def __str__(self):
        return self.poll_question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey()
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
