# Generated by Django 5.1.4 on 2024-12-27 13:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_app', '0001_initial'),
        ('teacher_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='quizattempt',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='teacher_app.quiz'),
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quiz_attempts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='enrolled_classes',
            field=models.ManyToManyField(related_name='students_in_class', to='teacher_app.class'),
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
