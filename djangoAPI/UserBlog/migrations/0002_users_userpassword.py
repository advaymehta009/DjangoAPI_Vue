# Generated by Django 4.0.6 on 2022-07-17 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('UserBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='UserPassword',
            field=models.CharField(default=django.utils.timezone.now, max_length=8),
            preserve_default=False,
        ),
    ]