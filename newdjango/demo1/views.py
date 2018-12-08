from django.shortcuts import render
from django.shortcuts import render,redirect
# from demo1.models import LiInfo
from demo1 import models
# 导入render和HttpResponse模块
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import Permission,User
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse

# 导入Paginator,EmptyPage和PageNotAnInteger模块
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.

def homePage(request):
    li1 = models.Li.objects.filter(sign=1)
    li2 = models.Li.objects.filter(sign=2)
    li3 = models.Li.objects.filter(sign=3)
    li4 = models.Li.objects.filter(sign=4)
    li5 = models.Li.objects.filter(sign=5)
    li6 = models.Li.objects.filter(sign=6)
    forum = models.forum.objects.filter(sign=4)
    paginator = Paginator(forum, 10)
    # 从前端获取当前的页码数,默认为1
    page = request.GET.get('page', 1)
    # 把当前的页码数转换成整数类型
    currentPage = int(page)
    try:
        print(page)
        forum = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        forum = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        forum = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request,'demo1/index.html',{'head1':li1,'head2':li2,'head3':li3,'head4':li4,'head5':li5,'head6':li6,'forum4':forum})

def demo(request):
    li = models.Liaa.objects.all()
    return render(request,'demo1/demo.html',{'aa':li})

def getname(request):
    a=request.POST.get('x.liname')
    return a

def log_in(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        # Django提供的authenticate函数，验证用户名和密码是否在数据库中匹配
        user = authenticate(username=username, password=password)
        if user is not None:
            # if user.is_active:
            login(request, user)
            # userper = User.objects.get(username=username)
            # if userper.has_perm('add_delete_alter'):
            #     can = True
            # else:
            #     can = False
            #print('succeed')
            return HttpResponseRedirect("/index/")

        else:
            print('failed')
            return render(request,'demo1/Userlogin.html')
    else:
        return render(request,'demo1/Userlogin.html')

def resiger(request):
    if request.method=='POST':
        username = request.POST['username']
        filterResult = User.objects.filter(username=username)
        if len(filterResult) > 0:
            return render(request,'demo1/Userdemo.html',{'error1' : "用户名已存在"})
        else:
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            #error = []
            if(password1 != password2):
                return render(request,'demo1/Userdemo.html',{'error2' : "两次输入密码不一致！"})
            password = password2

            user = User.objects.create_user(username=username,password=password)
            #user.last_name = 'Lennon'
            user.save()
            return render(request,'demo1/Success.html',{'success' : "注册成功！"})
    else:

            # 渲染模板
            # 如果不是 POST 请求，则渲染的是一个空的表单
            # 如果用户通过表单提交数据，但是数据验证不合法，则渲染的是一个带有错误信息的表单
        return render(request, 'demo1/Userdemo.html')
def success(request):
    return render(request,'demo/Success.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/index/")

def submit(request):
    if request.method=='POST':
        head = request.POST['title']
        pic_head = request.POST['pic_title']
        content = request.POST['content']
        models.Li.objects.create(liname = head,litext = content,lipicture = pic_head)
        return HttpResponseRedirect("/index/")
    else:
        return render(request,'demo/index.html')

def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'demo1/result.html', {'error_msg': error_msg})


    post_list = models.Li.objects.filter(litext__icontains=q)
    return render(request, 'demo1/result.html', {'error_msg': error_msg,
                                               'post_list': post_list})


# login_ajax
def login_ajax(request):
    return render(request, 'demo1/index.html')


# login_ajax_check
def login_ajax_check(request):
    username = request.GET.get('username')
    password = request.GET.get('password')

    if username == 'smart' and password == '123':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})