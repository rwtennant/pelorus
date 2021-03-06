# Generated by Django 3.1 on 2020-08-26 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('full_path', models.CharField(max_length=200)),
                ('load_date', models.DateTimeField(verbose_name='date loaded')),
            ],
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=200)),
                ('column_type', models.CharField(max_length=200)),
                ('num_blank', models.IntegerField(verbose_name='number blank')),
                ('num_unique', models.IntegerField(verbose_name='number unique values')),
                ('variability', models.FloatField()),
                ('num_max', models.FloatField(verbose_name='maximum value')),
                ('num_min', models.FloatField(verbose_name='minimum value')),
                ('num_mean', models.FloatField(verbose_name='average value')),
                ('num_std', models.FloatField(verbose_name='standard deviation')),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datastats.dataset')),
            ],
        ),
    ]
