from django.shortcuts import render, redirect
import re
from users.forms import UserAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .page_speed_api import get_data
import json

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
    return redirect('home')

@login_required(login_url='home')
def dashboard(request):
    search_url = ''
    err_msg = None
    reports = request.user.report.all()
    if request.method == 'POST':
        search_url = request.POST['search']
        string = re.match('(?i)(url:|origin:)?http(s)?://.*', search_url)

        if not string:
            err_msg = "Urls must match the following example http(s)://example.com/"
            context = {'err_msg': err_msg, "search": search_url}
            return render(request, 'reportApp/dashboard.html', context)
        elif reports.filter(report_id=search_url):
            report = reports.filter(report_id=search_url)[0]
            data = json.loads(report.report_data)
            r_id = request.user.report.all().filter(report_id=data["id"])[0].id
            return redirect('report', r_id)
        else:
            data = get_data(search_url)
            if data["error"]:
                err_msg = "Unable to get the data for" + search_url
                data = None
            else:
                str_report_data = json.dumps(data)
                reportObj = request.user.report.create(user=request.user, report_id=data["id"], report_data=str_report_data)
                reportObj.save()
            r_id = request.user.report.all().filter(report_id=data["id"])[0].id
            return redirect('report', r_id)

        context = {'err_msg': err_msg, 'data': data, 'search':search_url, 'reports': reports}
        return render(request, 'reportApp/dashboard.html', context)

    context = {'search': search_url, 'reports': reports}
    return render(request, 'reportApp/dashboard.html', context)


@login_required(login_url='home')
def report(request, pk):
    reports = request.user.report.all().filter(id=pk)
    data = None
    if reports:
        data = json.loads(reports[0].report_data)
        context = {'data': data}
    return render(request, 'reportApp/report.html', context)


@login_required(login_url='home')
def regenerate(request, pk):
    reports = request.user.report.all().filter(id=pk)
    if (reports):
        search_url = reports[0].report_id
        print(search_url)
        data = get_data(search_url)

        str_report_data = json.dumps(data)

        reportObj = reports[0]
        reportObj.report_data=str_report_data
        reportObj.save()

        context={"data": data}
    return render(request, 'reportApp/report.html', context)