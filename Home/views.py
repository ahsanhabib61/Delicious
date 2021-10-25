from django.shortcuts import render , HttpResponse
from django.core.mail import send_mail ,  send_mass_mail
from django.conf import settings
from Home.models import Pizza , Burger ,Shawarma_pltr , Appetizer , Sandwiche , Pasta_Roll , Address ,Customer , Cartitem , Cart ,Order , Contact
import json  ,datetime 

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contct = Contact(Name=name , Email= email , Message= message)
        contct.save()
        thank = True        
        return render(request , 'index.html' ,{'thank' : thank} )
    return render(request , 'index.html') 
   
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        jason = request.POST.get('itemsJson')
        totle_price = request.POST.get('totle_price')
        No_of_items = request.POST.get('No_of_items')
        passwrd = request.POST.get('password')
        if Customer.objects.filter(Email=email).exists():
            data = Customer.objects.get(Email=email , Password=passwrd)             

            cartt = Cart(Total_price = totle_price , No_of_items = No_of_items)
            cartt.save()
            order = Order(cart=cartt , customer=data , Date_time= datetime.datetime.now())
            order.save()

            message = "Thanks " + data.Name + " for using our services! \n\n   You order is \n"
            cart = json.loads(jason)
            for item in cart:
                cartitem = Cartitem(Cart_id = cartt , Name = cart[item][1]  , Quantity = cart[item][0] )
                message=message + str(cart[item][0]) + " - " + cart[item][1] + "\n"
                cartitem.save() 
                
            message2 = "\n A new order is arrived with order_id " + str(order.id) + " , at " + str(datetime.datetime.now() ) 

            message=message + "\n Your Total numbers of Products are - " + No_of_items + " and Total Price is Rs. " + totle_price     
            message=message + "\n Your Order will be Delievered in less than 3 Hours , Stay Home , Stay Happy "    
            subject = 'Delecious '
            email_from = settings.EMAIL_HOST_USER

            datatuple = (        
            ( subject ,  message , email_from , [email]),
            ( subject ,  message2 , email_from, ['malikalishan846@gmail.com']),
            )
            send_mass_mail(datatuple)

            thank = 1
            return render(request , 'checkout.html' , {'thank' : thank})
        else:
            thank = 2
            return render(request , 'checkout.html' , {'thank' : thank})
            
    return render(request , 'checkout.html') 
   

def base(request):
    return render(request , 'base.html')


def checkout(request):
    if request.method == "POST":
        jason = request.POST.get('itemsJson')
        totle_price = request.POST.get('totle_price')
        No_of_items = request.POST.get('No_of_items')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        phone = request.POST.get("phone")
        street = request.POST.get("street")

        if Customer.objects.filter(Email=email , Password=password).exists():
            thank = 3
            return render(request , 'checkout.html' , {'thank' : thank})
        else:
            adress = Address(City_name = city , street_No = street , Zip_code= zip , Phone_NO= phone)
            adress.save()
            customer = Customer(Name = name , Email = email , Password = password,  address = adress)
            customer.save() 
            cartt = Cart(Total_price = totle_price , No_of_items = No_of_items)
            cartt.save()
            order = Order(cart=cartt , customer=customer , Date_time= datetime.datetime.now())
            order.save()

            message = "Thanks " + name + " for using our services! \n\n   You order is \n"
            cart = json.loads(jason)
            for item in cart:
                cartitem = Cartitem(Cart_id = cartt , Name = cart[item][1]  , Quantity = cart[item][0] )
                message=message + str(cart[item][0]) + " - " + cart[item][1] + "\n"
                cartitem.save() 
                
            message2 = "\n A new order is arrived with order_id " + str(order.id) + " , at " + str(datetime.datetime.now() ) 

            message=message + "\n Your Total numbers of Products are - " + No_of_items + " and Total Price is Rs. " + totle_price     
            message=message + "\n Your Order will be Delievered in less than 3 Hours , Stay Home , Stay Happy "    
            subject = 'Delecious '
            email_from = settings.EMAIL_HOST_USER

            # recipient_list1 = [email]
            # send_mail( subject, message, email_from, recipient_list1 )         
            
            datatuple = (        
            ( subject ,  message , email_from , [email]),
            ( subject ,  message2 , email_from, ['malikalishan846@gmail.com']),
            )
            send_mass_mail(datatuple)       
            thank = 1
            return render(request , 'checkout.html' , {'thank' : thank})       
    return render(request , 'checkout.html')
   
def order(request):
    pizaa = Pizza.objects.all()
    burgerr = Burger.objects.all()
    appetizer = Appetizer.objects.all()
    shawarma_pltr  = Shawarma_pltr.objects.all()
    sandwiche = Sandwiche.objects.all()
    pasta_Roll = Pasta_Roll.objects.all()
    para = {
        'piza' : pizaa ,
        'burger' : burgerr ,
        'appetizer' : appetizer,
        'shawarma_pltr' : shawarma_pltr ,
        'sandwiche' : sandwiche ,
        'pasta_Roll' : pasta_Roll ,

    }
    return render(request , 'order.html'  , para)