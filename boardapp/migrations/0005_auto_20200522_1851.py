# Generated by Django 3.0.6 on 2020-05-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0004_auto_20200522_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
