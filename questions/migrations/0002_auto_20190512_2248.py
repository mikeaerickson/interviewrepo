# Generated by Django 2.2.1 on 2019-05-12 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='icon',
            field=models.CharField(max_length=250),
        ),
    ]
