from django import forms
from posts.models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post', 'image']
        widgets = {
            'post': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'What’s on your mind?'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
