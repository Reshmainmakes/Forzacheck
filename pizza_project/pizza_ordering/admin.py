
from django.contrib import admin
from .models import KitchenLunch, KitchenLate, TerminalLunch, TerminalLate, KitchenSpecialcleaningMonday, \
    DryStorageCleaning, WednesdayCleaning, ApartmentCleaning, KitchenLunchTask, KitchenLateTask


@admin.register(KitchenLunch)
class KitchenLunchAdmin(admin.ModelAdmin):
    list_display = ('date', 'location','name', 'today_balls_total', 'yesterday_balls_total','comments')
from django.contrib import admin
from .models import KitchenLunch

@admin.register(KitchenLate)
class KitchenLateAdmin(admin.ModelAdmin):
    list_display = ('date', 'location','name',  'pizza_grade','tomorrow_balls_total','old_balls_total','balls_broken_today','pizzas_broken_today','comments')
@admin.register(TerminalLunch)
class TerminalLunchAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')
@admin.register(TerminalLate)
class TerminalLateAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','hallway_mopped','cellar_tidy','replenished','comments')
@admin.register(KitchenSpecialcleaningMonday)
class KitchenSpecialCleaningMondayAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')
@admin.register(DryStorageCleaning)
class DryStorageCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')

@admin.register(WednesdayCleaning)
class DryStorageCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')

@admin.register(ApartmentCleaning)
class ApartmentCleaningAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments')
@admin.register(KitchenLunchTask)
class KitchenLunchTaskAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','task_kitchen_cleaned','task_enough_laundry','comments')
@admin.register(KitchenLateTask)
class KitchenLateTaskAdmin(admin.ModelAdmin):
    list_display = ('date','location','name','comments','side','soap_WC_sufficient','toilet_paper_WC_sufficient','grease_remover_kitchen_sufficient','washingup_liquid_kitchen_sufficient','blue_roll_kitchen_sufficient')