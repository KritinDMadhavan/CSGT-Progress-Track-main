# Generated by Django 4.0.5 on 2022-08-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book_editor',
            name='Emp_ID',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='collaboration',
        ),
        migrations.RemoveField(
            model_name='conference',
            name='type_of_publication',
        ),
        migrations.RemoveField(
            model_name='journal',
            name='type_of_publication',
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='conference',
            name='no_of_attendees',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='indexing',
            field=models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS'), ('Springer', 'Springer'), ('Ei Compendex', 'Ei Compendex')], max_length=20),
        ),
        migrations.AlterField(
            model_name='conference',
            name='indexing',
            field=models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS'), ('Springer', 'Springer'), ('Ei Compendex', 'Ei Compendex')], max_length=20),
        ),
        migrations.AlterField(
            model_name='journal',
            name='indexing',
            field=models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS'), ('Springer', 'Springer'), ('Ei Compendex', 'Ei Compendex')], max_length=20),
        ),
        migrations.DeleteModel(
            name='book_chapter',
        ),
        migrations.DeleteModel(
            name='book_editor',
        ),
    ]
