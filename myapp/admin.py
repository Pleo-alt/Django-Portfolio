# admin.py
from django.contrib import admin
from django.utils.html import format_html
from .models import Skill
from .models import Project

class SkillAdmin(admin.ModelAdmin):
    # Show description with formatted text (preserves line breaks and paragraphs)
    list_display = ['name', 'percentage', 'formatted_description']

    # Customize the display of the description in the admin
    def formatted_description(self, obj):
        # Replace newlines in description with <br> tags to make line breaks visible
        return format_html('<div>{}</div>', obj.description.replace('\n', '<br>'))

    formatted_description.short_description = 'Description'

admin.site.register(Skill, SkillAdmin)
admin.site.register(Project)
