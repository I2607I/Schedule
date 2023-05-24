# Generated by Django 4.0 on 2022-08-26 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('slug', models.SlugField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='NumberLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.PositiveIntegerField()),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('content', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TypeLesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_even', models.BooleanField(default=True)),
                ('classroom', models.CharField(blank=True, max_length=20)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FWP.day')),
                ('number_lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FWP.numberlesson')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FWP.subject')),
                ('type_lesson', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FWP.typelesson')),
            ],
        ),
    ]