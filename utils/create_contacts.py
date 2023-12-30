import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'agenda.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contatos.models import Categoria, Contato

    Contato.objects.all().delete()
    Categoria.objects.all().delete()

    fake = faker.Faker('pt_BR')
    categories = ['Amigos', 'Família', 'Conhecidos']

    django_categories = [Categoria(nome=name) for name in categories]

    for category in django_categories:
        category.save()

    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        created_date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contato(
                nome=first_name,
                sobrenome=last_name,
                telefone=phone,
                email=email,
                data_criacao=created_date,
                descricao=description,
                categoria=category,
            )
        )

    if len(django_contacts) > 0:
        Contato.objects.bulk_create(django_contacts)