# Generated by Django 2.2 on 2021-06-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hunter_app', '0003_remove_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_post',
            name='city',
            field=models.CharField(default='text', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_post',
            name='state',
            field=models.CharField(default='city', max_length=2),
            preserve_default=False,
        ),
    ]
