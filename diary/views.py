from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView

from .forms import CreateSubjectForm
from .models import Homework, Subject


class HomeworkListView(LoginRequiredMixin, ListView):
    template_name = "diary/list_homework.html"

    def get_queryset(self):
        user = self.request.user
        homeworks = Homework.objects.filter(subject__user=user)
        return homeworks


class SubjectsListView(LoginRequiredMixin, ListView):
    template_name = "diary/list_subjects.html"

    def get_queryset(self):
        user = self.request.user
        subjects = Subject.objects.filter(user=user)
        return subjects


class CreateSubjectView(LoginRequiredMixin, CreateView):
    template_name = "diary/create_subject.html"
    form_class = CreateSubjectForm
    success_url = reverse_lazy("diary:all_subjects")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
