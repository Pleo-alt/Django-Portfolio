# Generated by Django 5.1.2 on 2024-11-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_project_github_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='No description available'),
        ),
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='list_category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]