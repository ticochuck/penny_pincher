# Generated by Django 3.1 on 2020-08-19 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_search', '0004_searchquery_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchquery',
            name='date_from',
            field=models.DateField(help_text='First day of your availabilty'),
        ),
    ]
