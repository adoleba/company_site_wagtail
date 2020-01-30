# Generated by Django 2.2.8 on 2020-01-29 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('header_title', models.CharField(max_length=500)),
                ('header_description', models.TextField()),
                ('about_intro', models.CharField(max_length=200)),
                ('about_description', models.TextField()),
                ('first_card_title', models.CharField(max_length=200)),
                ('first_card_description', models.TextField()),
                ('second_card_title', models.CharField(max_length=200)),
                ('second_card_description', models.TextField()),
                ('third_card_title', models.CharField(max_length=200)),
                ('third_card_description', models.TextField()),
                ('edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
