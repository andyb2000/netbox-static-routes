# Generated by Django 4.0.4 on 2022-05-28 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_static_routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staticroute',
            options={'ordering': ('device', 'vrf', 'destination_prefix', 'next_hop'), 'verbose_name_plural': 'Static Routes'},
        ),
    ]