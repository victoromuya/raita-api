# Generated by Django 4.0 on 2023-06-19 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_article_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user_id',
        ),
    ]
