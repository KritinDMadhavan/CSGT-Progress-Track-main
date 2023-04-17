# Generated by Django 4.0.5 on 2022-08-05 15:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=320, primary_key=True, serialize=False, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(to='auth.group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=20)),
                ('date_of_join', models.DateField()),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'), ('Prefer not to say', 'Prefer not to say')], max_length=20)),
                ('orcid', models.IntegerField(blank=True, default=0, null=True)),
                ('research_gate', models.CharField(blank=True, max_length=256, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=256, null=True)),
                ('google_scholar', models.CharField(blank=True, max_length=256, null=True)),
                ('personal_page', models.CharField(blank=True, max_length=256, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('role', models.CharField(choices=[('PI', 'PI'), ('Co-PI', 'Co-PI'), ('Other', 'Other')], max_length=30)),
                ('funding_agency', models.CharField(max_length=100)),
                ('amount_registered', models.IntegerField(blank=True, null=True)),
                ('amount_sanctioned', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('type', models.CharField(choices=[('National', 'National'), ('International', 'International')], max_length=20)),
                ('no_of_authors', models.IntegerField()),
                ('filed_date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('published_date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('granted_date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('no_of_authors', models.IntegerField()),
                ('journal_name', models.CharField(max_length=100)),
                ('collaboration', models.CharField(choices=[('National', 'National'), ('International', 'International'), ('Internal', 'Internal')], max_length=20)),
                ('indexing', models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS'), ('Springer', 'Springer')], max_length=20)),
                ('impact_factor', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('volume_no', models.IntegerField(blank=True, null=True)),
                ('issue_no', models.IntegerField(blank=True, null=True)),
                ('digital_obj_id', models.CharField(blank=True, max_length=30, null=True)),
                ('type_of_publication', models.CharField(choices=[('Open Access', 'Open Access'), ('Subscription', 'Subscription')], max_length=100)),
                ('funder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_of_publication', models.IntegerField(blank=True, null=True)),
                ('support', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True)),
                ('emp_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='industrial_interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mou_signed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=30)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0))),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='consultancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Product development', 'Product development'), ('Research Collaboration', 'Research Collaboration')], max_length=50)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('company_name', models.CharField(max_length=50)),
                ('funding_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=5)),
                ('amount_registered', models.IntegerField(blank=True, null=True)),
                ('amount_sanctioned', models.IntegerField(blank=True, null=True)),
                ('invoice_number', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=100)),
                ('no_of_authors', models.IntegerField()),
                ('collaboration', models.CharField(choices=[('National', 'National'), ('International', 'International'), ('Internal', 'Internal')], max_length=20)),
                ('conference_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('place', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('National', 'National'), ('International', 'International')], max_length=20)),
                ('indexing', models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS'), ('Springer', 'Springer')], max_length=20)),
                ('conducting', models.CharField(choices=[('Conducting', 'Conducting'), ('Attending', 'Attending')], max_length=20)),
                ('published_as', models.CharField(choices=[('Research Paper', 'Research Paper')], max_length=30)),
                ('digital_obj_id', models.CharField(blank=True, max_length=30, null=True)),
                ('type_of_publication', models.CharField(choices=[('Subscription', 'Subscription')], max_length=100)),
                ('funder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_of_publication', models.IntegerField(blank=True, null=True)),
                ('support', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='book_editor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('no_of_authors', models.IntegerField()),
                ('Designation', models.CharField(max_length=20)),
                ('Collaboration', models.CharField(choices=[('National', 'National'), ('International', 'International'), ('Internal', 'Internal')], max_length=20)),
                ('Author_pos', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('Indexing', models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS')], max_length=20)),
                ('ISSN_ISBN_number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('publisher_name', models.CharField(max_length=30)),
                ('Type_of_publisher', models.CharField(choices=[('National', 'National'), ('International', 'International')], max_length=30)),
                ('Vol_no', models.IntegerField(blank=True, null=True)),
                ('Issue_no', models.IntegerField(blank=True, null=True)),
                ('DOI', models.CharField(blank=True, max_length=30, null=True)),
                ('Type_of_publication', models.CharField(choices=[('Open Access', 'Open Access'), ('Subscription', 'Subscription')], max_length=100)),
                ('Funder_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Enter if type is "Open" ')),
                ('Amount_of_Publication', models.IntegerField(blank=True, null=True, verbose_name='Enter if type is "Open" ')),
                ('Support', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True, verbose_name='Whether Support received from Vellore Institute of Technology?')),
                ('Emp_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='book_chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('no_of_authors', models.IntegerField()),
                ('Designation', models.CharField(max_length=20)),
                ('Collaboration', models.CharField(choices=[('National', 'National'), ('International', 'International'), ('Internal', 'Internal')], max_length=20)),
                ('Author_pos', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])),
                ('Indexing', models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS')], max_length=20)),
                ('ISSN_ISBN_number', models.IntegerField()),
                ('year', models.IntegerField()),
                ('book_title', models.CharField(max_length=100)),
                ('publisher_name', models.CharField(max_length=30)),
                ('Type_of_publisher', models.CharField(choices=[('National', 'National'), ('International', 'International')], max_length=30)),
                ('Vol_no', models.IntegerField(blank=True, null=True)),
                ('Issue_no', models.IntegerField(blank=True, null=True)),
                ('DOI', models.CharField(blank=True, max_length=30, null=True)),
                ('Type_of_publication', models.CharField(choices=[('Open Access', 'Open Access'), ('Subscription', 'Subscription')], max_length=100)),
                ('Funder_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Enter Funder name if type is "Open" ')),
                ('Amount_of_Publication', models.IntegerField(blank=True, null=True, verbose_name='Enter Amount of Publication if type is "Open" ')),
                ('Support', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True, verbose_name='Whether Support received from Vellore Institute of Technology?')),
                ('Emp_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('chapter_title', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(max_length=20)),
                ('no_of_authors', models.IntegerField()),
                ('type_of_publication', models.CharField(choices=[('Open Access', 'Open Access'), ('Subscription', 'Subscription')], max_length=100)),
                ('volume_no', models.IntegerField(blank=True, null=True)),
                ('issue_no', models.IntegerField(blank=True, null=True)),
                ('digital_obj_id', models.CharField(blank=True, max_length=30, null=True)),
                ('year', models.IntegerField()),
                ('isbn', models.IntegerField()),
                ('indexing', models.CharField(choices=[('SCI', 'SCI'), ('SCIE', 'SCIE'), ('SCOPUS', 'SCOPUS'), ('Springer', 'Springer')], max_length=20)),
                ('funder_name', models.CharField(blank=True, max_length=100, null=True)),
                ('amount_of_publication', models.IntegerField(blank=True, null=True)),
                ('support', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=4, null=True)),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.personal')),
            ],
        ),
        migrations.AddConstraint(
            model_name='project',
            constraint=models.UniqueConstraint(fields=('emp_id', 'title'), name='unique-emp_id-title-project'),
        ),
        migrations.AddConstraint(
            model_name='patent',
            constraint=models.UniqueConstraint(fields=('emp_id', 'title'), name='unique-emp_id-title-patent'),
        ),
        migrations.AddConstraint(
            model_name='journal',
            constraint=models.UniqueConstraint(fields=('emp_id', 'article_title'), name='unique-emp_id-article_title-journal'),
        ),
        migrations.AddConstraint(
            model_name='consultancy',
            constraint=models.UniqueConstraint(fields=('emp_id', 'company_name'), name='unique-emp_id-company_name-consultancy'),
        ),
        migrations.AddConstraint(
            model_name='conference',
            constraint=models.UniqueConstraint(fields=('emp_id', 'article_title'), name='unique-emp_id-article_title-conference'),
        ),
        migrations.AddConstraint(
            model_name='book_editor',
            constraint=models.UniqueConstraint(fields=('Emp_ID', 'title'), name='unique_EmpID_title_bookEditor'),
        ),
        migrations.AddConstraint(
            model_name='book_chapter',
            constraint=models.UniqueConstraint(fields=('Emp_ID', 'title'), name='unique_EmpID_title_bookChapter'),
        ),
        migrations.AddConstraint(
            model_name='book',
            constraint=models.UniqueConstraint(fields=('emp_id', 'book_title'), name='unique-emp_id-book_title-book'),
        ),
    ]
