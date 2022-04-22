from curses.ascii import HT
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  # add this
from .utils import sendEmail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token  
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.contrib.auth import get_user_model

def index(request):
    data =  {
        'nbar': 'home'
    }
    return render(request, "home/home.html", data)


def register_request(request):    
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == "POST":
        form = NewUserForm(request.POST)        
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False              
            user.save()
            current_site = get_current_site(request)
            domain = current_site.domain
            html_message = render_to_string('email/verify_email.html', { 'username': user.username,  'domain' : domain, 'uid':urlsafe_base64_encode(force_bytes(user.pk)), 'token':account_activation_token.make_token(user) })
            is_sent = sendEmail(html_message, 'Verification Email', user.email)
            if is_sent:
                messages.success(request, "Registration successful. We have sent you email for the confirmation.", extra_tags="alert-success")
                return redirect("login")
            else:
                messages.success(request, "Registration successful. We have sent you email for the confirmation.", extra_tags="alert-success")
                return HttpResponseRedirect("login")            
        # else:
        #     return HttpResponse([form.errors])
    else: 
        form = NewUserForm()
    return render(request=request, template_name="home/register.html", context={"register_form": form})


def login_request(request):
    if request.user.is_authenticated:
        return redirect('/')

    elif request.method == 'POST':        
        if 'username' in request.POST and 'password' in request.POST:
            username = request.POST['username'].strip()
            password = request.POST['password'].strip()
            if len(username) == 0 or len(password) == 0:
                messages.error(request, 'Invalid request made.', extra_tags='alert-danger')
                return redirect('login')
            else:
                user = authenticate(
                    request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Welcome to Medy App :)', extra_tags='alert-success')
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid Username or Password', extra_tags='alert-danger')    
                    return redirect('login')
        else:
            messages.error(request, 'Invalid request made.', extra_tags='alert-danger')    
            return redirect('login')
    else:
        data = {}
        data['javascripts'] = ['scripts/login.js']
        return render(request, 'home/login.html', data)

def logout_request(request):
    logout(request)
    return redirect('/login')

def test(request):
    html_message = render_to_string('email/test.html', { 'username': 'kishan' })
    t = sendEmail(html_message, 'subject', 'ksmistry1991@gmail.com')    
    return HttpResponse(t)

def activate(request, uidb64, token):
    User = get_user_model() 
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.', extra_tags='alert-success')        
    else:  
        messages.error(request, 'Activation link is invalid!', extra_tags='alert-danger')        
    return redirect('/login')