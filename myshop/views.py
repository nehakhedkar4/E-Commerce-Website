from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm,AddressForm
from django.contrib.auth import authenticate,login,logout
from .models import Product,customer,Cart
from django.views import View
from django.views.generic.edit import CreateView,DeleteView,UpdateView


# SIGNUP 
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        print(email)
        ps1 = request.POST['password1']
        ps2 = request.POST['password2']
        print(username,ps1,ps2)
        print("going to check conditions")
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username already taken!!')
            return redirect('/signup/')
        elif User.objects.filter(email=email).exists():
            print("in email elif")
            print("email taken")
            messages.info(request,'Email already taken!!')
            return redirect('/signup/')
        elif ps1 != ps2:
            messages.info(request,'Password does not match!')
            return redirect('/signup/')
        reg = User.objects.create_user(username=username,email=email,password=ps2)
        reg.save()
        messages.info(request,'Account Created Sunccessfully!!')
    fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})


# LOGIN PAGE
def user_login(request):
    if request.method == 'POST':
        # username = request.POST['username']
        username = request.POST['username']
        ps = request.POST['password']
        user = authenticate(request,username=username,password=ps)
        if user is not None:
            print(user)
            login(request, user)
            return redirect('home')
            # return HttpResponse("you are logged in")
        print(user)
        messages.info(request,'Invalid User')
        return redirect('/login/')
    return render(request,'login.html')

# HOME PAGE
class HomeView(View):
    def get(self,request):
        fashion = Product.objects.filter(category='F')
        print(fashion, "---------------------------------------------------------------")
        today_deals = Product.objects.filter(category='TD')
        return render(request,'home_page.html',{'fashion': fashion,'Today_deals': today_deals})

def index(request):
    form = AddressForm()
    return render(request,'index.html',{'form':form})

# PRODUCT DETAILS PAGE
class ProductDetailView(View):
    def get(self,request,pk):
        product_detail = Product.objects.filter(pk=pk)
        return render(request,'product_detail.html',{'product_detail' : product_detail})

# def mobile(request,data=None):
#     if data == 'Mi' or data == 'Realme' or data == 'Samsung':
#         mobiles = Product.objects.filter(category='M').filter(brand=data)
#     return render(request,'mobile.html',{'mobiles' : mobiles})

# def mobile(request):
#     return render(request,'mobile.html')

# class MobilView(View):
#     def get(self,request,data=None):
#         print(data,"************************************************************************")
#         if data == 'Mi' or data == 'Realme' or data == 'Samsung':
#             print(data)
#             mobiles = Product.objects.filter(category='M').filter(brand=data)
#             print(mobiles,"mobiles============================================================")
#         return render(request,'mobile.html',{'mobiles' : mobiles})
        

# ADD_TO_CART PAGE
class AddToCartView(View):
    def get(self,request,pk):
        # print("inside addtocart-------------------------------------------------------------------",pk )
        user = request.user
        cart_details = Product.objects.filter(pk=pk)
        product = Product.objects.get(id=pk)
        print(product)
        # Cart(user=user,product=product).save()
        # cart_details = Cart.objects.all()
        return render(request,'addToCart.html',{'cart_details':cart_details})



# ADD_TO_CART PAGE
# class AddressView(View):
    
#     def get(self,request,pk):
#         print("inside address------------------------------------------------------------------" )
#         cart_details = Product.objects.filter(pk=pk)

#         # ADDRESS FORM
#         fm = AddressForm()
#         address = customer.objects.all()

#         # EDIT ADDRESS
#         # data = customer.objects.get(pk=pk)
#         # edit_f = customer(instance=data)
#         return render(request,'address.html',{'cart_details':cart_details,'form':fm,'address':address,})
    
#     def post(self,request,pk):
#         print('Post')
#         fm = AddressForm(request.POST)
#         user = request.user
#         print(user,"------------------------------------------------")
#         name = request.POST['name']
#         locality = request.POST['locality']
#         city = request.POST['city']
#         pincode = request.POST['pincode']
#         state = request.POST['state']
#         if fm.is_valid():
#             a = customer.objects.create(user=user,name=name,locality=locality,city=city,pincode=pincode,state=state)
#             # a.save()
#             # print("save address")
#             return render(request,'address.html')


def address(request,pk):
    cart_details = Product.objects.filter(pk=pk)

    # ADDRESS FORM
    fm = AddressForm()
    address = customer.objects.all()

    # EDIT ADDRESS
    address_id = request.GET.get('addressID')
    # address_id = request.GET['addressID']
    print("address id--------------------------- ",address_id)
    # data = customer.objects.get(pk=pk)
    # edit_f = customer(instance=data)

    if 'add' in request.POST:
        fm = AddressForm(request.POST)
        user = request.user
        print(user,"------------------------------------------------")
        name = request.POST['name']
        locality = request.POST['locality']
        city = request.POST['city']
        pincode = request.POST['pincode']
        state = request.POST['state']
        if fm.is_valid():
            a = customer.objects.create(user=user,name=name,locality=locality,city=city,pincode=pincode,state=state)
            a.save()
            print("save address")
            return redirect('/address/')
    elif 'edit' in request.POST:
        print('in else=========================================================')
        # address_id = request.POST['addressID']
        # print("name--------------------------- ",address_id)
        # data = customer.objects.get(pk=address_id)


    return render(request,'address.html',{'cart_details':cart_details,'form':fm,'address':address,})


# LOG OUT BY USER
def user_logout(request):
    logout(request)
    return render(request,'home_page.html')








