# Generated by Django 2.0.6 on 2020-09-09 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='networkGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='', verbose_name='分组名称')),
                ('networks', models.TextField(default='', verbose_name='网络')),
                ('parent', models.TextField(default='', verbose_name='父分组')),
                ('parent_array', models.TextField(default='', verbose_name='父分组列表')),
                ('haschild', models.BooleanField(default=False, verbose_name='是否有孩子分组')),
            ],
        ),
    ]
