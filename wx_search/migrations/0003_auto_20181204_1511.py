# Generated by Django 2.0.6 on 2018-12-04 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wx_search', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]