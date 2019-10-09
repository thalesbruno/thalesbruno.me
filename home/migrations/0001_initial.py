# Generated by Django 2.2.5 on 2019-10-09 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
                ('repository_url', models.CharField(max_length=200)),
                ('site_url', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(0, 'Ok'), (1, 'Good'), (2, 'Nice'), (3, 'Awesome'), (4, 'Spetacular')], default=0)),
                ('technologies', models.ManyToManyField(to='home.Technology')),
            ],
        ),
    ]