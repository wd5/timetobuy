#coding: utf-8
from django.core.management.base import BaseCommand
from optparse import make_option
from django.conf import settings
import os

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('-i', '--initial',
            action='store_true',
            default=False,
            help='South initial of all apps'),
        make_option('-a', '--auto',
            action='store_true',
            default=False,
            help='South auto for all apps')
        )
    manage_py = os.path.join(settings.PROJECT_ROOT, 'manage.py')

    def make_initial(self, app):
        os.system('%s schemamigration %s --initial' % (self.manage_py, app))

    def make_auto(self, app):
        print app
        os.system('%s schemamigration %s --auto' % (self.manage_py, app))

    def handle(self, *args, **options):
        project_name = os.path.split(os.path.dirname(settings.PROJECT_ROOT))[1]
        myapps = []
        for app in os.listdir(settings.PROJECT_ROOT):
            if os.path.isdir(app):
                if '__init__.py' in os.listdir(app):
                    if not project_name == app:
                        myapps.append(app)
        if options['initial']:
            for app in myapps:
                self.make_initial(app)
        elif options['auto']:
            for app in myapps:
                self.make_auto(app)
