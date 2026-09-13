from django.views.generic import ListView

from .models import Homework


class DeadlineListView(ListView):
    model = Homework
    template_name = 'diary/list_homework.html'
