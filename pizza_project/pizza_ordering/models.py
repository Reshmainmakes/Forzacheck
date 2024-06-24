from django.db import models

class KitchenLunch(models.Model):
    date = models.DateField()
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES,default='JP23')
    comments=models.TextField(null=True,blank=True)

    today_balls_total = models.IntegerField()
    yesterday_balls_total = models.IntegerField()

    class Meta:
        verbose_name = "Kitchen Department Lunch Shift(Quantity)"
        verbose_name_plural = "Kitchen Department Lunch Shift(Quantity)"

class KitchenLate(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    pizza_grade = models.IntegerField()
    tomorrow_balls_total = models.IntegerField()
    old_balls_total = models.IntegerField()
    balls_broken_today = models.IntegerField()
    pizzas_broken_today = models.IntegerField()

    class Meta:
        verbose_name = "Kitchen Department Late Shift(Quantity)"
        verbose_name_plural = "Kitchen Department Late Shift(Quantity)"


from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=100)

class TerminalLunch(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Terminal Department Lunch Shift"
        verbose_name_plural = "Terminal Department Lunch Shift"


class TerminalLate(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    HALLWAY_MOPPED_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    CELLAR_TIDY_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    REPLENISHED_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)
    hallway_mopped=models.CharField(max_length=3, choices=HALLWAY_MOPPED_CHOICES, blank=True, null=True,verbose_name="Hallway has been mopped")
    cellar_tidy=models.CharField(max_length=3, choices=CELLAR_TIDY_CHOICES, blank=True, null=True,verbose_name="Cellar rooms are garbage-free & tidy")
    replenished=models.CharField(max_length=3, choices=REPLENISHED_CHOICES, blank=True, null=True,verbose_name="Waiter's pad, receipt rolls, napkins have been replenished")

    class Meta:
        verbose_name = "Terminal Department Late Shift"
        verbose_name_plural = "Terminal Department Late Shift"

class KitchenSpecialcleaningMonday(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Kitchen Department Specialcleaning(Monday)"
        verbose_name_plural = "Kitchen Department Specialcleaning(Monday)"

class DryStorageCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Dry Storage Cleaning(Wednesday)"
        verbose_name_plural = "Dry Storage Cleaning(Wednesday)"

class WednesdayCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Kitchen Special Cleaning(Wednesday)"
        verbose_name_plural = "Kitchen Special Cleaning(Wednesday)"

class ApartmentCleaning(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    comments=models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Apartment Cleaning(Wednesday)"
        verbose_name_plural = "Apartment Cleaning(Wednesday)"

class KitchenLunchTask(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]
    KITCHEN_CLEANED_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    ENOUGH_LAUNDRY_CHOICES=[
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)

    task_kitchen_cleaned = models.CharField(max_length=3, choices=KITCHEN_CLEANED_CHOICES, blank=True, null=True,verbose_name="Kitchen cleaned according to instructions")
    task_enough_laundry=models.CharField(max_length=3, choices=ENOUGH_LAUNDRY_CHOICES, blank=True, null=True,verbose_name="Was there enough laundry")
    comments = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Kitchen Department Lunch Shift(Task)"
        verbose_name_plural = "Kitchen Department Lunch Shift(Task)"

class KitchenLateTask(models.Model):
    LOCATION_CHOICES = [
        ('JP23', 'JP23'),
        ('KP5', 'KP5'),
        ('TS17', 'TS17'),
    ]

    SIDE_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]

    soap_WC_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    toilet_paper_WC_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]

    grease_remover_kitchen_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    washingup_liquid_kitchen_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    blue_roll_kitchen_sufficient_CHOICES = [
        ('yes', 'YES'),
        ('no', 'NO'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, default='JP23')
    date = models.DateField()
    name = models.CharField(max_length=100)
    side = models.CharField(max_length=10, choices=SIDE_CHOICES,default=False) # New side field
    comments = models.TextField(null=True, blank=True)
    soap_WC_sufficient = models.CharField(max_length=3, choices=soap_WC_sufficient_CHOICES, blank=True, null=True)
    toilet_paper_WC_sufficient=models.CharField(max_length=3, choices=toilet_paper_WC_sufficient_CHOICES, blank=True, null=True)
    grease_remover_kitchen_sufficient=models.CharField(max_length=3, choices=grease_remover_kitchen_sufficient_CHOICES, blank=True, null=True)
    washingup_liquid_kitchen_sufficient=models.CharField(max_length=3, choices=washingup_liquid_kitchen_sufficient_CHOICES, blank=True, null=True)
    blue_roll_kitchen_sufficient=models.CharField(max_length=3, choices=blue_roll_kitchen_sufficient_CHOICES, blank=True, null=True)
    class Meta:
        verbose_name = "Kitchen Department Late Shift(Task)"
        verbose_name_plural = "Kitchen Department Late Shift(Task)"

