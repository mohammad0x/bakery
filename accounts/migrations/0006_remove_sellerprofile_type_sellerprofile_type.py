# Generated by Django 4.1.4 on 2023-08-14 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_costumerprofile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sellerprofile',
            name='type',
        ),
        migrations.AddField(
            model_name='sellerprofile',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='typeof', to='accounts.bakerytype'),
        ),
    ]
