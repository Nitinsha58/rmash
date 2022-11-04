from django.shortcuts import render, redirect
import re
from  users.forms import UserAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .page_speed_api import get_data

# Create your views here.

def index(request):
    form =  UserAuthenticationForm()

    if request.method == 'POST':
        form = UserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.user_cache)
            redirect('home')
        else: 
            redirect('home')
    context = {'form':  form}
    return render(request, 'reportApp/home.html', context)

@login_required(login_url='home')
def logout_user(request):
    logout(request)
    # messages.info(request, 'You logged out successfully')
    return redirect('home')

@login_required(login_url='home')
def dashboard(request):

    search_url = ''
    if request.method == 'POST':
        search_url = request.POST['search']
        string = re.match('(?i)(url:|origin:)?http(s)?://.*', search_url)
        if not string:
            err_msg = "Urls must match the following example http(s)://example.com/"
            context = {'err_msg': err_msg, "search": search_url}
            return render(request, 'reportApp/dashboard.html', context)
        else:
            data = get_data(search_url)
            if data["error"]:
                err_msg = "Unable to get the data for " + search_url
                data = None
            else:
                err_msg = None
            context = {'err_msg': err_msg, 'data': data, 'search':search_url}
            return render(request, 'reportApp/dashboard.html', context)


    context = {'search': search_url}
    return render(request, 'reportApp/dashboard.html', context)