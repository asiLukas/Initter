from .models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'image',
            'description',

        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]
