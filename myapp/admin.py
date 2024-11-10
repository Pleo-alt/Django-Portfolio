from django.contrib import admin
from .models import Skill, Project, List_Category

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'percentage', 'description']
    search_fields = ['name'] 

# Inline admin configuration for List_Category model
class ListCategoryInline(admin.TabularInline):  # Use TabularInline for a table-like layout
    model = List_Category
    extra = 1  # Number of empty forms to display for adding new List_Categories

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'github_url', 'created_at']  # Ensure 'created_at' is in list_displa
    list_filter = ('created_at',) 

@admin.register(List_Category)
class List__categoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'project', 'image', 'description')
    search_fields = ('name', 'project__title')  # You can search by project title too
    list_filter = ('project',)


admin.site.site_header = "Adrian"
admin.site.site_title = "Portfolio-ADMIN"
admin.site.index_title = "Welcome to my Admin"

