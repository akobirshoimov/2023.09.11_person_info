# Generated by Django 4.2.5 on 2023-09-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='pustuvoncha', max_length=120)),
                ('surname', models.CharField(default='palonchayev', max_length=120)),
                ('date_of_birth', models.DateField(default='2004-10-02')),
                ('gender', models.CharField(default=' ', max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
