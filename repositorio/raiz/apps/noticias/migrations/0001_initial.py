# Generated by Django 4.2 on 2023-07-22 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='noticias')),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=120)),
                ('creado', models.DateField(auto_now_add=True)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(blank=True, max_length=50, null=True)),
                ('imagen', models.ImageField(null=True, upload_to='noticias')),
                ('estado', models.BooleanField(default=True)),
                ('objetivo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='noticias.objetivo')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mis_comentarios', to='noticias.noticia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario_comentario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]