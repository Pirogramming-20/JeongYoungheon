# Generated by Django 5.0.1 on 2024-01-22 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_alter_post_is_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]