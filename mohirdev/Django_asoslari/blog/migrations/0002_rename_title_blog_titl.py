# Generated by Django 5.1 on 2024-08-24 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='titl',
        ),
    ]
