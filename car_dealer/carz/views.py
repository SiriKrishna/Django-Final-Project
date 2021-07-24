from django.shortcuts import render,redirect
from carz.forms import CarForm,UsgForm,Rltype,Rlupd,Pfupd,Chgepwd
from carz.models import Car,Rolereq,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail
from car_dealer import settings
from .filters import CarFilter

# Create your views here.
def home(request):
	w = Car.objects.all()

	myFilter = CarFilter()
	context = {'myFilter':myFilter}
	return render(request,'home.html',{'c':w})

	
	

def about(request):
	return render(request,'about.html')

def contact(request):
	return render(request,'contact.html')

@login_required
def carlist(request):
	y = Car.objects.all()
	if request.method == "POST":
		t = CarForm(request.POST,request.FILES)
		if t.is_valid():
			c = t.save(commit=False)
			c.uid_id = request.user.id
			c.save()
			messages.success(request,"Car Added Successfully")
			return redirect('/crlist')
	t = CarForm()
	return render(request,'carlist.html',{'q':t,'a':y})
@login_required
def carup(request,m):
	k = Car.objects.get(id=m)
	if request.method == "POST":
		e = CarForm(request.POST,instance=k)
		if e.is_valid():
			e.save()
			return redirect('/crlist')
	e = CarForm(instance=k)
	return render(request,'carupdate.html',{'x':e})

@login_required
def crdl(request,n):
	v = Car.objects.get(id=n)
	if request.method == "POST":
		v.delete()
		return redirect('/crlist')
	return render(request,'cardelete.html',{'q':v})	


@login_required
def carview(request,a):
	s = Car.objects.get(id=a)
	return render(request,'carview.html',{'z':s})

@login_required
def payment(request,a):
	s = Car.objects.get(id=a)
	return render(request,'payment.html',{'z':s})	

def usrreg(request):
	if request.method == "POST":
		d = UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/login')
	d = UsgForm()
	return render(request,'usrregister.html',{'t':d})

@login_required
def rolereq(request):
	p = Rolereq.objects.filter(ud_id=request.user.id).count()
	if request.method == "POST":
		k = Rltype(request.POST,request.FILES)
		if k.is_valid():
			y = k.save(commit=False)
			y.ud_id = request.user.id
			y.uname = request.user.username
			y.save()
			return redirect('/')
	k = Rltype()
	return render(request,'rolereq.html',{'d':k,'c':p})

@login_required
def gveperm(request):
	u = User.objects.all()
	r = Rolereq.objects.all()
	d = {}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id != m.ud_id:
				continue
			else:
				d[m.id] = m.uname,m.rltype,n.role,n.id,m.id
	return render(request,'gvper.html',{'h':d.values()})

@login_required
def gvupd(request,t):
	y = Rolereq.objects.get(ud_id=t)
	d = User.objects.get(id=t)
	if request.method == "POST":
		n = Rlupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked = 1
			y.save()
			return redirect('/gvper')
	n = Rlupd(instance=d)
	return render(request,'gvepermsion.html',{'c':n})

@login_required
def gvdlte(request,m):
	n = Rolereq.objects.get(id=m)
	t = User.objects.get(id=n.ud_id)
	if request.method == "POST":
		n.delete()
		t.role = 1
		t.save()
		return redirect('/gvper')
	return render(request,'gvdlte.html',{'d':n})

@login_required
def pfle(request):
	return render(request,'profile.html')

@login_required
def feedback(request):
	if request.method == "POST":
		sd = request.POST['snmail'].split(',')
		sm = request.POST['sub']
		mg = request.POST['msg']
		rt = settings.EMAIL_HOST_USER
		dt = send_mail(sm,mg,rt,sd)
		if dt == 1:
			return redirect('/')
	return render(request,'feedback.html')

@login_required
def pfleupd(request):
	t = User.objects.get(id=request.user.id)
	if request.method == "POST":
		pfl = Pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')
	pfl = Pfupd(instance=t)
	return render(request,'pfleupdate.html',{'u':pfl})

@login_required
def changepwd(request):
	if request.method == "POST":
		k = Chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = Chgepwd(user=request)
	return render(request,'changepwd.html',{'t':k})	
