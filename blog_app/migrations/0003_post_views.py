# Generated by Django 4.1.3 on 2022-11-11 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=12, null=True),
        ),
    ]
