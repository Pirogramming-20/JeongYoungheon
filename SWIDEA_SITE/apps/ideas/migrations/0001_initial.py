# Generated by Django 5.0.1 on 2024-01-17 23:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devtools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='제목')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='이미지')),
                ('content', models.TextField(max_length=200, verbose_name='아이디어 설명')),
                ('interest', models.IntegerField(default=0, verbose_name='아이디어 관심도')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devtools.devtool', verbose_name='예상 개발 툴')),
            ],
        ),
    ]