# Generated by Django 4.2.2 on 2023-06-24 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FDS', '0002_remove_order_total_amount_alter_menuitem_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=2.0, max_digits=10),
        ),
    ]
