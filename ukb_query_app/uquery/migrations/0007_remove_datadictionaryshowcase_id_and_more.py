# Generated by Django 4.0.3 on 2022-04-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uquery', '0006_remove_datadictionaryshowcase_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datadictionaryshowcase',
            name='id',
        ),
        migrations.AlterField(
            model_name='datadictionaryshowcase',
            name='FieldID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
