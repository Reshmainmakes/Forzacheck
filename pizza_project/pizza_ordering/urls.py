from django.urls import path
from . import views

urlpatterns = [
    path('department_selection/', views.department_shift_selection, name='department_shift_selection'),  # Department and shift selection page and submission
    # path('kitchenlunch/', views.kitchen_lunch_form, name='kitchen_lunch_form'),  # URL for kitchen lunch form
    path('kitchenlate/', views.kitchen_late_form, name='kitchen_late_form'),  # URL for kitchen late form
    # Define URLs for TerminalLunch and TerminalLate similarly
path('kitchenlunch_submit/', views.kitchen_lunch_submit, name='kitchen_lunch_submit'), # URL for handling kitchen lunch form submission
path('kitchen_lunch_form/', views.kitchen_lunch_form, name='kitchen_lunch_form'),
path('kitchenlunchdashboard/', views.kitchen_lunch_dashboard, name='kitchen_lunch_dashboard'), # Add this URL pattern
path('kitchenlate_submit/', views.kitchen_late_submit, name='kitchen_late_submit'),
path('kitchenlatedashboard/', views.kitchen_late_dashboard, name='kitchen_late_dashboard'), # Add this URL pattern
path('terminallunch/', views.terminal_lunch_form, name='terminal_lunch_form'),
path('terminallunch_submit/', views.terminal_lunch_submit, name='terminal_lunch_submit'),
    path('terminallunchdashboard/', views.terminal_lunch_dashboard, name='terminal_lunch_dashboard'),
    path('terminallate/', views.terminal_late_form, name='terminal_late_form'),
    path('terminallate_submit/', views.terminal_late_submit, name='terminal_late_submit'),
    path('terminallatedashboard/', views.terminal_late_dashboard, name='terminal_late_dashboard'),
    path('kitchenspecialcleaningmonday_submit/', views.kitchen_specialcleaning_monday_submit, name='kitchen_specialcleaning_monday_submit'),
    path('kitchenspecialcleaningmondaydashboard/', views.kitchen_specialcleaning_monday_dashboard, name='kitchen_specialcleaning_monday_dashboard'),
path('kitchen_specialcleaning_monday/', views.kitchen_specialcleaning_monday, name='kitchen_specialcleaning_monday'),


path('drystorage_cleaning_submit/', views.drystorage_cleaning_submit, name='drystorage_cleaning_submit'),
    path('dry_storage_cleaning_form/', views.dry_storage_cleaning_form, name='dry_storage_cleaning_form'),
    path('drystorage_cleaning_dashboard/', views.drystorage_cleaning_dashboard, name='drystorage_cleaning_dashboard'),

path('wednesday_cleaning_submit/', views.wednesday_cleaning_submit, name='wednesday_cleaning_submit'),
    path('wednesday_cleaning_kitchen/', views.wednesday_cleaning_kitchen, name='wednesday_cleaning_kitchen'),
    path('wednesday_cleaning_dashboard/', views.wednesday_cleaning_dashboard, name='wednesday_cleaning_dashboard'),

path('apartment_cleaning_submit/', views.apartment_cleaning_submit, name='apartment_cleaning_submit'),
    path('apartment_cleaning_form/', views.apartment_cleaning_form, name='apartment_cleaning_form'),
    path('apartment_cleaning_dashboard/', views.apartment_cleaning_dashboard, name='apartment_cleaning_dashboard'),

path('kitchen_lunch_task_submit/', views.kitchen_lunch_task_submit, name='kitchen_lunch_task_submit'),
    path('kitchen_lunch_task/', views.kitchen_lunch_task, name='kitchen_lunch_task'),
    path('kitchen_lunch_task_dashboard/', views.kitchen_lunch_task_dashboard, name='kitchen_lunch_task_dashboard'),

path('kitchen_late_task_submit/', views.kitchen_late_task_submit, name='kitchen_late_task_submit'),
    path('kitchen_late_task/', views.kitchen_late_task, name='kitchen_late_task'),
    path('kitchen_late_task_dashboard/', views.kitchen_late_task_dashboard, name='kitchen_late_task_dashboard'),

]

