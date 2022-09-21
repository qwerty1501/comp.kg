# Generated by Django 4.1.1 on 2022-09-19 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
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
                (
                    "image",
                    models.ImageField(
                        upload_to="images/dop_images", verbose_name="Фотография"
                    ),
                ),
            ],
            options={
                "verbose_name": "Фотография",
                "verbose_name_plural": "Доп_Фотографии",
            },
        ),
        migrations.CreateModel(
            name="ProductImage",
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
                (
                    "images",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.image",
                        verbose_name="Фотография",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                        verbose_name="Продукт",
                    ),
                ),
            ],
        ),
    ]