# Generated by Django 5.0.7 on 2024-11-10 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andresapp', '0021_alter_infoextra_options_alter_infoextra_acabados_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alquiler',
            name='balcon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='cocina',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='comedor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='alquiler',
            name='jardin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='preconstruccion',
            name='balcon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='preconstruccion',
            name='comedor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='preconstruccion',
            name='jardin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='preconstruccion',
            name='politicas_de_venta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='terreno',
            name='metros_cuadrados',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='balcon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='cocina',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='comedor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='jardin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]