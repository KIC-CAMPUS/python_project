# Generated by Django 4.2.7 on 2023-11-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletter_site', '0003_rename_post_like_coverletter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coverletter',
            name='like_user_set',
        ),
        migrations.AddField(
            model_name='coverletter',
            name='bookmark',
            field=models.BooleanField(default=False),
        ),
    ]
