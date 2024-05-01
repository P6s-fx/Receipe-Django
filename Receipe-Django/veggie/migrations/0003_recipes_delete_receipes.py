# Generated by Django 5.0 on 2023-12-23 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0002_rename_receipe_receipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('recipe_description', models.TextField()),
                ('recipe_image', models.ImageField(upload_to='recipes')),
            ],
        ),
        migrations.DeleteModel(
            name='Receipes',
        ),
    ]