# Generated by Django 4.2.2 on 2023-06-27 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FDS', '0004_alter_order_food_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_orders', to='FDS.menuitem'),
        ),
    ]