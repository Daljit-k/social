# Generated by Django 2.1.4 on 2019-01-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_auto_20190111_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpost1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=140)),
                ('img', models.FileField(upload_to='')),
                ('status', models.CharField(max_length=140)),
                ('posttime', models.CharField(max_length=40)),
            ],
        ),
    ]
