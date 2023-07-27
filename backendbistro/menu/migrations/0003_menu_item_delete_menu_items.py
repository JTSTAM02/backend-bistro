# Generated by Django 4.2.3 on 2023-07-27 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_rename_spicy_level_menu_items_spicy_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('spicy_level', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.category')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.cuisine')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.location')),
            ],
        ),
        migrations.DeleteModel(
            name='Menu_Items',
        ),
    ]
