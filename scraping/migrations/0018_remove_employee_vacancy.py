# Generated by Django 3.0.5 on 2020-05-03 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0017_auto_20200503_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='vacancy',
        ),
    ]