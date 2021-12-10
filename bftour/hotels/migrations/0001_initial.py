import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hotel",
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
                ("title", models.CharField(max_length=50)),
                ("contents", models.TextField()),
                ("address", models.CharField(max_length=255)),
                ("facility", models.CharField(default="", max_length=50)),
                ("start_dt", models.DateTimeField(verbose_name="date published")),
                ("end_dt", models.DateTimeField(verbose_name="date published")),
                (
                    "pro_price",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("reg_dt", models.DateTimeField(auto_now_add=True)),
                ("reg_id", models.CharField(default="admin", max_length=50)),
                (
                    "thumb_file",
                    models.ImageField(
                        blank=True, null=True, upload_to="hotel_thumb/%Y/%m/%d"
                    ),
                ),
                ("del_yn", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("postname", models.CharField(max_length=50)),
                ("contents", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomType",
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
                ("name", models.CharField(default="", max_length=60)),
            ],
        ),
    ]
