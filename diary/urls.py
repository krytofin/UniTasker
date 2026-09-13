from django.urls import path

from .views import HomeworkListView, SubjectsListView

app_name = 'diary'

urlpatterns = [
    path("", HomeworkListView.as_view(), name="all_homework"),
    path("subjects/", SubjectsListView.as_view(), name="all_subjects"),
]
