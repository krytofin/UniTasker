from django import forms


from .models import Homework, Subject


class CreateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'professor']
