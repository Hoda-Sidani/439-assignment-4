# Generated by Django 5.1.3 on 2024-11-27 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0002_contact_delete_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='tel_number',
            new_name='contact_info',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='profession',
        ),
        migrations.AddField(
            model_name='contact',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=300, max_digits=10),
        ),
        migrations.AddField(
            model_name='contact',
            name='recommendation',
            field=models.PositiveIntegerField(default=6),
        ),
        migrations.AddField(
            model_name='contact',
            name='speciality',
            field=models.CharField(default='Cardiothoracic Surgeon', max_length=250),
        ),
    ]