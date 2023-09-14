# Generated by Django 4.2.3 on 2023-08-02 14:30

from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_location'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('bmw', 'BMW'), ('toyota', 'TOYOTA'), ('peageot', 'PEAGEOT'), ('vivo', 'VIVO'), ('mk', 'MK'), ('jeep', 'JEEP')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default='', max_length=24),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=main.utils.user_listing_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='', max_length=74),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='listing',
            name='vin',
            field=models.CharField(default='', max_length=17),
            preserve_default=False,
        ),
    ]