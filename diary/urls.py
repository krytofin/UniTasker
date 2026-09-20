from django.urls import path

from .views import CreateSubjectView, HomeworkListView, SubjectsListView, CreateHomeworkView, CompleteHomework, UpdateHomeworkView, ArchiveSubject, ArchiveSubjectListView

app_name = 'diary'

urlpatterns = [
    path("", HomeworkListView.as_view(), name="all_homework"),
    path("subjects/", SubjectsListView.as_view(), name="all_subjects"),
    path('add/subject/', CreateSubjectView.as_view(), name='create_subject'),
    path('add/homework/', CreateHomeworkView.as_view(), name='create_homework'),
    path('update/homework/<int:pk>', UpdateHomeworkView.as_view(), name='update_homework'),
    path('homework/update/', CompleteHomework.as_view(), name='update_homework'),
    path('subject/archive/', ArchiveSubject.as_view(), name='archive_subject'),
    path('archive/view/', ArchiveSubjectListView.as_view(), name='archive_subject_view'),
]
