# Generated by Django 4.2 on 2023-05-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarea', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('descripcion', models.CharField(max_length=50, verbose_name='descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='create_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='update_at')),
            ],
            options={
                'db_table': 'tipotareas',
            },
        ),
    ]