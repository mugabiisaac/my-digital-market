# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import products.models
import django.core.files.storage
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyProducts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media', models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/mugabiisaac/Desktop/dm2/src/static_cdn/protected'), null=True, upload_to=products.models.download_media_location, blank=True)),
                ('title', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True, blank=True)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(default=9.99, null=True, max_digits=100, decimal_places=2, blank=True)),
                ('sale_price', models.DecimalField(default=6.99, null=True, max_digits=100, decimal_places=2, blank=True)),
                ('managers', models.ManyToManyField(related_name='managers_products', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(default=b'hd', max_length=20, choices=[(b'hd', b'HD'), (b'sd', b'SD'), (b'micro', b'MICRO')])),
                ('height', models.CharField(max_length=20, null=True, blank=True)),
                ('width', models.CharField(max_length=20, null=True, blank=True)),
                ('media', models.ImageField(height_field=b'height', width_field=b'width', null=True, upload_to=products.models.Thumbnail_location, blank=True)),
                ('product', models.ForeignKey(to='products.Product')),
            ],
        ),
        migrations.AddField(
            model_name='myproducts',
            name='products',
            field=models.ManyToManyField(to='products.Product', blank=True),
        ),
        migrations.AddField(
            model_name='myproducts',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
