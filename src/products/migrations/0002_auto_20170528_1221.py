# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='managers',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
        migrations.AddField(
            model_name='product',
            name='sale_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=23, to='sellers.SellerAccount'),
        ),
    ]
