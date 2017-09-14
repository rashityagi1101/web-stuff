


# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from homepage.forms import UserForm,FarmerForm,RetailerForm,SellForm,FComplainForm,RComplainForm,R_ad_post_Form,ad_form
from django.contrib.auth import login as auth_login

from .models import farmer,retailer,fcomplain,r_ad_details,sell,rcomplain



def index(request):
    return render(request, "homepage/index.html",context_instance=RequestContext(request))
def registerpage(request):
    return render(request, "homepage/registerpage.html",context_instance=RequestContext(request))

def material(request):
    return render(request, "homepage/material.html",context_instance=RequestContext(request))
def farmerr(request):
    return render(request, "homepage/farmer.html",context_instance=RequestContext(request))
def loginpage(request):
    return render(request, "homepage/loginpage.html",context_instance=RequestContext(request))


# def logout(request):
#     form = UserForm(request.POST or None)
#     context = {
#         "form": form,
#     }
#     return render(request, 'homepage/login.html', context)


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmers = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/farmer_dash.html', {'farmers': farmers})
            else:
                return render(request, 'homepage/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/login.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/login.html')

def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                retailers = retailer.objects.filter(user=request.user)
                return render(request, 'homepage/retailer_dash.html', {'retailers': retailers})
            else:
                return render(request, 'homepage/login1.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'homepage/login1.html', {'error_message': 'Invalid login'})
    return render(request, 'homepage/login1.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmers = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/create_farmer_extra.html', {'farmers': farmers})
    context = {
        "form": form,
    }
    return render(request, 'homepage/register.html', context)


def register1(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                farmers = farmer.objects.filter(user=request.user)
                return render(request, 'homepage/create_retailer_extra.html', {'farmers': farmers})
    context = {
        "form": form,
    }
    return render(request, 'homepage/register1.html', context)






def create_farmer(request):
    if not request.user.is_authenticated():
        return render(request,'homepage/login.html')
    else:
        form= FarmerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            farmer_details=form.save(commit=False)
            farmer_details.user=request.user
            farmer_details.save();
            return render(request, 'homepage/farmer_dash.html',{'farmer_details':farmer_details})
        context = {
                "form": form,
            }

        return render(request, 'homepage/create_farmer.html', context)


def create_retailer(request):
    if not request.user.is_authenticated():
        return render(request,'homepage/login.html')
    else:
        form= RetailerForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            retailer_details=form.save(commit=False)
            retailer_details.user = request.user
            retailer_details.save();
            return render(request, 'homepage/retailer_dash.html' , {'retailer_details':retailer_details})
        context = {
                "form": form,
            }
        return render(request, 'homepage/create_retailer.html', context)


def sell_crop(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        form = SellForm(request.POST or None, request.FILES or None)
        form1 = ad_form(request.POST or None, request.FILES or None)

        if form.is_valid() and form1.is_valid():
            sell_details = form.save(commit=False)
            sell_details.user = request.user
            sell_details.save();

            ad_details = form1.save(commit=False)
            ad_details.user = request.user
            ad_details.save();
            return render(request, 'homepage/farmer_dash.html', {'sell_details': sell_details , 'ad_details':ad_details})
        context = {
            "form": form,
            "form1": form1,
        }
        return render(request, 'homepage/sell_crop.html', context)


def farmer_dash(request):
    args = {'user': request.user}
    return render(request,'homepage/farmer_dash.html',args)

def retailer_dash(request):
    args = {'user': request.user}
    return render(request, 'homepage/retailer_dash.html', args)

        #return render(request, "homepage/farmer_dash.html", context_instance=RequestContext(request))


def complain(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        form = FComplainForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            fcomplain_details = form.save(commit=False)
            fcomplain_details.user = request.user
            fcomplain_details.save();
            return render(request, 'homepage/farmer_dash.html', {'fcomplain_details': fcomplain_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/complain.html', context)

def rtcomplain(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        form = RComplainForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            rcomplain_details = form.save(commit=False)
            rcomplain_details.user = request.user
            rcomplain_details.save();
            return render(request, 'homepage/retailer_dash.html', {'rcomplain_details': rcomplain_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/rcomplain.html', context)


def create_farmer_extra(request):
    return render(request, "homepage/create_farmer_extra.html",context_instance=RequestContext(request))


def create_retailer_extra(request):
    return render(request, "homepage/create_retailer_extra.html",context_instance=RequestContext(request))

def complain_page(request):
    return render(request, "homepage/complain_page.html",context_instance=RequestContext(request))

def ret_complain_page(request):
    return render(request, "homepage/ret_complain_page.html",context_instance=RequestContext(request))

def cmp_status_farmer(request):

    #args1 = {'user': request.user }
    #posts = fcomplain.objects.get(user=request.user)
    posts = fcomplain.objects.filter(user=request.user);
    args1 = {'posts': posts }
    #posts = get_object_or_404(fcomplain,user=request.user)
    #print(posts)
    return render(request, 'homepage/cmp_status_farmer.html', args1)

def cmp_status_retailer(request):

    #args1 = {'user': request.user }
    #posts = fcomplain.objects.get(user=request.user)
    posts = rcomplain.objects.filter(user=request.user);
    args1 = {'posts': posts }
    #posts = get_object_or_404(fcomplain,user=request.user)
    #print(posts)
    return render(request, 'homepage/cmp_status_retailer.html', args1)


def crop_details_farmer(request):
    posts = r_ad_details.objects.all();
    args = {'posts': posts }
    return render(request, 'homepage/crop_ad_details.html', args)

def crop_ad_posted(request):
    if not request.user.is_authenticated():
        return render(request, 'homepage/login.html')
    else:
        form = R_ad_post_Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            postad_details = form.save(commit=False)
            postad_details.user = request.user
            postad_details.save();
            return render(request, 'homepage/retailer_dash.html', {'postad_details': postad_details})
        context = {
            "form": form,
        }
        return render(request, 'homepage/crop_ad_details_post.html', context)

def response_recv(request):
    print(request.user)

    #lol = r_ad_details.objects.all().first();
    #lol1 = r_ad_details.objects.filter(user=lol.user);
    #posts = sell.objects.filter(retailer_details=lol.retailer_details);
    posts = sell.objects.filter(retailer_details=request.user);
    args = {'posts': posts}
    return render(request, 'homepage/response_recv.html', args)


def retailerlogoutt(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/login1.html', context)


def farmerlogoutt(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'homepage/login.html', context)










