# Generated by Django 4.0 on 2023-06-19 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_article_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='user_id',
            field=models.CharField(default='username', max_length=20),
        ),
    ]
