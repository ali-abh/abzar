# Generated by Django 5.0.7 on 2024-07-24 17:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abzar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=100, verbose_name='نام محصول')),
                ('remained', models.CharField(blank=True, max_length=3, null=True, verbose_name='تعداد باقی مانده ')),
                ('price', models.DecimalField(decimal_places=3, max_digits=7, verbose_name=' قیمت')),
                ('aboutproduct', models.TextField(blank=True, max_length=350, null=True, verbose_name='درباره ابزار ')),
                ('brandname', models.CharField(blank=True, max_length=40, null=True, verbose_name='نام برند ')),
                ('manufacturing_country', models.CharField(max_length=20, verbose_name=' کشور سازنده ')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=350, verbose_name=' آدرس دقیق ')),
                ('housenumber', models.IntegerField(verbose_name=' پلاک  ')),
                ('postalcode', models.IntegerField(verbose_name='  کدپستی ')),
                ('paymentmethod', models.CharField(max_length=1000, verbose_name=' روش پرداخت')),
                ('receivername', models.CharField(max_length=25, verbose_name='نام نحویل گیرنده ')),
            ],
            options={
                'verbose_name': 'فروش',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام  ')),
                ('lastname', models.CharField(max_length=50, null=True, verbose_name='نام خانوادگی ')),
                ('userphonenumber', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Enter a valid phone number', regex='\\d{10,14}')], verbose_name='شماره تلفن  ')),
                ('gmail', models.EmailField(max_length=254, unique=True, verbose_name=' ایمیل ')),
                ('password', models.CharField(max_length=50, verbose_name='رمز  ')),
                ('address', models.TextField(max_length=100, verbose_name=' ادرس محل سکونت ')),
                ('age', models.PositiveIntegerField(blank=True, null=True, verbose_name=' سن ')),
            ],
        ),
    ]
