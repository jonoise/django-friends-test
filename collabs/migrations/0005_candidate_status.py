# Generated by Django 3.1.7 on 2021-03-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabs', '0004_auto_20210314_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='status',
            field=models.CharField(default=('pending', 'Pending'), max_length=20, verbose_name='status'),
        ),
    ]