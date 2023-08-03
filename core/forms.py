from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('todo',)
        widgets = {
            'todo': forms.TextInput(attrs={
                'class': 'text-blue-500 mt-4 w-[20rem] rounded-xl p-2',
                'placeholder': 'Type something...'
            })
        }

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('todo',)
        widgets = {
            'todo': forms.TextInput(attrs={
                'class': 'text-blue-500 mt-4 w-[20rem] rounded-xl p-2',
                'placeholder': 'Edit...'
            })
        }