# Generated by Django 5.0.7 on 2024-11-13 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('andresapp', '0026_perfilamiento_cargo_en_la_agencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fichatecnica',
            name='cargo_en_la_agencia',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='ciudad_y_estado',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='email_agente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='logo_agente',
            field=models.ImageField(blank=True, null=True, upload_to='andresapp/agentes'),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='nombre_agente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='pagina_web',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='fichatecnica',
            name='telefono_agente',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]