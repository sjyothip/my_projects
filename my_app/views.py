from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from . models import User, Messages
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, logout, login as Login_user
# Create your views here.
from django.contrib import auth
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime, timezone, date, timedelta
from django.utils import timezone




@csrf_exempt
def log_usr(request):
	if request.method == 'POST':
		print("")
		print(request.POST)
		print("")
		emailORusername = request.POST['email']
		password = request.POST['password']
		print("")
		print(emailORusername)
		print("")
		if emailORusername and password:
			def authenticate(username=None, password=None):
				try:
					user = User.objects.get(email=username)
					if user.check_password(password):
						return user
				except:
					user = User.objects.get(username=username)
					if user.check_password(password):
						return user

			if authenticate(username=emailORusername, password=password):
				print('username')
				user = authenticate(username=emailORusername, password=password)
				data1 = User.objects.filter(username=emailORusername)
				data = list(data1.values())
				Login_user(request,user)
				print("USER",user)
				return render(request, 'main.html', {'data':data,'info1':" login"})

			
			# if authenticate(username=emailORusername, password=password):
			# 	print('email')
			# 	user = authenticate(username=email, password=password)
			# 	data1 = User.objects.filter(email=email)
			# 	data = list(data1.values())
			# 	Login_user(request,user)
			# 	print("USER",user)
			# 	return render(request, 'main.html', {'data':data,'info1':"Email login"})
			
			else:
				return render(request, 'log.html', {"data":"Invalid Credentials"})
		else:
			return render(request, 'log.html',{'data':'Provide Credentials'})

		return render(request,'log.html',{'data':'Use POST method'})


@csrf_exempt
def log(request):
	return render(request, 'log.html')

# @login_required(login_url='/my_app/login')
@api_view(['GET'])
def main(request):
	data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	return render(request, 'main.html',{'info':data})



@api_view(['GET'])
def testview(request):
	data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	# print(data)
	return render(request, 'user.html',{'info':data})


# @login_required(login_url='/my_app/login')
@csrf_exempt
def usr_pst(request):
	if request.method == 'POST':
		print("")
		print("requestr",request.POST)
		print("request",request.FILES)
		print("")
		username = request.POST.get('username')
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		profile = request.FILES.get('profile')
		phone = request.POST.get('phone')
		password = request.POST.get('password')
		print("image",profile)
		print("email",email)
		print("mobile",phone)
		usr = User.objects.create(
			username=username,
			email=email,
			first_name=first_name,
			last_name=last_name,
			profile_pic=profile,
			phone=phone,
			password=make_password(password)
			)
		data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
		# print(data)
		return render(request, 'main.html',{'info':data, 'info1':'User created'})
	return JsonResponse({'success':False, 'info':'User not created'})

# {% for i in data %}
# <div class="profile_image">

# <img class="profile_img" width="100%" src= "{{ MEDIA_URL }}/media/{{i.profile_pic}}" onerror="this.src='{{ MEDIA_URL }}/media/Images/avatar.png'">

# <!--   <img class="profile_img" width="100%" src= "http://127.0.0.1:8000/media/Images/avatar.png "> -->

 
# <img id="profile_img" style="#">
# </div>


 # {% if uploaded_file_url %}
 #    <p>File uploaded at: <a href="{{ uploaded_file_url }}">{{ uploaded_file_url }}</a></p>
 #  {% endif %}

# <!-- <img src="{% static "my_app/example.jpg" %}" alt="My image"> -->
# <img src="{% static 'img/image1.png' %}" />
# @api_view(['GET'])


# @login_required(login_url='/my_app/login')
def test_ing(request):
	return render(request,'usr_pst.html')


def testhtml(request):
	data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	print(data)
	return render(request,'test.html',{'info':data})

def testhtml2(request):
	data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	print(data)
	return render(request,'test2.html',{'info':data})

@api_view(['GET'])
def mock_time_limit(request):
	if request.method == 'GET':

		seen = set()
		new_l = []
		for d in data:
			t = tuple(d.items())
			if t not in seen:
				seen.add(t)
				new_l.append(d)
	
		return JsonResponse({'success':False, 'info':'Time OUT teeeeee'})

# @csrf_exempt
# def image_upload_view(request):
#     if request.method == 'POST':
#         form = User(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'index.html', {'form': form})


@csrf_exempt
def usr_del(request):
	idd = request.GET['id']
	User.objects.filter(id=idd).delete()
	data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	return render(request, 'test.html',{'info':data})


@login_required(login_url='/my_app/login')
@csrf_exempt
def usr_pst_msgs(request):
	if request.method == 'POST':
		print("")
		print("requestr",request.GET)
		print("requestr",request.POST)
		print("requestr",request.FILES)
		print("")
		message = request.POST.get('message')
		user_id = request.POST.get('to_user')
		file = request.FILES.get('file')
		User.objects.filter(id=user_id)
		msgs = Messages.objects.create(
			msgs=message,
			user_id=user_id,
			sender_id=request.user,
			shared_files=file
			)
		data = list(User.objects.filter(id=user_id).values('id','username','email','first_name','last_name','profile_pic'))
		name=request.user.username
		lid=request.user.id
		l = User.objects.get(id=user_id)
		msg = list(Messages.objects.filter(user_id=lid).filter(sender_id=l.username).order_by('added_at').values('user__id','user__username','msgs','sender_id'))
		msg1 = list(Messages.objects.filter(user=l.id).filter(sender_id=name).order_by('added_at').values('user__id','sender_id','msgs','user__username'))
		print("msg",msg)
		print("msg1",msg1)
		lis=[]
		for s in msg:
			lis.append(s)
		for c in msg1:
			lis.append(c)
		seen = set()
		print("")
		print("msg",msg)
		print("msg",msg1)
		print("")
		print("lis",lis)
		print("")
		new_l = []
		for d in lis:
		    t = tuple(d.items())
		    if t not in seen:
		        seen.add(t)
		        new_l.append(d)
		print(new_l)
		return render(request,'message.html',{'info':data,'info1':new_l})
	return render(request,'message.html',{'info':'Message not sent'})

@login_required(login_url='/my_app/login')
@csrf_exempt
def messagehtml(request):
	data = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	print(data)
	msg = list(Messages.objects.filter(user=request.user).values('id','msgs','added_at','user','sender_id','shared_files'))
	print("")
	print("msg",msg)
	print("")
	return render(request,'message.html',{'info':data,'info1':msg})

@login_required(login_url='/my_app/login')
@csrf_exempt
def chats(request):
	
	all_chats = list(User.objects.all().order_by('username').values('id','username','email','first_name','last_name','profile_pic'))
	msg = list(Messages.objects.filter(sender_id=request.user).order_by('user').values('user__id','user__username'))
	msg1 = list(Messages.objects.filter(user=request.user).order_by('user').values('user__id','sender_id'))
	lis=[]
	for s in msg:
		lis.append(s)
	for c in msg1:
		lis.append(c)
	print("")
	print("msg",msg)
	print("msg",msg1)
	print("")
	print("lis",lis)
	print("")
	seen = set()
	new_l = []
	for d in lis:
	    t = tuple(d.items())
	    if t not in seen:
	        seen.add(t)
	        new_l.append(d)
	# print("duplicate",[i for n, i in enumerate(msg) if i not in msg[n + 1:]])
	print(new_l)
	return render(request,'chats.html',{'info':new_l})

# from django.db.models import Q
@login_required(login_url='/my_app/login')
@csrf_exempt
def usr_chat(request):
	user_id=request.GET['user_id']
	chats = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	data = list(User.objects.filter(id=user_id).values('id','username','email','first_name','last_name','profile_pic'))
	print("data",data)
	name=request.user.username
	lid=request.user.id
	l = User.objects.get(id=user_id)
	# queryset = list(Messages.objects.filter(
	# 	Q(user_id=user_id),
	# 	Q(sender_id=name)|
	# 	Q(user_id=request.user),
	# 	Q(sender_id=l.username)
	# 	).values('id','user__username','msgs','added_at','user__id','sender_id','shared_files'))
	# print('queryset',queryset)
	msg = list(Messages.objects.filter(user_id=lid).filter(sender_id=l.username).order_by('added_at').values('user__id','user__username','msgs','sender_id'))
	msg1 = list(Messages.objects.filter(user_id=l.id).filter(sender_id=name).order_by('added_at').values('user__id','sender_id','msgs','user__username'))
	# print("msg",msg)
	print("msg1",msg1)
	lis=[]
	for s in msg:
		lis.append(s)
	for c in msg1:
		lis.append(c)
	seen = set()
	print("")
	print("msg",msg)
	print("msg",msg1)
	print("")
	print("lis",lis)
	print("")
	new_l = []
	for d in lis:
	    t = tuple(d.items())
	    if t not in seen:
	        seen.add(t)
	        new_l.append(d)
	print("new_l",new_l)
	return render(request,'message.html',{'info':data,'info1':new_l})

@login_required(login_url='/my_app/login')
@csrf_exempt
def usr_get_msgs(request):
	data = list(Messages.objects.all().values('id','msgs','added_at','user'))
	print(data)
	chats = list(User.objects.all().values('id','username','email','first_name','last_name','profile_pic'))
	return render(request,'addchat.html',{'info':data, 'info1':chats})


@login_required(login_url='/my_app/login')
@csrf_exempt
def chat_del(request):
	chat_id = request.GET['chat_id']
	Messages.objects.filter(user_id=chat_id).delete()
	all_chats = list(User.objects.all().order_by('username').values('id','username','email','first_name','last_name','profile_pic'))
	msg = list(Messages.objects.filter(sender_id=request.user).order_by('user').values('user__id','user__username'))
	seen = set()
	new_l = []
	for d in msg:
	    t = tuple(d.items())
	    if t not in seen:
	        seen.add(t)
	        new_l.append(d)

	print(new_l)
	return render(request,'chats.html',{'info':new_l, 'info1':all_chats})


@login_required(login_url='/my_app/login')
@csrf_exempt
def logout_request(request):
    auth.logout(request)
    # messages.info(request, "Logged out successfully!")
    return redirect('log')



@csrf_exempt
def test_test(request):
	one_week_ago = datetime.today()
	month12 = date.today() - timedelta(days=7)
	print(month12)
	# load_qs = list(Load.objects.filter(date__range=[month12,one_week_ago]).extra(select={'date': "DATE(date)"}).values("date").exclude(load_status="cancel").annotate(**{'total': Sum('quantity')}))
	li=[]
	no_days=7
	for i in range(8):
		some_day=timezone.now().date() - timedelta(days=no_days)
		li.append(some_day)
		no_days=no_days-1
		print(li,"li")
	data=[]
	for i in li:    
		load_qs = Messages.objects.filter(added_at=i).count()
		# load_qsss = list(Messages.objects.filter(date__range=[month12,one_week_ago]).extra(select={'date': "DATE(added_at)"}).values("added_at").annotate(**{'total': Sum('shared_files')}))
		# print(load_qsss)
		if load_qs:
			data.append({"added_at":i,"created_count":load_qs})
		else:
			data.append({"added_at":i,"created_count":0})
		print(data,"data")
            
	return JsonResponse({'success':True,'data':data})
