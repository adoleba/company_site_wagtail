# Generated by Django 2.2.8 on 2020-02-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('home', '0002_auto_20200204_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='first_card_button_url',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
    ]
