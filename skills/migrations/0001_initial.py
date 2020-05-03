# Generated by Django 3.0.5 on 2020-05-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('coursera', 'www.coursera.org'), ('edx', 'www.edx.org')], max_length=200)),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Russian')], max_length=2)),
                ('link', models.CharField(default='', max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]
