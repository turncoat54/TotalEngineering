# Generated by Django 2.0.6 on 2019-03-24 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wx_search', '0004_student_avator'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pinyin',
            field=models.CharField(default='test', max_length=255),
        ),
    ]