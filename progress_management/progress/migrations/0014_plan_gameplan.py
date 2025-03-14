# Generated by Django 5.1.6 on 2025-03-12 10:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0013_rename_progress_note_subpage_progress_detail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GamePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concept', models.TextField()),
                ('mechanics', models.TextField()),
                ('art_style', models.TextField()),
                ('development_schedule', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='progress.game')),
            ],
        ),
    ]
