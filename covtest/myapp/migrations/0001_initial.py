# Generated by Django 3.0.5 on 2021-04-03 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_time_start', models.DateField()),
                ('working_time_end', models.DateField()),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('override_status', models.BooleanField()),
                ('order_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('glovo_id', models.IntegerField()),
                ('glovo_code', models.CharField(max_length=255)),
                ('glovo_description', models.TextField()),
                ('glovo_scheduleTime', models.CharField(max_length=255)),
                ('glovo_state', models.CharField(max_length=255)),
                ('glovo_reference', models.TextField()),
            ],
        ),
    ]