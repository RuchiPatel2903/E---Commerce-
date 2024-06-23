from django.shortcuts import render,redirect
from .models import Store,Top_product,Catagory,Product,Cart,Wishlist,O_tracker,O_item,Order
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'password_reset.html'
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login')

def index(request):
    tp_data = Top_product.objects.all()
    return render(request,'index.html',{'tp_data':tp_data})

def cat_prod(request,id):
    cat_prod_data = Product.objects.filter(cat_id=id)
    return render(request,'cat_prod.html',{'cat_prod_data':cat_prod_data})

def shop(request):
    prods = Paginator(Product.objects.all(), 2)
    page= request.GET.get('page')
    try:
        prods = prods.page(page)
    except PageNotAnInteger:
        prods = prods.page(1)
    except EmptyPage:	
        prods = prods.page(prods.num_pages)
    return render(request,'shop.html',{'prods':prods})

def prod_details(request,id):
    prod_data = Product.objects.get(pid=id)
    return render(request,'detail.html',{'prod_data':prod_data})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        s = Store(name=name,email=email,message=message)
        s.save()
        messages.success(request, "Data Submitted" )

        return redirect('/')
    return render(request,'contact.html')

@login_required(login_url='/login/')
def checkout(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state= request.POST['state']
        zip= request.POST['zip']
        amount= request.POST['amount']
        payment = request.POST['payment']

        tid = O_tracker.objects.get(otid=1)
        o = Order(name=name,email=email,phone=phone,address=address,city=city,state=state,zip=zip,amount=amount,u_id=request.user,ot_id=tid,p_type=payment)
        o.save()

        o_last = Order.objects.last()

        c_data = Cart.objects.filter(u_id=request.user)
        for c in c_data:
            p = Product.objects.get(pid=c.pid.pid)

            c_item = O_item(o_id=o_last,p_id=p,quantity=c.quantity,sub_total=c.sub_total())
            c_item.save()
            c.delete()

        return redirect('/confirm-order/'+ str(o.oid))
    return render(request,'checkout.html')

def confirm_order(request,id):
    o_data = Order.objects.get(oid=id)
    o_item_data = O_item.objects.filter(o_id=id)
    return render(request,'confirmorder.html',{'order_data':o_data,'order_item_data':o_item_data})

def order_history(request):
    o_data = Order.objects.filter(u_id=request.user)
    return render(request,'order_history.html',{'o_data':o_data})

@login_required(login_url='/login/')
def cart(request):
    c_data = Cart.objects.filter(u_id=request.user)
    return render(request,'cart.html',{'c_data':c_data})

@login_required(login_url='/login/')
def add_cart(request,id):
    c_data = Cart.objects.filter(u_id=request.user,pid=id)
    if c_data:
        messages.info(request,"Product is already in Cart...")
        return redirect('cart')
    else:
        p = Product.objects.get(pid=id)
        c = Cart(pid=p,u_id=request.user,quantity=1)
        c.save()
        messages.info(request,"Product is add to Cart...")
        return redirect('cart')

def delete_cart(request,id):
    c_data = Cart.objects.get(u_id=request.user,cid=id)
    c_data.delete()
    messages.success(request,"Product deleted from Cart...")
    return redirect('cart')

def minus_cart(request,id):
    c_data = Cart.objects.get(u_id=request.user,cid=id)
    if c_data.quantity <= 1:
        c_data.delete()
        messages.success(request,"Product deleted from Cart...")
        return redirect('cart')
    else:
        c_data.quantity -= 1
        c_data.save()
        messages.success(request,"Product quantity is decreased...")
        return redirect('cart')

def plus_cart(request,id):
    c_data = Cart.objects.get(u_id=request.user,cid=id)
    c_data.quantity += 1
    c_data.save()
    messages.success(request,"Product quantity is increased...")
    return redirect('cart')


def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        uname = request.POST['uname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 == pass2:
            if User.objects.filter(username=uname).exists():
                print("User already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print("Email already exists")
                return redirect('register')
            else:
                u = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
                u.save()
                messages.success(request, "User Created" )

                return redirect('login')
        else:
            print("Password not matched.......")
            return redirect('register')

        # s = Store(name=name,email=email,message=message)
        # s.save()
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pass1 = request.POST['pass1']
    
        user = auth.authenticate(username=uname,password=pass1)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "User Logged In" )

            return redirect('/')
        else:
            messages.success(request, "Invalid Credentials" )

            return redirect('login')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out" )

    return redirect('/')

@login_required(login_url='/login/')
def wish_list(request):
    w_data = Wishlist.objects.filter(u_id=request.user)
    return render(request,'wishlist.html',{'w_data':w_data})

@login_required(login_url='/login/')
def add_wish(request,id):
    c_data = Wishlist.objects.filter(u_id=request.user,pid=id)
    if c_data:
        messages.info(request,"Product is already in Wish-list...")
        return redirect('/wish-list/')
    else:
        p = Product.objects.get(pid=id)
        c = Wishlist(pid=p,u_id=request.user)
        c.save()
        messages.info(request,"Product is add to Wish-list...")
        return redirect('/wish-list/')

def delete_wish(request,id):
    c_data = Wishlist.objects.get(u_id=request.user,wid=id)
    c_data.delete()
    messages.success(request,"Product deleted from Wish-list...")
    return redirect('/wish-list/')


def search(request):
	query = request.GET['q_pro']

	if len(query)>50 or len(query)==0:
		allpro=Product.objects.none()
	else:	
		allpro = Product.objects.filter(name__icontains=query)

	if allpro.count() == 0:
		messages.warning(request, 'No search result found. please refine your query.')	

	param={'allpro':allpro, 'query':query}
	return render(request, 'search.html', param)



