# Generated by Django 3.0.5 on 2020-04-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200422_1133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',), 'verbose_name': 'Articolo', 'verbose_name_plural': 'Articoli'},
        ),
        migrations.AddField(
            model_name='post',
            name='data_pubblicazione',
            field=models.DateField(blank=True, null=True),
        ),
    ]
