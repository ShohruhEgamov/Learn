# Generated by Django 5.1.2 on 2024-11-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0002_rename_catigory_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('message', models.TextField()),
            ],
        ),
    ]
