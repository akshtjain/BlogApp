# Generated by Django 3.0.1 on 2019-12-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191225_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='main.Author'),
        ),
    ]
