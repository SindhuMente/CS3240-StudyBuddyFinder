# Generated by Django 3.1.1 on 2020-10-05 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0004_auto_20200930_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='student_verified',
            field=models.BooleanField(default=False),
        ),
    ]
