# Generated by Django 5.1.3 on 2024-11-28 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0003_rename_tel_number_contact_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='experience',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(default='Female', max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='hospital',
            field=models.CharField(default='CMC', max_length=200),
        ),
    ]