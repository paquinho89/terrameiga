# Generated by Django 4.0.3 on 2024-02-06 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicleteiros', '0006_alter_km_altitude_model_journey_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='km_altitude_model',
            name='journey_day',
            field=models.IntegerField(default=30, null=True),
        ),
        migrations.AlterField(
            model_name='money_model',
            name='journey_day',
            field=models.IntegerField(default=30, null=True),
        ),
    ]