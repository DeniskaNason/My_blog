# Generated by Django 4.2.3 on 2023-07-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_alter_tag_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.tag', verbose_name='Теги'),
        ),
    ]
