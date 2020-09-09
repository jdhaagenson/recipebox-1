# Generated by Django 3.1 on 2020-08-05 19:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('time_required', models.CharField(max_length=20)),
                ('instructions', models.TextField()),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(default='Default Value', max_length=300),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.author'),
        ),
    ]