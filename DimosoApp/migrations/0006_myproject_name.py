# Generated by Django 4.0.3 on 2022-05-02 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DimosoApp', '0005_alter_experience_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myproject',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
