# Generated by Django 3.0.2 on 2020-01-07 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20200107_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='transaction_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
