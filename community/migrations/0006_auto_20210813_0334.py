# Generated by Django 3.1.3 on 2021-08-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_auto_20210813_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcare',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='careimages/'),
        ),
        migrations.AlterField(
            model_name='newjogging',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='jogimages/'),
        ),
    ]
