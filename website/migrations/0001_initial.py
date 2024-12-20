# Generated by Django 5.1.2 on 2024-11-01 15:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('logo', models.ImageField(upload_to='logo/')),
                ('total_subscription', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'verbose_name': 'Channel',
                'verbose_name_plural': 'Channel',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('thumbnail', models.ImageField(upload_to='videoThumbnail/')),
                ('video', models.URLField(blank=True, null=True)),
                ('like', models.IntegerField(default=0)),
                ('dislike', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('channel', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='website.channel')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'video',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('created_on', models.DateField(default=datetime.datetime.now, editable=False)),
                ('video', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, to='website.videos')),
            ],
            options={
                'verbose_name': 'Comments',
                'verbose_name_plural': 'Comments',
            },
        ),
    ]
