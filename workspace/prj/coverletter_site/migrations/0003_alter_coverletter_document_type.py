# Generated by Django 4.2.7 on 2023-11-20 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coverletter_site', '0002_alter_coverletter_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coverletter',
            name='document_type',
            field=models.CharField(choices=[('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D')], max_length=100),
        ),
    ]
