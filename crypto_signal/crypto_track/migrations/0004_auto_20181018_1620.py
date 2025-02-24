# Generated by Django 2.1.2 on 2018-10-18 14:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('crypto_track', '0003_auto_20181018_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyTrends',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('is_partial', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='cryptocandle',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 14, 20, 21, 697926, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cryptocandlehistory',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 14, 20, 21, 698912, tzinfo=utc)),
        ),
    ]
