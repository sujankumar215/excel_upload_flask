# Generated by Django 4.1.7 on 2023-03-10 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exp', models.IntegerField()),
                ('subject', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='classname',
            field=models.IntegerField(),
        ),
    ]