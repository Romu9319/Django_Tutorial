# Generated by Django 4.2.7 on 2023-11-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('imagen', models.CharField(max_length=250)),
            ],
        ),
    ]
