# Generated by Django 5.1.3 on 2024-11-07 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserDetails',
        ),
    ]
