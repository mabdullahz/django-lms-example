# Generated by Django 4.2.6 on 2023-10-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='LOL101', max_length=8),
            preserve_default=False,
        ),
    ]
