from django.shortcuts import render, HttpResponse, redirect

from systemWeb.models import UserInfo, MyTeam

# Create your views here.

def userInfoList(request):
    # UserInfo.objects.create(username = 'Steven', passward = '123456')
    data_list = UserInfo.objects.all()
    # for item in data_list:
    #     print(item.id, item.username, item.passward)
    return render(request,'userInfo.html',{'data_list':data_list})

def userAdd(request):
    if request.method == "GET":
        return render(request,'signUpPage.html')
    #获取用户提交数据
    username = request.POST.get("username")
    password = request.POST.get("password")

    #添加到数据库
    UserInfo.objects.create(username=username, password=password)
    #添加后跳转到指定页面
    return redirect("/accCreated/")
    #添加成功标记
    # return HttpResponse("Add Sucessfully!")

def userDel(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id = nid).delete()
    return redirect("/userInfo/")

def teamInfoList(request):
    data_list = MyTeam.objects.all()
    return render(request,'contactUs.html',{'data_list':data_list})

def toContactPage(request):
    return render(request, "contactUs.html")

def toHomePageAndLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if UserInfo.objects.filter(username = username):
            if UserInfo.objects.filter(username = username)[0].password == password:
                return redirect('/main/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('user not exist')
    return render(request, "homePage.html")

def toAccCreatedPage(requeast):
    return render(requeast,"accCreated.html")

def toMainPage(request):
    return render(request,'mainPage.html')
