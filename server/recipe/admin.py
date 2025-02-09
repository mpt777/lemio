from datetime import timedelta
from django import forms
from django.contrib import admin
from django.forms import TimeInput

from durationwidget.widgets import TimeDurationWidget

from recipe.models import *

# Register your models here.

class IngredientInlineAdmin(admin.TabularInline):
  model = Ingredient
  extra=0

class RecipeAdmin(admin.ModelAdmin):
  list_display = ('name', 'handle', 'created_by')
  raw_id_fields = ("created_by", "image")
  search_fields = ("name", "handle")
  inlines = (IngredientInlineAdmin,)
  # formfield_overrides = {
  #     models.PositiveIntegerField: {'widget': TimeDurationWidget(show_days=False, show_seconds=False)},
  # }


class UnitAdmin(admin.ModelAdmin):
  list_display = ('name', 'code', 'system', "kind")
  list_filter = ("system", "kind")
  search_fields = ("name", "code")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Unit, UnitAdmin)