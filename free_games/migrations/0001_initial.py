# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('game_description', models.CharField(max_length=200)),
                ('game_title', models.CharField(max_length=50)),
                ('image_url', models.URLField()),
                ('game_url', models.URLField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
