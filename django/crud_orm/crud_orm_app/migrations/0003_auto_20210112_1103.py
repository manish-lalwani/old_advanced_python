# Generated by Django 3.1.1 on 2021-01-12 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud_orm_app', '0002_auto_20210112_1102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='e_name',
            new_name='ename',
        ),
    ]
