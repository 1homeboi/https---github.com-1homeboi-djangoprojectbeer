# Generated by Django 4.2.4 on 2023-08-14 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='adress',
            new_name='address',
        ),
    ]