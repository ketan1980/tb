# Generated by Django 2.0 on 2018-08-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0017_auto_20180616_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='Momentum_Player1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictions',
            name='Momentum_Player2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictions',
            name='Surface',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='QualityForm_Player1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='QualityForm_Player2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='WinRateOpponentquality_Player1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='WinRateOpponentquality_Player2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
