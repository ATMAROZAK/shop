# Generated by Django 2.1 on 2018-08-28 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Название валюты')),
                ('symbol', models.CharField(max_length=1, verbose_name='Символ')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.Currency', verbose_name='Валюта')),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='product_app.Product', verbose_name='Товар'),
        ),
    ]
