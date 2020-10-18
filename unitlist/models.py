from django.db import models
from django.core import validators


class Attribute(models.Model):
    att_id = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        primary_key=True,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5)]
    )
    att_desc = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        default='',
        validators=[validators.RegexValidator(
                regex=u'^[a-zA-Z0-9_]+$',
                message='半角英数字とアンダーバーのみにしてください')]
    )
    att_desc_lower = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        default='',
        validators=[validators.RegexValidator(
                regex=u'^[a-z0-9_]+$',
                message='半角小文字英数字とアンダーバーのみにしてください')]
    )
    att_desc_jp = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        default=''
    )
    att_advantage_id = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5)]
    )

    def __str__(self):
        return self.att_desc


class Role(models.Model):
    role_id = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        primary_key=True,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(4)]
    )
    role_desc = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        default='',
        validators=[validators.RegexValidator(
                regex=u'^[a-z0-9_]+$',
                message='半角小文字英数字とアンダーバーのみにしてください')]
    )
    role_desc_jp = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        default=''
    )


class UnitType(models.Model):
    unit_type_id = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        primary_key=True,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(1)]
    )
    unit_type_desc = models.CharField(
        blank=True,
        null=False,
        max_length=100,
        default=''
    )

    def __str__(self):
        return self.unit_type_desc


class Unit(models.Model):
    unit_enable = models.BooleanField(
        default=False
    )
    unit_type = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    unit_no = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(1)]
    )
    unit_id = models.CharField(
        blank=False,
        null=False,
        max_length=100,
        default='',
        primary_key=True,
        validators=[validators.RegexValidator(
                regex=u'^[a-z0-9_]+$',
                message='半角小文字英数字とアンダーバーのみにしてください')]
    )
    sub_name = models.CharField(
        blank=True,
        null=False,
        max_length=100,
        default=''
    )
    jp_name = models.CharField(
        blank=True,
        null=False,
        max_length=100,
        default=''
    )
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    rarity = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(5)]
    )
    skill_desc = models.CharField(
        blank=True,
        null=False,
        max_length=500,
        default=''
    )
    skill_wait = models.IntegerField(
        blank=False,
        null=False,
        default=0,
        validators=[validators.MinValueValidator(0),
                    validators.MaxValueValidator(9999)]
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    gender = models.CharField(
        blank=True,
        null=False,
        max_length=100,
        default=''
    )
    race = models.CharField(
        blank=True,
        null=False,
        max_length=100,
        default=''
    )

    def __str__(self):
        return '{} {}'.format(self.sub_name, self.jp_name)
