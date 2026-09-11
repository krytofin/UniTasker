from django.contrib import admin

from .models import Homework, Subject


admin.site.register(Subject)

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject__title', 'deadline', 'status', 'created_at', ]
    list_filter = ['subject', 'deadline', 'status']
    ordering = ['-deadline']
    search_fields = ['title','description','subject__title']

