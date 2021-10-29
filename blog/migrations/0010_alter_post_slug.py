# Generated by Django 3.2.8 on 2021-10-29 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_postview_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, default=models.CharField(max_length=100, unique=True), help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, unique=True, verbose_name='slug'),
        ),
    ]
