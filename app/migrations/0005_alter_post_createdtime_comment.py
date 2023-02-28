# Generated by Django 4.1.7 on 2023-02-28 11:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_alter_post_createdtime_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 28, 16, 30, 49, 801543)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postBy', to='app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
