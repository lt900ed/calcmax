from django.db import models
from django.core import validators

# Create your models here.
class UnitSet(models.Model):
	unit_set_id = models.IntegerField(
		blank=False,
		null=False,
		default=0,
		primary_key=True,
		validators=[validators.MinValueValidator(0)]
	)
	unit_set_text = models.CharField(
		blank=False,
		null=False,
		max_length=300,
		default='',
		validators=[validators.RegexValidator(
				regex=u'^[a-z0-9_\-]+$',
				message='半角小文字英数字ハイフンアンダーバーのみにしてください')]
	)