# Generated by Django 4.1.2 on 2023-06-17 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_article_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user_id',
        ),
    ]
