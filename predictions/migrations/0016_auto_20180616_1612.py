# Generated by Django 2.0 on 2018-06-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0015_completematches_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='QualityForm_Player1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictions',
            name='QualityForm_Player2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictions',
            name='WinRateOpponentquality_Player1',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='predictions',
            name='WinRateOpponentquality_Player2',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
