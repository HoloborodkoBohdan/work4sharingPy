# Generated by Django 3.0.5 on 2020-05-03 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0019_remove_employee_position'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skill',
        ),
    ]