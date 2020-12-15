# Generated by Django 3.1.1 on 2020-10-06 18:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='topic',
            name='length',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='student',
            name='province',
            field=models.CharField(default='ON', max_length=2),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Confirmed'), (2, 'On Hold')], default=1)),
                ('order_date', models.DateField(default=django.utils.timezone.now)),
                ('courses', models.ManyToManyField(blank=True, to='myapp.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myapp.student')),
            ],
        ),
    ]