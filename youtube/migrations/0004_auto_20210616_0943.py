# Generated by Django 3.2.4 on 2021-06-16 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0003_auto_20210616_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='videodetail',
            name='default_thumbnail',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='videodetail',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='videodetail',
            name='medium_thumbnail',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='videodetail',
            name='publishedAt',
            field=models.CharField(blank=True, max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='videodetail',
            name='title',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
