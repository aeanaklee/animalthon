# Generated by Django 3.1.3 on 2021-08-12 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='newCare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_kind', models.CharField(choices=[('DOG', 'dog'), ('CAT', 'cat'), ('ETC', 'other')], max_length=3)),
                ('area', models.CharField(choices=[('SE', '서울특별시'), ('GG', '경기도'), ('CH', '충청도'), ('GS', '경상도'), ('JL', '전라도'), ('GW', '강원도'), ('JJ', '제주도')], max_length=2)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('kind', models.CharField(max_length=50)),
                ('caution', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='newJogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_kind', models.CharField(choices=[('DOG', 'dog'), ('CAT', 'cat'), ('ETC', 'other')], max_length=3)),
                ('area', models.CharField(choices=[('SE', '서울특별시'), ('GG', '경기도'), ('CH', '충청도'), ('GS', '경상도'), ('JL', '전라도'), ('GW', '강원도'), ('JJ', '제주도')], max_length=2)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('kind', models.CharField(max_length=50)),
                ('caution', models.TextField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
