# Generated by Django 4.1.7 on 2023-02-28 10:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 16, 23, 36, 161477)),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='app.post')),
            ],
        ),
    ]