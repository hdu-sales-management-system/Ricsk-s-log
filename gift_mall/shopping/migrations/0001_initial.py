# Generated by Django 2.1.1 on 2018-11-16 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hot', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
                ('receive_mark', models.IntegerField(default=0)),
                ('present_num', models.DecimalField(decimal_places=0, max_digits=9)),
                ('logistics', models.CharField(max_length=200)),
                ('begin_date', models.DateTimeField()),
                ('sum_money', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user_feedback', models.CharField(max_length=200)),
                ('type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Present',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('on_date', models.DateTimeField()),
                ('store_num', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=11)),
                ('hot', models.IntegerField(default=0)),
                ('off', models.IntegerField(default=0)),
                ('off_cost', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Present')),
                ('ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Category')),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('present', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Present')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hot', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('auth', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('birthday', models.DateTimeField()),
                ('nickname', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[(1, '男'), (2, '女'), (0, '无')], default=0, max_length=200)),
                ('phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='relationshipt',
            name='ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.Tag'),
        ),
        migrations.AddField(
            model_name='order',
            name='present',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.Present'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shopping.User'),
        ),
    ]
