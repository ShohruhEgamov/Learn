# Generated by Django 5.1 on 2024-08-24 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_titl_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='titles',
        ),
    ]
