# Generated by Django 5.0.7 on 2024-10-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andresapp', '0004_remove_terreno_estado_remove_terreno_tipo_de_terreno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='imagen10',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen11',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen12',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen13',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen14',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen15',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen16',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
        migrations.AddField(
            model_name='venta',
            name='imagen9',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp'),
        ),
    ]
