# Generated by Django 5.1.2 on 2024-11-03 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_delete_githubproject_alter_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='description',
        ),
    ]
