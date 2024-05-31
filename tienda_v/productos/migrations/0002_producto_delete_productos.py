# Generated by Django 4.2.6 on 2023-11-09 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_producto', models.CharField(blank=True, max_length=100, null=True)),
                ('precio_producto', models.FloatField(default=0)),
                ('escala_producto', models.CharField(blank=True, max_length=10, null=True)),
                ('tamaño', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen_Producto', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
    ]
