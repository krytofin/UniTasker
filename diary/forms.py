from django import forms


from .models import Homework, Subject


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'professor']
