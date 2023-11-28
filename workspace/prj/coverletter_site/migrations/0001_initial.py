# Generated by Django 4.2.7 on 2023-11-28 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoverLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.IntegerField(choices=[(1, '지원 동기'), (2, '입사 포부'), (3, '성격'), (4, '팀워크'), (5, '기타')])),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('rate', models.DecimalField(decimal_places=3, max_digits=5, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('bookmark', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CoverLetterPlagiarism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_sentence', models.TextField()),
                ('most_similar', models.TextField()),
                ('result', models.DecimalField(decimal_places=3, max_digits=6, null=True)),
                ('sequence_number', models.IntegerField()),
                ('coverletter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coverletter_site.coverletter')),
            ],
        ),
    ]
