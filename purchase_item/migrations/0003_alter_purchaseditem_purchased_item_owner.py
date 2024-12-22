# Generated by Django 5.1.2 on 2024-12-10 08:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("purchase_item", "0002_purchaseditem_created_at"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseditem",
            name="purchased_item_owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchased_products",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]