# Generated by Django 4.2.9 on 2024-01-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('data1', models.CharField(max_length=50)),
                ('data2', models.CharField(max_length=50)),
            ],
        ),
    ]