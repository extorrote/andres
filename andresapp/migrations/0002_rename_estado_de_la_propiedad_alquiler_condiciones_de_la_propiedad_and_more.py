# Generated by Django 5.0.7 on 2024-10-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andresapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alquiler',
            old_name='estado_de_la_propiedad',
            new_name='condiciones_de_la_propiedad',
        ),
        migrations.RenameField(
            model_name='venta',
            old_name='estado',
            new_name='condiciones_de_la_propiedad',
        ),
        migrations.RemoveField(
            model_name='terreno',
            name='privada_o_con_escrituras',
        ),
        migrations.AlterField(
            model_name='preconstruccion',
            name='anticipo',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]