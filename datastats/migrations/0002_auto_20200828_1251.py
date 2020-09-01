# Generated by Django 3.1 on 2020-08-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='num_count',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Number of Values (Numeric)'),
        ),
        migrations.AddField(
            model_name='column',
            name='pct_25',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='25th Percentile'),
        ),
        migrations.AddField(
            model_name='column',
            name='pct_50',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='50th Percentile'),
        ),
        migrations.AddField(
            model_name='column',
            name='pct_75',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='75th Percentile'),
        ),
        migrations.AlterField(
            model_name='column',
            name='column_name',
            field=models.CharField(max_length=200, verbose_name='Column Name'),
        ),
        migrations.AlterField(
            model_name='column',
            name='column_type',
            field=models.CharField(max_length=200, verbose_name='Column Type'),
        ),
        migrations.AlterField(
            model_name='column',
            name='num_blank',
            field=models.IntegerField(verbose_name='Number Blank Values'),
        ),
        migrations.AlterField(
            model_name='column',
            name='num_max',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Max Value'),
        ),
        migrations.AlterField(
            model_name='column',
            name='num_mean',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Avg Value'),
        ),
        migrations.AlterField(
            model_name='column',
            name='num_min',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Min Value'),
        ),
        migrations.AlterField(
            model_name='column',
            name='num_std',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='Std Deviation'),
        ),
        migrations.AlterField(
            model_name='column',
            name='num_unique',
            field=models.IntegerField(verbose_name='Number Unique Values'),
        ),
        migrations.AlterField(
            model_name='column',
            name='variability',
            field=models.FloatField(verbose_name='Variability Index'),
        ),
    ]
