# Generated by Django 4.2.3 on 2023-07-27 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_menu_item_delete_menu_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Menu_Item',
            new_name='Menu_Items',
        ),
    ]