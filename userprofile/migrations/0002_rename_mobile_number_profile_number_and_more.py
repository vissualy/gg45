# Generated by Django 4.2.3 on 2023-08-14 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("userprofile", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="mobile_number",
            new_name="number",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="profile_picture",
        ),
        migrations.AddField(
            model_name="profile",
            name="picture",
            field=models.ImageField(null=True, upload_to="media/accountimage"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="bio",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="location",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profiles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
