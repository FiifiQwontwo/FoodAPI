# Generated by Django 4.2.2 on 2023-06-27 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FDS', '0003_order_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='FDS.menuitem'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
