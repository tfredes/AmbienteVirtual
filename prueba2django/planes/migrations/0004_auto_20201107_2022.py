# Generated by Django 3.1.2 on 2020-11-07 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0003_auto_20201107_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='review',
            field=models.TextField(default='SOME STRING', max_length=100),
        ),
    ]
