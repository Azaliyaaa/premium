# Generated by Django 3.1.4 on 2020-12-27 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('premium', '0003_notebook_smartphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('season', models.CharField(max_length=255, verbose_name='Сезон')),
                ('material', models.CharField(max_length=255, verbose_name='Материал')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premium.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trench',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Общая цена')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('season', models.CharField(max_length=255, verbose_name='Сезон')),
                ('material', models.CharField(max_length=255, verbose_name='Материал')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premium.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='smartphone',
            name='category',
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='premium.customer', verbose_name='Покупатель'),
        ),
        migrations.DeleteModel(
            name='NoteBook',
        ),
        migrations.DeleteModel(
            name='Smartphone',
        ),
    ]
