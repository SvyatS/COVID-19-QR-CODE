import random
import uuid
from django.db import models


def generate_vaccine_id():
    return '10000{}'.format(str(random.randint(0, 99999999999)))

class UserData(models.Model):
    ''' Data of certified user'''

    _SEX_CHOISE = (
        ('male', 'Мужской'),
        ('female', 'Женский')
    )

    _ADDRESS = 'Томская обл, г Томск, ул Источная, д. 42, кв.2'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField('Name', max_length=128)
    middle_name = models.CharField('Middle name', max_length=128)
    surname = models.CharField('Surname', max_length=128)
    date_birthday = models.DateField('Birthday')
    vaccine_id = models.CharField("Vaccine id", default=generate_vaccine_id, max_length=16)
    sex = models.CharField('Sex', max_length=6, choices=_SEX_CHOISE)
    passport_series = models.CharField('Passport series', max_length=4)
    passport_number = models.CharField('Passport number', max_length=6)
    residence_address = models.CharField('Address', max_length=256, default=_ADDRESS)
    snills = models.CharField('Snils', max_length=11, null=True, default='')
    oms = models.CharField('OMS', max_length=11, null=True, default='')
    medical_organization = models.CharField("Medical organization", max_length=128, default='ОГАУЗ "Поликлиника №4"')

    def __str__(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.surname)



