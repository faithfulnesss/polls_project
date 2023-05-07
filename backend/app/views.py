from django.shortcuts import render

from app.models import Poll
# Create your views here.

def test_view(request):
    poll = Poll(poll_question = 'aboba')
    poll.save()
    return render(request, "index.html", {"poll" : poll})