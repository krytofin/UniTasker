from django import forms


from .models import Homework, Subject


class CreateSubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'professor']



class CreateHomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['subject', 'title', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateInput(
                format="%Y-%m-%d",
                attrs={"type": "date"}
            )
        }


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        subjects = Subject.objects.filter(user=user)
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = subjects
