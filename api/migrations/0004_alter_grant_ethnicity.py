# Generated by Django 4.1.7 on 2023-04-04 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_grant_users_user_grants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grant',
            name='ethnicity',
            field=models.TextField(),
        ),
    ]
