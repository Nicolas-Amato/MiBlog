# Generated by Django 4.1.4 on 2022-12-12 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('deporte', models.CharField(max_length=40)),
                ('DNI', models.IntegerField()),
            ],
        ),
    ]