# Generated by Django 4.1.7 on 2023-05-15 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titlte',
            new_name='title',
        ),
    ]
