from django.forms import ModelForm
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from  django.contrib.auth.models import User
from django import  forms


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']