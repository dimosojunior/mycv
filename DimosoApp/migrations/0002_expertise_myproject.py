# Generated by Django 4.0.3 on 2022-05-02 04:04

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=200, null=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('post_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
