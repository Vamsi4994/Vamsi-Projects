from django.shortcuts import render, redirect
from django.http import HttpResponse
from app_users.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def Home(request):
    return render(request, 'Home.html')
def Login(request):
    return render(request, 'Login.html')
def Signup(request):
    return render(request, 'Signup.html')
def Aboutus(request):
    return render(request, 'Aboutus.html')
def Contactus(request):
    return render(request, 'Contactus.html')


def register_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            return render(request, 'Signuperror.html', {
                'error_message': 'Email already registered. Please use a different email.'
            })
        try:
            user = User.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                gender=request.POST.get('gender'),
                date_of_birth=request.POST.get('date_of_birth'),
                email=request.POST.get('email'),
                mobile_number=request.POST.get('mobile_number'),
                password=make_password(request.POST.get('password')),
                higher_education_degree=request.POST.get('higher_education_degree'),
                higher_education_branch=request.POST.get('higher_education_branch'),
                higher_education_year_of_passout=int(request.POST.get('higher_education_year_of_passout') or 0),
                experience=int(request.POST.get('experience') or 0),
                location=request.POST.get('location'),
                zipcode=request.POST.get('zipcode'),
                usertype=request.POST.get('usertype'),
                company_name=request.POST.get('company_name') if request.POST.get('usertype') in ['Recruiter', 'Employee'] else None,
                company_address=request.POST.get('company_address') if request.POST.get('usertype') in ['Recruiter', 'Employee'] else None,
                resume=request.FILES.get('resume')
            )
            return redirect('Signupsucess')  # Change to your actual URL name
        except Exception as e:
            return render(request, 'Signuperror.html', {
                'error_message': f'Something went wrong: {str(e)}'
            })

    return render(request, 'Signup.html')



def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        print("Email entered:", email)
        print("Password entered:", password)

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                # Store user in session
                request.session['user_id'] = user.user_id
                request.session['user_type'] = user.usertype
                request.session['user_name'] = f"{user.first_name} {user.last_name}"
                return redirect('Dashboard')  # Redirect to dashboard or home page
            else:
                messages.error(request, 'Invalid password.')
        except User.DoesNotExist:
            messages.error(request, 'Email not found.')

    return render(request, 'Login.html')

def Dashboard(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(user_id=user_id)
        return render(request, 'Dashboard.html', {'user': user})
    return redirect('Login')

def logout_user(request):
    request.session.flush()  # Clear session
    return redirect('Login')