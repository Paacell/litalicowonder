# Generated by Django 5.1.6 on 2025-03-07 06:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0008_alter_progress_created_at_alter_progress_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('plan_image', models.ImageField(blank=True, null=True, upload_to='plans/')),
                ('plan_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='progress',
            name='user',
        ),
        migrations.AddField(
            model_name='progress',
            name='question1',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='progress',
            name='question2',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='progress',
            name='question3',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='progress',
            name='question4',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='progress',
            name='question5',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='progress',
            name='question6',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='progress',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='progresses', to='progress.game'),
        ),
    ]
