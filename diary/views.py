from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, View
from django.http import JsonResponse, HttpRequest

import json

from .forms import CreateSubjectForm, CreateHomeworkForm
from .models import Homework, Subject


class HomeworkListView(LoginRequiredMixin, ListView):
    template_name = "diary/list_homework.html"

    def get_queryset(self):
        user = self.request.user
        homeworks = Homework.objects.filter(subject__user=user, status__in=['p', 't'])
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


class CreateHomeworkView(LoginRequiredMixin, CreateView):
    template_name = "diary/create_homework.html"
    form_class = CreateHomeworkForm
    success_url = reverse_lazy("diary:all_homework")


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UpdateHomeworkView(LoginRequiredMixin, UpdateView):
    template_name = "diary/create_homework.html"
    form_class = CreateHomeworkForm
    model = Homework
    success_url = reverse_lazy("diary:all_homework")


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


@method_decorator(csrf_exempt, name='dispatch')
class CompleteHomework(LoginRequiredMixin, View):
    def post(self, request:HttpRequest):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'error': 'Invalid JSON'}, status=400)
        homework_id = data.get('id') 
        homework_status = data.get('status') 
        if not homework_id:
            return JsonResponse({'status': 'error', 'error': 'null id'}, status=400)
        if homework_status not in [x[0] for x in Homework.STATUS]:
            return JsonResponse({'status': 'error', 'error': 'there is not such status'}, status=400)
        try:
            homework = Homework.objects.get(pk=homework_id)
            homework.status = homework_status
            homework.save()
        except Homework.DoesNotExist:
            return JsonResponse({'status': 'error', 'error': f'{homework_id} object does not exist'}, status=400)
        return JsonResponse({'status': 'success'})

