# Generated by Django 5.0 on 2024-04-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_restaurant_max_nooffourtables_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='Time',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='NoOfFourTables',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='NoOfSixTables',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='NoOfTwoTables',
        ),
        migrations.AddField(
            model_name='booking',
            name='EndTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='StartTime',
            field=models.DateTimeField(null=True),
        ),
    ]
