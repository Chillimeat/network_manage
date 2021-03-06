# Generated by Django 2.0.6 on 2020-10-15 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceArpTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(unique=True, verbose_name='IP地址')),
                ('network', models.GenericIPAddressField(verbose_name='网络')),
                ('mac', models.CharField(default='', max_length=20, verbose_name='mac地址')),
                ('host_and_port', models.TextField(default='[]', verbose_name='IP地址所对应的主机名和端口')),
                ('query_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 163364), verbose_name='最新探测时间')),
            ],
            options={
                'verbose_name': '设备探测arp表',
                'verbose_name_plural': '设备探测arp表',
                'db_table': 'device_query_arp_table',
            },
        ),
        migrations.CreateModel(
            name='DeviceMacTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mac', models.CharField(default='', max_length=20, unique=True, verbose_name='mac地址')),
                ('host_and_port', models.TextField(default='[]', verbose_name='mac地址所对应的主机名和端口')),
                ('query_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 163976), verbose_name='最新探测时间')),
            ],
            options={
                'verbose_name': '设备探测MAC表',
                'verbose_name_plural': '设备探测MAC表',
                'db_table': 'device_query_mac_table',
            },
        ),
        migrations.CreateModel(
            name='NetworkToDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.GenericIPAddressField(verbose_name='网络')),
                ('device_ip', models.TextField(default='[]', verbose_name='探测设备IP')),
                ('device_hostname', models.TextField(default='[]', verbose_name='探测设备主机名')),
                ('interface', models.TextField(default='[]', verbose_name='端口名称')),
            ],
            options={
                'verbose_name': '探测网络对应的设备',
                'verbose_name_plural': '探测网络对应的设备',
                'db_table': 'network_to_device',
            },
        ),
        migrations.CreateModel(
            name='QueryDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snmp_host', models.GenericIPAddressField(unique=True, verbose_name='探测设备IP')),
                ('snmp_host_int', models.BigIntegerField(default=0, verbose_name='探测设备IP十进制')),
                ('snmp_port', models.IntegerField(default=0, verbose_name='探测设备端口')),
                ('device_hostname', models.TextField(default='', verbose_name='探测设备主机名')),
                ('device_manufacturer_info', models.TextField(default='', verbose_name='探测设备厂商信息')),
                ('snmp_group', models.CharField(max_length=30, verbose_name='团体名')),
                ('query_status', models.SmallIntegerField(choices=[(0, '未启动'), (1, '等待中'), (2, '探测完成'), (3, '路由不可达'), (4, '未知错误'), (5, '端口未开放'), (6, '探测中...')], default=0, verbose_name='探测状态')),
                ('auto_enable', models.BooleanField(default=False, verbose_name='定时任务开关')),
                ('crontab_time', models.TextField(default='', verbose_name='定时任务时间')),
                ('networks', models.TextField(default='[]', verbose_name='所有网络')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 160500), verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 160561), verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '设备探测信息',
                'verbose_name_plural': '设备探测信息',
                'db_table': 'device_query_task',
            },
        ),
        migrations.CreateModel(
            name='SnmpQueryIpRouteTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snmp_host', models.GenericIPAddressField(verbose_name='探测设备IP')),
                ('snmp_host_int', models.BigIntegerField(default=0, verbose_name='探测设备IP十进制')),
                ('dest_ip', models.CharField(default='', max_length=30, verbose_name='目的ip地址/掩码')),
                ('next_hop', models.CharField(default='', max_length=30, verbose_name='下一跳IP')),
                ('port_index', models.IntegerField(default=0, verbose_name='端口索引')),
                ('route_table_type', models.IntegerField(choices=[(1, 'other'), (2, 'invalid'), (3, 'direct'), (4, 'indirect')], default=0, verbose_name='路由表类型')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 164555), verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 164581), verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '设备探测的路由表',
                'verbose_name_plural': '设备探测的路由表',
                'db_table': 'ip_route_table',
            },
        ),
        migrations.CreateModel(
            name='SnmpQueryResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snmp_host', models.GenericIPAddressField(verbose_name='探测设备IP')),
                ('snmp_host_int', models.BigIntegerField(default=0, verbose_name='探测设备IP十进制')),
                ('if_name', models.TextField(default='', verbose_name='端口名称')),
                ('if_speed', models.CharField(default='', max_length=100, verbose_name='端口速率')),
                ('if_operstatus', models.CharField(default='', max_length=100, verbose_name='端口状态')),
                ('if_ip_setup', models.TextField(default='', verbose_name='端口ip地址')),
                ('if_descrs', models.TextField(default='', verbose_name='端口描述信息')),
                ('arp_infos', models.TextField(default='', verbose_name='arp信息')),
                ('brige_macs', models.TextField(default='', verbose_name='二层mac信息')),
                ('if_index', models.IntegerField(default=0, verbose_name='端口索引')),
                ('created_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 161667), verbose_name='创建时间')),
                ('last_mod_time', models.DateTimeField(default=datetime.datetime(2020, 10, 15, 15, 44, 20, 161710), verbose_name='修改时间')),
            ],
            options={
                'verbose_name': '设备探测详情',
                'verbose_name_plural': '设备探测详情',
                'db_table': 'device_query_result',
            },
        ),
        migrations.AlterUniqueTogether(
            name='snmpqueryresult',
            unique_together={('snmp_host_int', 'if_index')},
        ),
        migrations.AlterUniqueTogether(
            name='snmpqueryiproutetable',
            unique_together={('snmp_host_int', 'dest_ip')},
        ),
    ]
