# Generated by Django 3.2.5 on 2021-07-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='airport',
            field=models.ManyToManyField(to='app.airport'),
        ),
    ]
