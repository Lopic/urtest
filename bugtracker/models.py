# File encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Tester(models.Model):
    """Модель тестера"""
    QUALIFICATION_CHOICES = (
        ('l', 'Начинающий'),
        ('m', 'Любитель'),
        ('h', 'Опытный тестировщик'),
        ('g', 'Профессиональный тестировщик'),
    )
    name = models.CharField("имя", max_length=30)
    surname = models.CharField("фамилия", max_length=30)
    email = models.EmailField("e-mail")
    
    experience = models.IntegerField("опыт (лет)")
    qualification = models.CharField("квалификация", max_length=1,
                                     choices=QUALIFICATION_CHOICES,
                                     default='l')
    languages = models.CharField("знание языков", max_length=100)
    program_languages = models.CharField("языки программирования", max_length=200)
    address = models.CharField("адрес", max_length=200)
    birthdate = models.DateField("дата рождения")
    hobby = models.TextField("хобби", blank=True)
    about = models.TextField("о себе", blank=True)
    registration_date = models.DateField("дата регистрации", auto_now_add=True)

    projects = models.ManyToManyField('Project', blank=True,
                                        related_name='testers',
                                        verbose_name="проекты")

    account = models.OneToOneField(User)

    class Meta:
        verbose_name = "тестер"
        verbose_name_plural = "тестеры"

    def __unicode__(self):
        return "%s %s" % (self.name, self.surname)


class Company(models.Model):
    """Модель компании"""
    TYPE_CHOICES = (
        ('y', 'Юридическое лицо'),
        ('f', 'Физическое лицо'),
    )
    name = models.CharField("название", max_length=100)
    type = models.CharField("Лицо", max_length=1, choices=TYPE_CHOICES,
                            default='y')
    email = models.EmailField("e-mail")
    address = models.CharField("адрес", max_length=200)
    registration_date = models.DateField("дата регистрации", auto_now_add=True)

    account = models.OneToOneField(User)

    class Meta:
        verbose_name = "компания"
        verbose_name_plural = "компании"

    def __unicode__(self):
        return self.name


class Project(models.Model):
    """Модель проекта"""
    LEVEL_CHOICES = (
        ('l', 'Небольшой'),
        ('m', 'Нормальный такой'),
        ('h', 'Пацанский'),
        ('g', 'Как у негра'),
    )
    name = models.CharField("название", max_length=100)
    company = models.ForeignKey('Company', related_name='projects',
                                verbose_name="разработчик")
    description = models.TextField("описание")
    level = models.CharField("размер", max_length=1, choices=LEVEL_CHOICES,
                             default='l')
    submit_date = models.DateField("дата размещения", auto_now_add=True)
    planned_date = models.DateField("предполагаемая дата сдачи")
    paid = models.IntegerField("выплачено", blank=True, null=True)
    bugget = models.IntegerField("бюджет", blank=True, null=True)
    program_languages = models.CharField("язык программирования", max_length=100)
    document_languages = models.CharField("язык документации", max_length=100)

    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"

    def __unicode__(self):
        return self.name


class Bug(models.Model):
    """Модель бага"""
    SEVERITY_CHOICES = (
        ('l', 'Низкая'),
        ('m', 'Средняя'),
        ('h', 'Высокая'),
        ('g', 'OMG PEOPLE ARE DYING'),
    )
    name = models.CharField("название", max_length=100)
    severity = models.CharField("критичность", max_length=1, choices=SEVERITY_CHOICES)
    submit_date = models.DateField("дата добавления")
    description = models.TextField("описание")

    project = models.ForeignKey('Project', related_name='bugs',
                                verbose_name="проект")
    tester = models.ForeignKey('Tester', related_name='bugs',
                                verbose_name="тестировщик")

    class Meta:
        verbose_name = "баг"
        verbose_name_plural = "баги"

    def __unicode__(self):
        return self.name
