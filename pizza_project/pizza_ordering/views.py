from django.shortcuts import render, redirect
from .models import KitchenLunch, KitchenLate, TerminalLunch, TerminalLate, KitchenSpecialcleaningMonday, \
    DryStorageCleaning, WednesdayCleaning, ApartmentCleaning, KitchenLunchTask, KitchenLateTask


def department_shift_selection(request):
    if request.method == 'POST':

        selected_department = request.POST.get('department')
        selected_shift = request.POST.get('shift')
        selected_section = request.POST.get('section')
        selected_action=request.POST.get('action')

        if selected_department == 'kitchen' and selected_shift == 'lunch':
            if selected_action == 'quantity':
                return redirect('kitchen_lunch_form')# Corrected redirection
            elif selected_action== 'task':
                return redirect('kitchen_lunch_task')
        elif selected_department == 'kitchen' and selected_shift == 'late':
            if selected_action == 'quantity':
                return redirect('kitchen_late_form')
            elif selected_action== 'task':
                return redirect('kitchen_late_task')
        elif selected_department == 'terminal' and selected_shift == 'lunch':
            return redirect('terminal_lunch_form')
        elif selected_department == 'terminal' and selected_shift == 'late':
            return redirect('terminal_late_form')
        elif selected_department == 'kitchen' and selected_shift == 'specialcleaningmonday':
            return redirect('kitchen_specialcleaning_monday')
        elif selected_department == 'kitchen' and selected_shift == 'specialcleaningwednesday':
            if selected_section == 'kitchen':
                return redirect('wednesday_cleaning_kitchen')
            elif selected_section == 'dry_storage':
                return redirect('dry_storage_cleaning_form')
            elif selected_section == 'apartment':
                return redirect('apartment_cleaning_form')
        else:
            # If no conditions are met, re-render the form with an error message
            return render(request, 'pizza_ordering/department_selection.html', {
                'error_message': 'Invalid selection. Please try again.'
            })

    # Render the form if the request method is not POST
    return render(request, 'pizza_ordering/department_selection.html')

def kitchen_lunch_form(request):
    if request.method == 'POST':
        KitchenLunch.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],

            today_balls_total=request.POST['today_balls_total'],
            yesterday_balls_total=request.POST['yesterday_balls_total']
        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenlunch.html')
def kitchen_lunch_task(request):
    if request.method == 'POST':
        KitchenLunchTask.objects.create(
            date=request.POST['date'],
            name=request.POST['name'],
            location=request.POST['location'],

            task_kitchen_cleaned=request.POST['task_kitchen_cleaned'],
            task_enough_laundry=request.POST['task_enough_laundry'],
            comments=request.POST['comments'],

        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenlunchtask.html')

def kitchen_late_task(request):
    if request.method == 'POST':
        KitchenLateTask.objects.create(
            date=request.POST['date'],
            name=request.POST['name'],
            location=request.POST['location'],
            comments=request.POST['comments'],
            side=request.POST['side'],
            soap_WC_sufficient=request.POST['soap_WC_sufficient'],
            toilet_paper_WC_sufficient=request.POST['toilet_paper_WC_sufficient'],
            grease_remover_kitchen_sufficient=request.POST['grease_remover_kitchen_sufficient'],
            washingup_liquid_kitchen_sufficient=request.POST['washingup_liquid_kitchen_sufficient'],
            blue_roll_kitchen_sufficient=request.POST['blue_roll_kitchen_sufficient'],


        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenlatetask.html')

def kitchen_late_form(request):
    if request.method == 'POST':
        KitchenLate.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],

            pizza_grade=request.POST['pizza_grade'],
            tomorrow_balls_total=request.POST['tomorrow_balls_total'],
            old_balls_total=request.POST['old_balls_total'],
            balls_broken_today=request.POST['balls_broken_today'],
            pizzas_broken_today=request.POST['pizzas_broken_today']
        )
        return redirect(' ')
    return render(request, 'pizza_ordering/kitchenlate.html')
# from django.shortcuts import render, redirect
# from .models import KitchenLunch
def kitchen_specialcleaning_monday(request):
    if request.method == 'POST':
        KitchenSpecialcleaningMonday.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments']

        )
        return redirect('')
    return render(request, 'pizza_ordering/kitchenspecialcleaningmonday.html')


def terminal_lunch_form(request):
    if request.method == 'POST':
        TerminalLunch.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments']
        )
        return redirect('')
    return render(request, 'pizza_ordering/terminallunch.html')
def terminal_late_form(request):
    if request.method == 'POST':
        TerminalLate.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
            hallway_mopped=request.POST['hallway_mopped'],
            cellar_tidy=request.POST['cellar_tidy'],
            replenished=request.POST['replenished'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/terminallate.html')


def kitchen_late_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location=request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')


        pizza_grade = request.POST.get('pizza_grade')
        tomorrow_balls_total = request.POST.get('tomorrow_balls_total')
        old_balls_total = request.POST.get('old_balls_total')
        balls_broken_today = request.POST.get('balls_broken_today')
        pizzas_broken_today = request.POST.get('pizzas_broken_today')
        # Create a new instance of KitchenLunch model and save the data
        KitchenLate.objects.create(
            date=date,
            location=location,
            name=name,
            comments=comments,

            pizza_grade=pizza_grade,
            tomorrow_balls_total=tomorrow_balls_total,
            old_balls_total=old_balls_total,
            balls_broken_today=balls_broken_today ,
            pizzas_broken_today=pizzas_broken_today

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_late_dashboard')
    else:
        # Handle GET requests if needed
        pass

def kitchen_specialcleaning_monday_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        KitchenSpecialcleaningMonday.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_specialcleaning_monday_dashboard')
    else:
        # Handle GET requests if needed
        pass
def terminal_lunch_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        TerminalLunch.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('terminal_lunch_dashboard')
    else:
        # Handle GET requests if needed
        pass


def terminal_late_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')
        hallway_mopped=request.POST.get('hallway_mopped')
        cellar_tidy=request.POST.get('cellar_tidy')
        replenished=request.POST.get('replenished')

        TerminalLate.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,
            hallway_mopped=hallway_mopped,
            cellar_tidy=cellar_tidy,
            replenished=replenished,
        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('terminal_late_dashboard')
    else:
        # Handle GET requests if needed
        pass
from django.shortcuts import render, redirect
from .models import KitchenLunch


def kitchen_lunch_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        today_balls_total = request.POST.get('today_balls_total')
        yesterday_balls_total = request.POST.get('yesterday_balls_total')

        # Create a new instance of KitchenLunch model and save the data
        KitchenLunch.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

            today_balls_total=today_balls_total,
            yesterday_balls_total=yesterday_balls_total
        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_lunch_dashboard')
    else:
        # Handle GET requests if needed
        pass
def kitchen_lunch_task_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')

        task_kitchen_cleaned=request.POST.get('task_kitchen_cleaned')
        task_enough_laundry=request.POST.get('task_enough_laundry')
        comments = request.POST.get('comments')



        # Create a new instance of KitchenLunch model and save the data
        KitchenLunchTask.objects.create(
            date=date,
            name=name,
            location=location,

            task_kitchen_cleaned=task_kitchen_cleaned,
            task_enough_laundry=task_enough_laundry,
            comments=comments,


        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_lunch_task_dashboard')
    else:
        # Handle GET requests if needed
        pass

def kitchen_late_task_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')
        side= request.POST.get('side')
        soap_WC_sufficient= request.POST.get('soap_WC_sufficient')
        toilet_paper_WC_sufficient=request.POST.get('toilet_paper_WC_sufficient')
        grease_remover_kitchen_sufficient=request.POST.get('grease_remover_kitchen_sufficient')
        washingup_liquid_kitchen_sufficient=request.POST.get('washingup_liquid_kitchen_sufficient')
        blue_roll_kitchen_sufficient=request.POST.get('blue_roll_kitchen_sufficient')


        # Create a new instance of KitchenLunch model and save the data
        KitchenLateTask.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,
            side=side,
            soap_WC_sufficient=soap_WC_sufficient,
            toilet_paper_WC_sufficient=toilet_paper_WC_sufficient,
            grease_remover_kitchen_sufficient=grease_remover_kitchen_sufficient,
            washingup_liquid_kitchen_sufficient=washingup_liquid_kitchen_sufficient,
            blue_roll_kitchen_sufficient=blue_roll_kitchen_sufficient


        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('kitchen_late_task_dashboard')
    else:
        # Handle GET requests if needed
        pass
def kitchen_lunch_dashboard(request):
    kitchen_lunchs = KitchenLunch.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/kitchenlunchdashboard.html', {'kitchen_lunchs': kitchen_lunchs})
def kitchen_lunch_task_dashboard(request):
    kitchen_lunchs_task = KitchenLunchTask.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/kitchenlunchtaskdashboard.html', {'kitchen_lunchs_task': kitchen_lunchs_task})
from django.shortcuts import render
from .models import KitchenLunch

from django.shortcuts import render
from .models import KitchenLate

def kitchen_late_dashboard(request):
    kitchen_lates = KitchenLate.objects.all().order_by('-date')  # Fetch all KitchenLate objects from the database, ordered by date descending
    return render(request, 'pizza_ordering/kitchenlatedashboard.html', {'kitchen_lates': kitchen_lates})

def kitchen_late_task_dashboard(request):
    kitchen_lates_task = KitchenLateTask.objects.all().order_by('-date')  # Fetch all KitchenLunch objects from the database
    return render(request, 'pizza_ordering/kitchenlatetaskdashboard.html', {'kitchen_lates_task': kitchen_lates_task})

def terminal_lunch_dashboard(request):
    terminal_lunches = TerminalLunch.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/terminallunchdashboard.html', {'terminal_lunches': terminal_lunches})
def terminal_late_dashboard(request):
    terminal_lates = TerminalLate.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/terminallatedashboard.html', {'terminal_lates': terminal_lates})
def kitchen_specialcleaning_monday_dashboard(request):
    kitchen_specialcleanings_monday = KitchenSpecialcleaningMonday.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/kitchenspecialcleaningmondaydashboard.html', {'kitchen_specialcleanings_monday': kitchen_specialcleanings_monday})



def dry_storage_cleaning_form(request):
    if request.method == 'POST':
        DryStorageCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/drystoragecleaning.html')
def drystorage_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # Create a new instance of KitchenLunch model and save the data
        DryStorageCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('drystorage_cleaning_dashboard')
    else:
        # Handle GET requests if needed
        pass

def drystorage_cleaning_dashboard(request):
    dry_storage_cleanings_form = DryStorageCleaning.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/drystoragecleaningdashboard.html', {'dry_storage_cleanings_form': dry_storage_cleanings_form})

def wednesday_cleaning_kitchen(request):
    if request.method == 'POST':
        WednesdayCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/wednesdaycleaning.html')
def wednesday_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # Create a new instance of KitchenLunch model and save the data
        WednesdayCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('wednesday_cleaning_dashboard')
    else:
        # Handle GET requests if needed
        pass

def wednesday_cleaning_dashboard(request):
    wednesday_cleaning_kitchens = WednesdayCleaning.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/wednesdaycleaningdashboard.html', {'wednesday_cleaning_kitchens': wednesday_cleaning_kitchens})

def apartment_cleaning_form(request):
    if request.method == 'POST':
        ApartmentCleaning.objects.create(
            date=request.POST['date'],
            location=request.POST['location'],
            name=request.POST['name'],
            comments=request.POST['comments'],
        )
        return redirect('')
    return render(request, 'pizza_ordering/apartmentcleaning.html')
def apartment_cleaning_submit(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        location = request.POST.get('location')
        name = request.POST.get('name')
        comments = request.POST.get('comments')

        # Create a new instance of KitchenLunch model and save the data
        ApartmentCleaning.objects.create(
            date=date,
            name=name,
            location=location,
            comments=comments,

        )

        # Redirect to the kitchenlunchdashboard.html page
        return redirect('apartment_cleaning_dashboard')
    else:
        # Handle GET requests if needed
        pass

def apartment_cleaning_dashboard(request):
    apartment_cleaning_forms = ApartmentCleaning.objects.all().order_by('-date')
    return render(request, 'pizza_ordering/apartmentcleaningdashboard.html', {'apartment_cleaning_forms': apartment_cleaning_forms})

