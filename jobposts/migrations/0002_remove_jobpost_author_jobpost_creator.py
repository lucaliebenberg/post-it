# Generated by Django 5.0.6 on 2024-06-17 07:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('jobposts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='author',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='creator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
            preserve_default=False,
        ),
    ]
