# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 12:08
from __future__ import unicode_literals

from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("product", "0012_auto_20160218_0812")]

    operations = [HStoreExtension()]
