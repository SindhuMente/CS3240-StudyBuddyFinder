# Generated by Django 3.1.1 on 2020-09-30 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studybuddyfinder', '0002_auto_20200930_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='discord_id',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zoom_id',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
