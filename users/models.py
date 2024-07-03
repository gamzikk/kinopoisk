from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an Email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None):
    	user = self.create_user(username, email, phone, password=password)
    	user.is_staff = True
    	user.save(using=self._db)
    	return user

    # def create_superuser(self, email, password=None):
    #     user = self.create_user(email, password=password)
    #     user.is_staff = True
    #     user.save(using=self._db)
    #     return user


class CustomUser(AbstractBaseUser):
    username = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=100, unique=True)
    phone = PhoneNumberField('Номер', unique=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def has_perm(self, perm, obj=None):
    	return True

    def has_module_perms(self, app_label):
    	return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField('Аватар', null=True, blank=True, default='images_avatars/default_avatar.png', upload_to='images_avatars')

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Subscription(models.Model):
    name = models.CharField(max_length=100, unique=True)
    time_limit = models.IntegerField('Длительность')
    price = models.IntegerField('Цена')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subscription'
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class UserSubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    date = models.DateField('Дата подписки', auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        db_table = 'user_subscription'
        verbose_name = 'Подписка пользователя'
        verbose_name_plural = 'Подписки пользователей'