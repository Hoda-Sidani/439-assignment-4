# Generated by Django 5.1.3 on 2024-11-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp3', '0004_contact_email_contact_experience_contact_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]