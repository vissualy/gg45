# Generated by Django 4.2.3 on 2023-08-11 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import store.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("tittle", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
            ],
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
                ("tittle", models.CharField(max_length=100)),
                ("slug", models.SlugField(max_length=100)),
                (
                    "video",
                    models.FileField(
                        null=True,
                        upload_to="video/%y",
                        validators=[store.validators.filesize],
                    ),
                ),
                ("banner", models.ImageField(null=True, upload_to="bannerimage")),
                ("description", models.TextField(blank=True)),
                ("price", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("active", "active"), ("deleted", "deleted")],
                        default="active",
                        max_length=50,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="store.category",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
