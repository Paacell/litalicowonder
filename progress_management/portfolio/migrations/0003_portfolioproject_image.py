# Generated by Django 5.1.6 on 2025-02-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolioproject_delete_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioproject',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='portfolio_images/'),
        ),
    ]
