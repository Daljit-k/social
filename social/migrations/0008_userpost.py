# Generated by Django 2.1.4 on 2019-01-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_img_table_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='userpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=140)),
                ('img', models.FileField(upload_to='')),
                ('status', models.CharField(max_length=140)),
                ('posttime', models.CharField(max_length=40)),
            ],
        ),
    ]
