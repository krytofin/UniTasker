from django.urls import path, reverse_lazy
from django.contrib.auth import views


app_name = 'accounts'

urlpatterns = [
        path('login/', views.LoginView.as_view(template_name='accounts/login.html', success_url=reverse_lazy('diary:all_homework')), name='login'),
]
