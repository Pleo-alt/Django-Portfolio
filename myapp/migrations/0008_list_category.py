# Generated by Django 5.1.2 on 2024-11-06 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_project_github_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='List_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='categories/')),
                ('description', models.TextField()),
                ('github_url', models.URLField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='myapp.project')),
            ],
        ),
    ]
