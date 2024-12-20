# Generated by Django 5.1.2 on 2024-12-10 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_education_project_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='About/'),
        ),
        migrations.AlterField(
            model_name='education',
            name='image',
            field=models.ImageField(upload_to='Education/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='Project/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='skill',
            name='image',
            field=models.ImageField(upload_to='Skill/'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='level',
            field=models.PositiveIntegerField(),
        ),
    ]
