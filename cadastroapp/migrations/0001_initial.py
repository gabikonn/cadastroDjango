# Generated by Django 3.0.5 on 2020-04-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('altura', models.CharField(max_length=5)),
                ('dataNascimento', models.CharField(max_length=8)),
            ],
        ),
    ]
