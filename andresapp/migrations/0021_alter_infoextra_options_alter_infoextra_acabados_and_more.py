# Generated by Django 5.0.7 on 2024-11-05 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andresapp', '0020_remove_infoextra_direccion_del_inmueble'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infoextra',
            options={'verbose_name': 'Levantamiento', 'verbose_name_plural': 'Levantamientos'},
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='acabados',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='antiguedad_de_la_construccion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='calle',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='ciudad',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='colonia',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='cp',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='distribucion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='equipamiento_general',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='estado',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='estado_de_conservacion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='exterior',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='fachada',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='grietas',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='humedades',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='infraestructura_y_urbanizacion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='instalaciones_electricas',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='instalaciones_especiales',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='materiales_de_construccion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='nombre_del_propietario',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='pintura',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='plomeria',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='superficie_de_construccion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='superficie_de_terreno',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='undimientos',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='infoextra',
            name='vidrieria',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
