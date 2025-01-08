from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import GEOSGeometry

from planning_cases.models import planning_case

from django.utils.timezone import localdate, now
from datetime import timedelta, datetime
from django.db import IntegrityError

from ._scrape_accella import get_case_list, get_case_details
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Command(BaseCommand):
    help = "Download and save cases"

    def add_arguments(self, parser):
        parser.add_argument("--start_date", dest='start_date', default=localdate(now()-timedelta(1)).strftime('%m/%d/%Y'))
        parser.add_argument("--end_date", dest='end_date', default=localdate().strftime('%m/%d/%Y'))
        parser.add_argument("--case_number", dest='case_number', nargs='+')


    def handle(self, *args, **options):
        if options['case_number'] is not None:
            cases = []
            for case_number in options['case_number']:
                case_details = get_case_details(case=case_number)
                cases.append(case_details)
        else:
            try:
                cases = get_case_list(start_date=options['start_date'], end_date=options['end_date'])
            except (NoSuchElementException, TimeoutException) as e:
                cases = []
                 self.stdout.write('Exception during case list fetch.')
        cases_created = 0
        self.stdout.write((cases)
        for case_details in cases:
            try:
                geometry_pnt=case_details['PNT_GEOM']
                geometry_poly=case_details['POLY_GEOM']

            except ValueError:
                geometry_pnt = None
                geometry_poly = None
                self.stdout.write('ValueError with geometry')
            try:
                obj, created = planning_case.objects.update_or_create(
                    case_number=case_details['Case Number'],
                    defaults = {
                        'case_date':datetime.strptime(case_details['Case Date'], "%m/%d/%Y").date(),
                        'case_type':case_details['CaseType'],
                        'location':case_details['Location'],
                        'description':case_details['Description'],
                        'owner':case_details['Owner'],
                        'case_url':case_details['Case URL'],
                        'geometry_pnt':geometry_pnt,
                        'parcel_number':case_details['Parcel'],
                    },
                )
                 self.stdout.write(created, obj)
                if created:
                    cases_created = cases_created + 1
            except IntegrityError as e:
                self.stdout.write('integrityerror', e)

        self.stdout.write(
            self.style.SUCCESS('Successfully fetched and saved {} cases - {} new'.format(len(cases), cases_created) )
        )
