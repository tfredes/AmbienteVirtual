# Generated by Django 3.1.2 on 2020-11-07 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planes', '0002_auto_20201107_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='review',
            field=models.TextField(default='SOME STRING', max_length=50),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
