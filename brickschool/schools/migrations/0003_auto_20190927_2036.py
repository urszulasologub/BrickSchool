# Generated by Django 2.2.5 on 2019-09-27 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_badges'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='school_class',
            new_name='SchoolClass',
        ),
    ]