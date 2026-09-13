from django.urls import path

from .views import DeadlineListView

app_name = 'diary'

urlpatterns = [
    path("", DeadlineListView.as_view(), name="all_deadlines")
]
