from django import forms
from .models import Todo
class Taskform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'