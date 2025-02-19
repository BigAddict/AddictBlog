# Generated by Django 5.1.6 on 2025-02-19 11:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_homepage_body_alter_standardpage_body'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footertext',
            name='locale',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale', verbose_name='locale'),
        ),
    ]
