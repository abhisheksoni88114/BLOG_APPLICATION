# Generated by Django 3.1 on 2020-10-25 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201025_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='com',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
        ),
    ]
