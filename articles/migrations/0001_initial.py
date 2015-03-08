# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=200)),
                ('author', models.CharField(default=b'', max_length=200)),
                ('pub_date', models.DateField(default=datetime.date(2000, 1, 1))),
                ('department', models.CharField(default=b'IND', max_length=3, choices=[(b'ANT', b'Anthropology'), (b'ARC', b'Architecture School'), (b'ART', b'Art and Archaeology'), (b'AST', b'Astrophysical Sciences'), (b'CBE', b'Chemical and Biological Engineering'), (b'CHM', b'Chemistry'), (b'CEE', b'Civil and Environmental Engineering'), (b'CLA', b'Classics'), (b'COM', b'Comparative Literature'), (b'COS', b'Computer Science'), (b'CWR', b'Creative Writing Program'), (b'EAS', b'East Asian Studies'), (b'EEB', b'Ecology and Evolutionary Biology'), (b'ECO', b'Economics'), (b'ELE', b'Electrical Engineering'), (b'ENG', b'English'), (b'FRE', b'French'), (b'ITA', b'Italian'), (b'GEO', b'Geosciences'), (b'GER', b'German'), (b'HIS', b'History'), (b'IND', b'Independent Concentration'), (b'MAT', b'Mathematics'), (b'MAE', b'Mechanical and Aerospace Engineering'), (b'MOL', b'Molecular Biology'), (b'MUS', b'Music'), (b'NES', b'Near Eastern Studies'), (b'ORF', b'Operations Research and Financial Engineering'), (b'PHI', b'Philosophy'), (b'PHY', b'Physics'), (b'POL', b'Politics'), (b'PSY', b'Psychology'), (b'REL', b'Religion'), (b'SLA', b'Slavic Languages and Literature'), (b'SOC', b'Sociology'), (b'SPA', b'Spanish'), (b'POR', b'Portugese'), (b'THR', b'Theater'), (b'WWS', b'Woodrow Wilson School')])),
                ('abstract', models.TextField(default=b'')),
                ('article_link', models.URLField(default=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
