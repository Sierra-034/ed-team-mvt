# Generated by Django 4.2.4 on 2023-09-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagen', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=100)),
            ],
        ),
    ]