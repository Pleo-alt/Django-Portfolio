# Generated by Django 5.1.2 on 2024-11-06 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_list_category_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list_category',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='myapp.project'),
        ),
    ]
