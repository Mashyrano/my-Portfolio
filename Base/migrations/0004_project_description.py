# Generated by Django 5.1.2 on 2024-11-28 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0003_admin_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
