# Generated by Django 3.0.1 on 2019-12-25 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='title',
        ),
    ]
