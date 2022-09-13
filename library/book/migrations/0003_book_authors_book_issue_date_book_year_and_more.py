# Generated by Django 4.1 on 2022-09-07 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_remove_author_books_alter_author_name_and_more'),
        ('book', '0002_book_count_book_description_book_name_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='book', to='author.author'),
        ),
        migrations.AddField(
            model_name='book',
            name='issue_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='year',
            field=models.IntegerField(default=1900),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]