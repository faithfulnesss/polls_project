from django import forms

from django.forms import formset_factory

from django.forms import ModelForm, CharField, TextInput

# Form below represents a single choice in the poll
class ChoiceForm(forms.Form):
    # Form allows users to enter the choice text
    choice_text = forms.CharField(max_length=200,
        widget = forms.TextInput(attrs={'placeholder': 'Enter choice', 'class' : 'choice-form block w-full p-4 text-gray-900 border border-gray-300 mb-4 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
        label='',
        required=True
    )

# FormSet represents a set of choice forms
ChoiceFormSet = formset_factory(ChoiceForm, extra=0, min_num=2, max_num=10)

# Poll form represent the form of creating the poll itself
class PollForm(forms.Form):
    # Form for the poll question
    poll_question = poll_question = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your question', 'class' : 'block w-full p-4 text-gray-900 border border-gray-300 mb-6 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}),
        label='', 
    )

    # Form for the poll description
    poll_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder' : "Enter poll description",'class': "'block w-full p-4 text-gray-900 mb-4 border border-gray-300 rounded-lg bg-gray-50 sm:text-md focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'"}),
        label='', 
        required=True,
    )

