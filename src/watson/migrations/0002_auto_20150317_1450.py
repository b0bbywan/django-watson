# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.core.management import call_command


def install_watson(apps, schema_editor):
    call_command("installwatson", verbosity=0)

def uninstall_watson(apps, schema_editor):
    call_command("uninstallwatson", verbosity=0)

class Migration(migrations.Migration):

    dependencies = [
        ('watson', '0001_initial'),
    ]

    operations = [ 
    	migrations.RunPython(
            install_watson,
            uninstall_watson,
        ),
    ]
