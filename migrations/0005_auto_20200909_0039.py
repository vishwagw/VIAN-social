
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20200909_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name = 'Followers',
            field= models.ForeignKey(blank=True, null=True, on_delete=django.db.models.CASCADE, related_name='user follwing', to = settings.AUTH_USER_MODEL),
        ),
    ]
