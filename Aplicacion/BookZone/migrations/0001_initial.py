# Generated by Django 3.0.7 on 2020-11-06 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('editorial', models.CharField(choices=[('A', 'Ariel'), ('C', 'Caja Negra'), ('P', 'Planeta')], default='P', max_length=30)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=20)),
                ('sucursal', models.CharField(choices=[('O', 'Plaza Oeste'), ('S', 'Plaza Sur '), ('A', 'Plaza Arauco')], default='O', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Editoral',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookZone.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('editorial', models.CharField(choices=[('A', 'Ariel'), ('C', 'Caja Negra'), ('P', 'Planeta')], default='P', max_length=30)),
                ('cantidad', models.IntegerField()),
                ('vigencia', models.BooleanField(default=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookZone.Libro')),
            ],
        ),
    ]
