# Generated by Django 2.1.4 on 2019-01-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_auto_20190116_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost1',
            name='user_liked',
            field=models.CharField(default=0, max_length=1400),
        ),
    ]
