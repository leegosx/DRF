# Generated by Django 4.2.6 on 2023-11-02 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_user_contact_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]