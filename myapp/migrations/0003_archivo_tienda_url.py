# Generated by Django 5.2.4 on 2025-07-18 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_centrocomercial_options_alter_tienda_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('upload', models.FileField(upload_to='uploads/')),
            ],
        ),
        migrations.AddField(
            model_name='tienda',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
