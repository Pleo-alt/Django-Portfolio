# Generated by Django 5.1.2 on 2024-11-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_project_github_url_alter_list_category_github_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='github_url',
        ),
    ]
