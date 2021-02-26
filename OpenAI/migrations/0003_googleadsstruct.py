# Generated by Django 3.1.7 on 2021-02-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpenAI', '0002_questionanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleAdsStruct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('audience', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('keywords', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
