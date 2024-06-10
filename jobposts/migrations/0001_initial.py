# Generated by Django 5.0.6 on 2024-06-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255, verbose_name='post author')),
                ('contact_num', models.CharField(max_length=255, verbose_name='author contact number')),
                ('title', models.CharField(max_length=255, verbose_name='post title')),
                ('description', models.CharField(max_length=255, verbose_name='post description')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='date posted')),
            ],
        ),
    ]
