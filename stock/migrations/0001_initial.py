# Generated by Django 4.1.5 on 2023-01-12 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_id", models.IntegerField()),
                ("fname", models.CharField(max_length=30)),
                ("lname", models.CharField(max_length=30)),
                ("gender", models.CharField(max_length=6)),
                ("address", models.CharField(max_length=30)),
                ("phone", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "Customer",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("productID", models.IntegerField()),
                ("productName", models.CharField(max_length=50)),
                ("buyPrice", models.IntegerField()),
                ("salePrice", models.IntegerField()),
                ("quantity", models.IntegerField()),
            ],
            options={
                "db_table": "Product",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField()),
                ("fname", models.CharField(max_length=30)),
                ("lname", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("username", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "User",
            },
        ),
        migrations.CreateModel(
            name="Sale",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("saleQuantity", models.IntegerField()),
                ("discount", models.IntegerField()),
                ("saleDate", models.DateField()),
                (
                    "customerID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stock.customer"
                    ),
                ),
                (
                    "productID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stock.product"
                    ),
                ),
            ],
            options={
                "db_table": "Sale",
            },
        ),
    ]
