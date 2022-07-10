# Generated by Django 3.2.13 on 2022-07-10 06:11

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=120, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('imagen_referencial', models.ImageField(blank=True, null=True, upload_to='autores/', verbose_name='Imagen Referencial')),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre de la Categoría')),
                ('imagen_referencial', models.ImageField(upload_to='categoria/', verbose_name='Imagen Referencial')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
            },
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=150, verbose_name='Apellidos')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('asunto', models.CharField(max_length=100, verbose_name='Asunto')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
            },
        ),
        migrations.CreateModel(
            name='RedesSociales',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('facebook', models.URLField(verbose_name='Facebook')),
                ('twitter', models.URLField(verbose_name='Twitter')),
                ('instagram', models.URLField(verbose_name='Instagram')),
            ],
            options={
                'verbose_name': 'Red Social',
                'verbose_name_plural': 'Redes Sociales',
            },
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('correo', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
        migrations.CreateModel(
            name='Web',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nosotros', models.TextField(verbose_name='Nosotros')),
                ('telefono', models.CharField(max_length=10, verbose_name='Teléfono')),
                ('email', models.EmailField(max_length=200, verbose_name='Correo Electrónico')),
                ('direccion', models.CharField(max_length=200, verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Web',
                'verbose_name_plural': 'Webs',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('fecha_eliminacion', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('titulo', models.CharField(max_length=150, unique=True, verbose_name='Título del Post')),
                ('slug', models.CharField(max_length=150, unique=True, verbose_name='Slug')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('contenido', ckeditor.fields.RichTextField()),
                ('imagen_referencial', models.ImageField(max_length=255, upload_to='imagenes/', verbose_name='Imagen Referencial')),
                ('publicado', models.BooleanField(default=False, verbose_name='Publicado / No Publicado')),
                ('fecha_publicacion', models.DateField(verbose_name='Fecha de Publicación')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoria')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
    ]
