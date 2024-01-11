# Generated by Django 5.0.1 on 2024-01-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='genre',
            field=models.CharField(choices=[('SF', 'Science Fiction'), ('Romance', 'Romance'), ('Action', 'Action'), ('Horror', 'Horror'), ('Crime', 'Crime'), ('Comedy', 'Comedy')], max_length=200),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='rank',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]