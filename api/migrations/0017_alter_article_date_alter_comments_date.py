# Generated by Django 4.0 on 2023-06-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_alter_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.CharField(default='today', max_length=100),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.CharField(default='today', max_length=100),
        ),
    ]
