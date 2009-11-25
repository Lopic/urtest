# File encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Tester(User):
    """Модель тестера"""
    QUALIFICATION_CHOICES = (
        ('l', 'Начинающий'),
        ('m', 'Любитель'),
        ('h', 'Опытный тестировщик'),
        ('g', 'Профессиональный тестировщик'),
    )
    user = models.OneToOneField(User, parent_link=True)
    # Имя, фамилия, email наследуются
    birthdate = models.DateField("дата рождения")
    address = models.CharField("адрес", max_length=200)

    # Участие в проектах
    projects = models.ManyToManyField('Project', blank=True,
                                        related_name='testers',
                                        verbose_name="проекты")

    languages = models.CharField("языки общения", max_length=100)
    program_languages = models.CharField("языки программирования", max_length=200)
    
    experience = models.IntegerField("опыт (лет)")
    qualification = models.CharField("квалификация", max_length=1,
                                     choices=QUALIFICATION_CHOICES,
                                     default='l')
                                     
    about = models.TextField("о себе", blank=True)

    def _get_full_name(self):
        full_name = self.user.get_full_name()
        if len(full_name) == 0:
            return self.user.username
        else:
            return self.user.get_full_name()

    name = property(_get_full_name)
    
    class Meta:
        verbose_name = "тестер"
        verbose_name_plural = "тестеры"

    def __unicode__(self):
        return self.name


class Company(User):
    """Модель компании"""
    TYPE_CHOICES = (
        ('y', 'Юридическое лицо'),
        ('f', 'Физическое лицо'),
    )
    user = models.OneToOneField(User, parent_link=True)
    # Наследуются имя, фамилия.
    # Либо сделать их ФИО ответственного, либо игнорировать
    name = models.CharField("название компании", max_length=100)
    type = models.CharField("Лицо", max_length=1, choices=TYPE_CHOICES,
                            default='y')
    #email = models.EmailField("e-mail")
    address = models.CharField("адрес", max_length=200)
    
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

    document_languages = models.CharField("язык документации", max_length=100)
    program_languages = models.CharField("язык программирования", max_length=100)

    paid = models.IntegerField("выплачено", blank=True, null=True)
    bugget = models.IntegerField("бюджет", blank=True, null=True)

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
    submit_date = models.DateField("дата добавления", auto_now_add=True)
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
