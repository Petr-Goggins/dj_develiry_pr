from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):

    user = models.OneToOneField(
User,
on_delete=models.CASCADE,
related_name='profile',
verbose_name='Пользователь',
)
    phone = models.CharField(
max_length=20,
blank=True,
verbose_name='Телефон',
)
    address = models.CharField(
max_length=300,
blank=True,
verbose_name='Адрес доставки',
)
    birth_date = models.DateField(
null=True,
blank=True,
verbose_name='Дата рождения',
)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = 'Профиль'
    verbose_name_plural = 'Профили'
def __str__(self):
    return f'Профиль {self.user.username}'
class Courier(models.Model):
    TRANSPORT_CHOICES = [
    ('foot', 'Пешком'),
    ('bike', 'Велосипед'),
    ('car', 'Автомобиль'),
    ]
    user = models.OneToOneField(
    User,
    on_delete=models.CASCADE,
    related_name='courier',

    verbose_name='Пользователь',
    )
    phone = models.CharField(
    max_length=20,
    verbose_name='Рабочий телефон',
    )
    transport = models.CharField(
    max_length=10,
    choices=TRANSPORT_CHOICES,
    default='bike',
    verbose_name='Транспорт',
    )
    is_active = models.BooleanField(
    default=True,
    verbose_name='Работает',
    )
    hired_at = models.DateField(
    auto_now_add=True,
    verbose_name='Дата найма',
    )
    class Meta:
     verbose_name = 'Курьер'
    verbose_name_plural = 'Курьеры'
def __str__(self):
    return f'Курьер {self.user.get_full_name() or self.user.username}'