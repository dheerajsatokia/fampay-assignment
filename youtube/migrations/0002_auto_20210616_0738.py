# Generated by Django 3.2.4 on 2021-06-16 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoDetail',
            fields=[
                ('high_thumbnail', models.CharField(blank=True, max_length=250, null=True)),
                ('title', models.CharField(max_length=250, null=True, blank=True)),
                ('publishedAt', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('default_thumbnail', models.CharField(max_length=250, null=True, blank=True)),
                ('medium_thumbnail', models.CharField(max_length=250, null=True, blank=True))
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
