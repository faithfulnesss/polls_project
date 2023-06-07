from django.db import models
from django.contrib.auth.models import User

# Model representation of the Poll
class Poll(models.Model):
    poll_question = models.CharField(max_length=255)  # The question of the poll
    publication_date = models.DateTimeField(auto_now_add=True)  # The date and time when the poll was published
    poll_description = models.TextField(blank=True)  # The description of the poll (optional)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the poll

    def __str__(self):
        return self.poll_question

    def get_choices(self):
        return self.choice_set.all()  # Returns all the choices related to the poll

    def get_vote_counts(self):
        vote_counts = {}  # Dictionary to store the vote count for each choice
        total_votes = 0  # Total number of votes for the poll
        choices = self.choice_set.all()  # Get all the choices related to the poll

        for choice in choices:
            vote_count = choice.vote_set.count()  # Get the vote count for the choice
            vote_counts[choice.choice_text] = vote_count  # Store the vote count in the dictionary
            total_votes += vote_count  # Increment the total vote count

        return total_votes, vote_counts

# Model that represents the choice (variant of vote) of the poll
class Choice(models.Model): 
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)  # The poll to which the choice belongs
    choice_text = models.CharField(max_length=200)  # The text of the choice

    def __str__(self):
        return self.choice_text

# Model that represents a vote chosen by a user for a choice in a poll
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who chose the vote
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)  # The poll for which the vote was chosen
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)  # The choice for which the vote was chosen
