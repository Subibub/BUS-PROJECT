from django import forms
from .models import Comment,Feed

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = '__all__'