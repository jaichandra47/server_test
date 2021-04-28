# Generated by Django 3.0.8 on 2020-07-18 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpiderVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_or_out', models.BooleanField(default=False)),
                ('rptg_prd_year_mnth_nbr', models.TextField()),
                ('prod_vrtn_id', models.TextField()),
                ('bnft_pkg_id', models.TextField()),
                ('start_dt', models.DateTimeField()),
                ('cst_shr_column_name', models.TextField()),
                ('existing_value', models.IntegerField()),
                ('new_value', models.IntegerField()),
                ('contvar', models.TextField()),
                ('contvar_desc', models.TextField()),
                ('prov_arng', models.TextField()),
                ('bnft_lmt_desc', models.TextField()),
                ('edm_load_log_key', models.TextField()),
                ('load_dtm', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WpdVariables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_or_out', models.BooleanField(default=False)),
                ('rptg_prd_year_mnth_nbr', models.TextField()),
                ('prod_vrtn_id', models.TextField()),
                ('bnft_pkg_id', models.TextField()),
                ('start_dt', models.DateTimeField()),
                ('cst_shr_column_name', models.TextField()),
                ('existing_value', models.IntegerField()),
                ('new_value', models.IntegerField()),
                ('contvar', models.TextField()),
                ('contvar_desc', models.TextField()),
                ('prov_arng', models.TextField()),
                ('bnft_lmt_desc', models.TextField()),
                ('edm_load_log_key', models.TextField()),
                ('load_dtm', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
