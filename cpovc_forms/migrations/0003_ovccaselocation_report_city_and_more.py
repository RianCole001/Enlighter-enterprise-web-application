# Generated by Django 4.0.4 on 2022-11-20 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cpovc_main', '0002_initial'),
        ('cpovc_forms', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_country_code',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='ovccaselocation',
            name='report_sublocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_location', to='cpovc_main.setuplocation'),
        ),
        migrations.AlterField(
            model_name='ovccaselocation',
            name='case',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cpovc_forms.ovccaserecord'),
        ),
        migrations.AlterField(
            model_name='ovccaselocation',
            name='report_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location', to='cpovc_main.setuplocation'),
        ),
    ]