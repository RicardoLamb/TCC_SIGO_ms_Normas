# Generated by Django 3.1.7 on 2021-03-10 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210309_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='normas',
            name='area',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='normas',
            name='codigo',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='normas',
            name='fonte',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='normas',
            name='sigla',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='normas',
            name='vigencia',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
