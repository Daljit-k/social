# Generated by Django 2.1.4 on 2018-12-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20181228_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('re_password', models.CharField(max_length=40)),
            ],
        ),
    ]
