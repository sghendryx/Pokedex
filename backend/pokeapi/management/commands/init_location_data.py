from django.core.management.base import BaseCommand
from pokeapi.models import Region, Location, Area
import requests

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = 'Initialize database with region and location information'

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        print('seeding data...')
        run_seed(self, options['mode'])
        print('done.')


def clear_data():
    """Deletes all the table data"""
    print("Deleting Regions and Locations...")
    Region.objects.all().delete()


def save_regions():
    """Creates a region in the database for every region given by pokemon API"""
    print("********* Creating Regions *************")
    response = requests.get("https://pokeapi.co/api/v2/region/")
    json = response.json()
    regions = json['results']
    for r in regions:
        region_name = r['name']
        print(f'{region_name} saving...')
        Region.objects.create(name=region_name, poke_id=get_id_from_url(r['url']))


def save_locations():
    """Creates a location in the database for each region"""
    print("********* Creating Locations **********")
    regions = Region.objects.all()
    for r in regions:
        response = requests.get(f'https://pokeapi.co/api/v2/region/{r.poke_id}')
        json = response.json()
        locations = json['locations']
        print(f'*********** Saving locations for {r.name} ***********')
        for l in locations:
            location_name = l['name']
            print(f'{location_name} saving...')
            Location.objects.create(name=location_name, poke_id=get_id_from_url(l['url']), region=r)


def save_areas():
    print("*************** Create Areas *****************")
    locations = Location.objects.all()
    for l in locations:
        print(f'*********** Saving Areas for {l.name} ***********')
        response = requests.get(f'https://pokeapi.co/api/v2/location/{l.poke_id}')
        json = response.json()
        areas = json['areas']
        for a in areas:
            area_name = a['name']
            print(f'{area_name} saving...')
            Area.objects.create(name=area_name, poke_id=get_id_from_url(a['url']), location=l)


def get_id_from_url(url):
    return int(url.split('/')[-2])


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    save_regions()
    save_locations()
    save_areas()
