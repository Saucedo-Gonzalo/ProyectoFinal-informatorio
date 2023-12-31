# Generated by Django 4.2.3 on 2023-07-27 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('noticias', '0002_alter_noticia_estado_alter_objetivo_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='estado',
            field=models.CharField(blank=True, db_comment='habilitado, deshabilitado', default='habilitado', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='estado',
            field=models.CharField(blank=True, db_comment='habilitado, deshabilitado', default='habilitado', max_length=20, null=True),
        ),
    ]
