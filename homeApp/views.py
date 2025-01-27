from django.shortcuts import render,HttpResponse



# Create your views here.
def index(request):
    # we create variables of the data saved in our database and then send it to the template
    # (we dont it like this, just an example) context is the set of varibles, sent to the template
    context ={
        'variable1' : "DB Project",
        'variable2' : "Abdul Wasay"
        
    }
#    return HttpResponse("This is Homepage")
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("This is About Page")


def services(request):
    return HttpResponse("This is Services Page")


# def contact(request):
#     return HttpResponse("This is Contact Page")





def payment(request):
    return HttpResponse("This is Payment Page")

def personal_info(request):
    return HttpResponse("This is Personal Info Page")

def contact_dev(request):
    return render(request, 'ContactDevPage.html')



from django.shortcuts import redirect
from .models import Member
from django.contrib import messages


# **********************************  MEMBERS ************************************
def add_member(request):
    if request.method == "POST":
        # Get form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        join_date = request.POST.get('join_date')
        dob = request.POST.get('dob')
        status = request.POST.get('status')

        # Create and save the Member object
        try:
            new_member = Member(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                join_date=join_date,
                dob=dob,
                status=status
            )
            new_member.save()
            messages.success(request, "Member added successfully!")

            print(f'{first_name}--{last_name}--{email}--{phone}')
            
            return redirect('add_member')  # Redirect to the same page
        except Exception as e:
            messages.error(request, f"Error: {e}")
    
    return render(request, 'AddMember.html')




def view_members(request):
    members = Member.objects.all()  # Fetch all members from the database
    return render(request, 'ViewMembers.html', {'members': members})



def edit_member(request, member_id):
    member = Member.objects.get(member_id=member_id)

    if request.method == 'POST':
        member.first_name = request.POST['first_name']
        member.last_name = request.POST['last_name']
        member.email = request.POST['email']
        member.phone = request.POST['phone']
        member.address = request.POST['address']
        member.join_date = request.POST['join_date']
        member.dob = request.POST['dob']
        member.status = request.POST['status']
        member.save()
        messages.success(request, "Member updated successfully!")
        return redirect('view_members')

    return render(request, 'EditMember.html', {'member': member})



def delete_member(request, member_id):
    member = Member.objects.get(member_id=member_id)
    member.delete()
    messages.success(request, "Member deleted successfully!")
    return redirect('view_members')




# *********************************** Memberships *************************************

# def membership(request):
#     return HttpResponse("This is membership Page")

# from django.shortcuts import render, redirect, get_object_or_404
# from django.utils import timezone
# from .models import Member, Plan, Membership
# from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from .models import Member, Plan, Membership
from datetime import timedelta

def assign_membership(request):
    if request.method == "POST":
        # Get the member_id and plan_id from the POST request
        member_id = request.POST.get("member_id")
        plan_id = request.POST.get("plan_id")
        
        try:
            # Convert the IDs to integers (they might be strings from the form)
            member_id = int(member_id)
            plan_id = int(plan_id)

            # Fetch Member and Plan objects by their IDs
            member = get_object_or_404(Member, member_id=member_id)
            plan = get_object_or_404(Plan, plan_id=plan_id)
            
            # Set the start_date (current date and time)
            start_date = timezone.now().date()
            
            # Calculate the end_date (1 year from the start_date)
            end_date = start_date + timedelta(days=365)  # Adjust duration as per your plan's rules
            
            # Create a new Membership object
            new_membership = Membership(
                member=member,
                plan=plan,
                start_date=start_date,
                end_date=end_date,
                status="Active"  # Adjust status as needed (Active, Inactive, etc.)
            )
            new_membership.save()  # Save to the database

            # Success message after assignment
            messages.success(request, f"Membership for {member.first_name} {member.last_name} has been assigned successfully!")

            # Redirect to the dashboard or another page after success
            return redirect("dashboard")  # Change this if needed to the relevant view

        except ValueError:
            # Handle invalid member_id or plan_id input
            messages.error(request, "Invalid data provided. Please ensure valid member and plan IDs.")
        except Exception as e:
            # Handle error and display the error message
            messages.error(request, f"Error: {e}")

    # If it's a GET request, provide members and plans for dropdowns
    members = Member.objects.all()
    plans = Plan.objects.all()

    return render(request, "AssignMembership.html", {"members": members, "plans": plans})


# def view_memberships(request):
#     memberships = Membership.objects.all()  # Fetch all memberships from the database
#     return render(request, 'ViewMemberships.html', {'memberships': memberships})



# def edit_membership(request, membership_id):
#     membership = get_object_or_404(Membership, membership_id=membership_id)

#     if request.method == 'POST':
#         # Update membership fields
#         membership.plan = request.POST['plan']  # You might need to map the plan correctly
#         membership.start_date = request.POST['start_date']
#         membership.end_date = request.POST['end_date']
#         membership.status = request.POST['status']
#         membership.save()
        
#         messages.success(request, "Membership updated successfully!")
#         return redirect('view_memberships')

#     return render(request, 'EditMembership.html', {'membership': membership})



# def delete_membership(request, membership_id):
#     membership = get_object_or_404(Membership, membership_id=membership_id)
#     membership.delete()
#     messages.success(request, "Membership deleted successfully!")
#     return redirect('view_memberships')


# View all memberships
def view_memberships(request):
    memberships = Membership.objects.all()  # Fetch all memberships from the database
    return render(request, 'ViewMemberships.html', {'memberships': memberships})

# Edit membership
from django.shortcuts import get_object_or_404

# Edit membership
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Membership, Plan, Billing

#                       *****************muneeb***********************************
# edit
def edit_membership(request, membership_id):
    try:
        # Fetch the membership object using membership_id
        membership = Membership.objects.get(membership_id=membership_id)
        # Fetch all available plans
        plans = Plan.objects.all()

        if request.method == 'POST':
            # Update membership details
            membership.plan = get_object_or_404(Plan, plan_id=request.POST['plan'])
            membership.start_date = request.POST['start_date']
            membership.end_date = request.POST['end_date']
            membership.status = request.POST['status']
            membership.save()

            # Update payment status to "Unpaid" when membership is updated
            # Find the billing record for the membership and set its status to "Unpaid"
            billing = Billing.objects.filter(membership=membership).last()
            if billing:
                billing.payment_status = 'Unpaid'
                billing.save()

            # Redirect with a success message
            messages.success(request, 'Membership updated successfully! Payment status set to Unpaid.')
            return redirect('view_memberships')

        # Pass membership and plans to the template
        return render(request, 'EditMembership.html', {
            'membership': membership,
            'plans': plans,
        })

    except Membership.DoesNotExist:
        # Handle case where membership does not exist
        messages.error(request, 'Membership not found.')
        return redirect('view_memberships')


# Delete membership
def delete_membership(request, membership_id):
    membership = Membership.objects.get(id=membership_id)
    membership.delete()
    messages.success(request, "Membership deleted successfully!")
    return redirect('view_memberships')





# ************************** Trainer ********************************

from django.shortcuts import render, redirect
from .models import Trainer, TrainerSpeciality

def add_trainer(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        status = request.POST['status']
        speciality = request.POST['speciality']

        # Save the trainer details
        trainer = Trainer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            status=status
        )

        # Save the specialty for the trainer
        TrainerSpeciality.objects.create(
            trainer=trainer,
            specialty=speciality
        )

        return redirect('view_trainers')  # Redirect to the trainers' list after adding

    return render(request, 'AddTrainer.html')

from django.shortcuts import render, redirect, get_object_or_404

def view_trainers(request):
    # Use select_related to fetch related TrainerSpeciality in a single query
    trainers = Trainer.objects.all()
    # trainer_data = []

    # for trainer in trainers:
    #     trainer_data.append({
    #         'trainer': trainer,
    #         'speciality': trainer.trainerspeciality.speciality if hasattr(trainer, 'trainerspeciality') else "Not Assigned"
    #     })
    
    # print(trainers)

    return render(request, 'ViewTrainers.html', {'trainer_data': trainers})





def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, trainer_id=trainer_id)
    if request.method == "POST":
        trainer.first_name = request.POST['first_name']
        trainer.last_name = request.POST['last_name']
        trainer.email = request.POST['email']
        trainer.phone = request.POST['phone']
        trainer.status = request.POST['status']
        trainer.save()
        return redirect('view_trainers')
    return render(request, 'EditTrainer.html', {'trainer': trainer})


def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, trainer_id=trainer_id)
    trainer.delete()
    return redirect('view_trainers')



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Trainer, Member, TrainerAssignment

def assign_trainer(request):
    if request.method == "POST":
        member_id = request.POST.get("member")
        trainer_id = request.POST.get("trainer")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        member = get_object_or_404(Member, pk=member_id)
        trainer = get_object_or_404(Trainer, pk=trainer_id)

        # Create and save the trainer assignment
        TrainerAssignment.objects.create(
            member=member,
            trainer=trainer,
            start_date=start_date,
            end_date=end_date,
        )

        messages.success(request, f"Trainer {trainer} successfully assigned to {member}.")
        return redirect("assign_trainer")

    members = Member.objects.all()
    trainers = Trainer.objects.all()
    return render(request, "AssignTrainer.html", {"members": members, "trainers": trainers})


from .models import TrainerAssignment
from django.shortcuts import render
from .models import Trainer, TrainerAssignment
from django.shortcuts import render
from .models import TrainerAssignment

def view_trainer_assignments(request):
    # Fetch all trainer assignments
    assignments = TrainerAssignment.objects.select_related('trainer', 'member')
    return render(request, 'ViewTrainerAssignments.html', {'assignments': assignments})

# ******************************** Plans *****************************************


from .models import Plan

def add_plan(request):
    if request.method == "POST":
        # Get form data from POST request
        plan_name = request.POST.get('plan_name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        duration_months = request.POST.get('duration_months')

        # Create and save the Plan object
        Plan.objects.create(
            plan_name=plan_name,
            description=description,
            price=price,
            duration_months=duration_months
        )

        messages.success(request, "Plan added successfully!")
        return redirect('add_plan')  # Redirect to the same page
    
    return render(request, 'AddPlan.html')


def view_plans(request):
    plans = Plan.objects.all()  # Fetch all plans from the database
    return render(request, 'ViewPlans.html', {'plans': plans})


def edit_plan(request, plan_id):
    plan = get_object_or_404(Plan, plan_id=plan_id)

    if request.method == 'POST':
        plan.plan_name = request.POST['plan_name']
        plan.description = request.POST['description']
        plan.price = request.POST['price']
        plan.duration_months = request.POST['duration_months']
        plan.save()
        messages.success(request, "Plan updated successfully!")
        return redirect('view_plans')

    return render(request, 'EditPlan.html', {'plan': plan})


def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, plan_id=plan_id)
    plan.delete()
    messages.success(request, "Plan deleted successfully!")
    return redirect('view_plans')


# ******************************* BILLING *************************************
# ******************************** MUNEEB ***************************************************************

from django.shortcuts import render
from .models import Membership, Billing
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils import timezone
from decimal import Decimal
from .models import Billing, Membership


from django.shortcuts import render
from .models import Membership, Billing
from decimal import Decimal

def payment_page(request):
    # Fetch all memberships with related member and plan
    memberships = Membership.objects.select_related('member', 'plan')
    payment_data = []

    search_term = request.GET.get('search', '').lower()  # Get search term from query params

    for membership in memberships:
        # Fetch latest billing record if it exists
        billing = Billing.objects.filter(membership=membership).last()
        additional_charges = Decimal('0.00')  # Initialize to 0, as it's manually entered
        total_amount = membership.plan.price
        plan_amount = membership.plan.price  # This is the plan amount to display separately

        if billing:
            additional_charges = billing.additional_charges  # Use the saved additional charges
            total_amount += additional_charges
            payment_status = billing.payment_status
        else:
            payment_status = 'Unpaid'

        payment_data.append({
            'member_id': membership.member.member_id,
            'member_name': f"{membership.member.first_name} {membership.member.last_name}",
            'plan_name': membership.plan.plan_name,
            'plan_amount': plan_amount,  # Plan Amount
            'total_amount': total_amount,
            'additional_charges': additional_charges,  # Show the additional charges
            'payment_status': payment_status,
        })

    # Filter payment data based on search term
    if search_term:
        payment_data = [
            data for data in payment_data
            if search_term in data['member_name'].lower() or
               search_term in data['plan_name'].lower() or
               search_term in data['payment_status'].lower()
        ]

    context = {'payment_data': payment_data}
    return render(request, 'PaymentPage.html', context)



from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.timezone import now
from decimal import Decimal
from .models import Billing, Membership


def process_payment(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        additional_charges = request.POST.get('additional_charges', '0.00')

        try:
            member_id = int(member_id)
            additional_charges = Decimal(additional_charges)
        except ValueError:
            messages.error(request, 'Invalid input values.')
            return redirect('payment_page')

        membership = Membership.objects.filter(member_id=member_id).first()
        if membership:
            # Calculate total payment amount
            total_amount = membership.plan.price + additional_charges

            # Fetch or create the latest billing record
            billing, created = Billing.objects.get_or_create(
                membership=membership,
                payment_status='Unpaid',  # Pay only if previously unpaid
                defaults={
                    'amount': total_amount,
                    'additional_charges': additional_charges,
                    'billing_date': now(),
                },
            )
            if not created:
                billing.amount = total_amount
                billing.additional_charges = additional_charges
                billing.billing_date = now()
                billing.payment_status = 'Paid'  # Mark payment as successful
                billing.save()

            messages.success(request, 'Payment processed successfully!')
        else:
            messages.error(request, 'Membership not found.')

    return redirect('payment_page')




# ***************************** Graphical Insight *************************
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for rendering plots


import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64
from django.db.models import Count
from django.shortcuts import render
from .models import Membership, Plan

def plans_pie_chart():
    # Fetch data about plans and their counts
    plan_data = (
        Membership.objects.values('plan__plan_name')
        .annotate(plan_count=Count('plan'))
        .order_by('-plan_count')
    )

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(list(plan_data))
    labels = df['plan__plan_name']
    sizes = df['plan_count']

    # Create a Pie Chart
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Plans Distribution Among Memberships')
    plt.tight_layout()

    # Save plot to a BytesIO stream and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()
    return image_base64




from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Billing

def monthly_revenue_chart():
    # Fetch and aggregate billing data
    revenue_data = (
        Billing.objects.annotate(month=TruncMonth('billing_date'))
        .values('month')
        .annotate(total_revenue=Sum('amount') + Sum('additional_charges'))
        .order_by('month')
    )

    # Load data into a Pandas DataFrame
    df = pd.DataFrame(list(revenue_data))
    df['month'] = pd.to_datetime(df['month'])
    df = df.sort_values(by='month')

    # Generate Bar Chart
    plt.figure(figsize=(10, 6))
    plt.bar(df['month'].dt.strftime('%B %Y'), df['total_revenue'], color='skyblue')
    plt.title('Monthly Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue (USD)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save plot to a BytesIO stream and encode as base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()
    return image_base64




from .models import TrainerAssignment, Trainer

def trainer_assignments_chart():
    trainer_data = (
        TrainerAssignment.objects.values(
            'trainer__first_name', 'trainer__last_name'
        )
        .annotate(member_count=Count('member'))
        .order_by('-member_count')
    )

    df = pd.DataFrame(list(trainer_data))
    df['trainer'] = df['trainer__first_name'] + ' ' + df['trainer__last_name']
    df = df.sort_values(by='member_count', ascending=False)

    plt.figure(figsize=(10, 6))
    plt.bar(df['trainer'], df['member_count'], color='orange')
    plt.title('Trainer Assignments')
    plt.xlabel('Trainer')
    plt.ylabel('Number of Members Assigned')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()
    return image_base64




def graphs_page(request):
    # Generate graphs as base64 strings
    pie_chart = plans_pie_chart()
    bar_chart_revenue = monthly_revenue_chart()
    bar_chart_trainers = trainer_assignments_chart()

    # Pass the base64-encoded images to the template
    return render(request, 'Graphs.html', {
        'pie_chart': pie_chart,
        'bar_chart_revenue': bar_chart_revenue,
        'bar_chart_trainers': bar_chart_trainers,
    })




# *********************************************** Login *****************************************

# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# View for login
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f"Attempting to authenticate: {username}, {password}")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to the dashboard after successful login
        else:
            return HttpResponse("Invalid credentials, please try again.")  # Invalid login attempt

    return render(request, 'login.html')  # Render the login page template if it's a GET request

# Dashboard view (protected view)
@login_required
def dashboard(request):
    username = request.user.username  # Fetch logged-in user's username
    return render(request, 'dashboard.html', {'username': username})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with your login URL name





# ****************************************** dashboard functionalities *****************************************

from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime, timedelta
from .models import Member, Membership, Trainer, Billing
from django.utils.timezone import now


def dashboard(request):
    # Total number of members
    total_members = Member.objects.count()

    # Number of active memberships
    active_memberships = Membership.objects.filter(status='Active').count()

    # Revenue calculations for the current month, quarter, and year
    current_date = datetime.now()
    current_month = current_date.month
    current_year = current_date.year
    current_quarter_start_month = 3 * ((current_month - 1) // 3) + 1

    # Revenue for the current month
    revenue_current_month = Billing.objects.filter(
        billing_date__month=current_month,
        billing_date__year=current_year
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    # Revenue for the current quarter
    revenue_current_quarter = Billing.objects.filter(
        billing_date__month__gte=current_quarter_start_month,
        billing_date__month__lt=current_quarter_start_month + 3,
        billing_date__year=current_year
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    # Revenue for the current year
    revenue_current_year = Billing.objects.filter(
        billing_date__year=current_year
    ).aggregate(Sum('amount'))['amount__sum'] or 0

    # Number of trainers
    total_trainers = Trainer.objects.count()

    # Expiring memberships (next 7 days)
    expiring_memberships = Membership.objects.filter(
        end_date__range=[current_date.date(), current_date.date() + timedelta(days=7)],
        status='Active'
    )

    # Automatically update pending payments to unpaid if billing date has passed
    Billing.objects.filter(
        payment_status='Pending',
        billing_date__lt=now().date()
    ).update(payment_status='Unpaid')

    # Pending payments (including newly updated unpaid)
    pending_payments = Billing.objects.filter(payment_status='Unpaid')

    # Context data to pass to the template
    context = {
        'total_members': total_members,
        'active_memberships': active_memberships,
        'revenue_current_month': revenue_current_month,
        'revenue_current_quarter': revenue_current_quarter,
        'revenue_current_year': revenue_current_year,
        'total_trainers': total_trainers,
        'expiring_memberships': expiring_memberships,
        'pending_payments': pending_payments,
    }

    return render(request, 'dashboard.html', context)








