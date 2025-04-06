from django.contrib import admin
from .models import Student, RecruiterSearch, Analytics

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'skills', 'created_at', 'updated_at')
    search_fields = ('user__username', 'user__email', 'skills')
    list_filter = ('created_at', 'updated_at')

@admin.register(RecruiterSearch)
class RecruiterSearchAdmin(admin.ModelAdmin):
    list_display = ('search_query', 'searched_at')
    list_filter = ('searched_at',)
    search_fields = ('search_query',)

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'search_count')
    list_filter = ('search_count',)
    search_fields = ('skill_name',)
