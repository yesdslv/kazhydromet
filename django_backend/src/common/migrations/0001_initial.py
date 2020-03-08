from django.conf import settings
from django.db import migrations
from django.contrib.postgres.operations import CreateExtension


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        CreateExtension('postgis'),
    ]
