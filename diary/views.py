from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Homework, Subject


class HomeworkListView(LoginRequiredMixin, ListView):
    template_name = 'diary/list_homework.html'

    def get_queryset(self):
        user = self.request.user
        homeworks = Homework.objects.filter(subject__user=user)
        return homeworks



class SubjectsListView(LoginRequiredMixin, ListView):
    template_name = 'diary/list_subjects.html'

    def get_queryset(self):
        user = self.request.user
        subjects = Subject.objects.filter(user=user)
        return subjects
