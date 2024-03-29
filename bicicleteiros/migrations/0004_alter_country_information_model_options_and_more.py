# Generated by Django 4.0.3 on 2024-01-30 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bicicleteiros', '0003_alter_km_altitude_model_journey_day_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country_information_model',
            options={'ordering': ['-country_number']},
        ),
        migrations.AlterField(
            model_name='km_altitude_model',
            name='journey_day',
            field=models.IntegerField(default=22, null=True),
        ),
        migrations.AlterField(
            model_name='km_altitude_model',
            name='week',
            field=models.IntegerField(default=4, null=True),
        ),
        migrations.AlterField(
            model_name='money_model',
            name='journey_day',
            field=models.IntegerField(default=22, null=True),
        ),
        migrations.AlterField(
            model_name='money_model',
            name='week',
            field=models.IntegerField(default=4, null=True),
        ),
        migrations.AlterField(
            model_name='videos_model',
            name='week',
            field=models.IntegerField(default=4, null=True),
        ),
    ]
