# Generated by Django 5.0.6 on 2024-06-12 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('juego', models.CharField(max_length=20)),
                ('año_salida', models.CharField(max_length=20)),
            ],
        ),
    ]
