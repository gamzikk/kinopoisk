# Generated by Django 4.2.1 on 2023-06-23 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0006_alter_rating_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film'),
        ),
    ]
