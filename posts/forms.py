from django import forms
from posts.models import Posts
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['post', 'image']
        widgets = {
            'post': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'What’s on your mind?'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(UserCreationForm):
    email  = forms.EmailField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
