from django.http import Http404
from .models import Pet, Cart
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
	all_pets = Pet.objects.all()
	context = {'all_pets':all_pets}
	return render(request, 'shop/index.html', {'all_pets': all_pets})


def detail(request, pet_id):
	try:
		pet = Pet.objects.get(pk= pet_id)
	except Pet.DoesNotExist:
		raise Http404("Page does not exist")
	return render(request, 'shop/detail.html', {'pet': pet})

def Login(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return redirect('/shop')
	else:
		return redirect('/shop/loginform')

def logout_view(request):
	logout(request)
	return render(request, 'shop/index.html')

def loginform(request):
	return render(request, 'shop/loginform.html')

def addtocart(request, pet_id):
	pet = Pet.objects.get(pk= pet_id)
	newitem = Cart(userid = request.user, productid = pet)
	newitem.save()
	return redirect('/shop')

def cart(request):
	items = Cart.objects.filter(userid = request.user.id)
	cartlist = []
	for item in items:
		cartlist.append(Pet.objects.get(pet_type = str(item.productid)))
	return render(request, 'shop/transaction.html', {'cartlist':cartlist})

def checkout(request):
	items = Cart.objects.filter(userid = request.user.id)
	cartlist = []
	for item in items:
		Pet.objects.get(pet_type = str(item.productid)).delete()
	return redirect('/shop/successful')

def successful(request):
	return render(request, 'shop/successful.html')