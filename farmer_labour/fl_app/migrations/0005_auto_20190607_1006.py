# Generated by Django 2.0 on 2019-06-07 10:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fl_app', '0004_auto_20190607_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='frtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typework', models.CharField(max_length=200)),
                ('startdate', models.DateField(default=datetime.date(2019, 6, 8))),
                ('enddate', models.DateField(blank=True, null=True)),
                ('labourcount', models.IntegerField(default=1)),
                ('fname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='lrtable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typework', models.CharField(max_length=200)),
                ('startdate', models.DateField(default=datetime.date(2019, 6, 8))),
                ('enddate', models.DateField(blank=True, null=True)),
                ('lname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_pics/image001.jpg', upload_to='profile_pics'),
        ),
    ]