from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Blog
from .serializers import BlogSerializer
from django.db.models import F
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.

def home(request):
    """ this function view will show all the Blogs and blog information of current user after authenticating user
    from here user can choose three option 1. view 2.update 3.Add new blog"""
    if request.user.is_authenticated:
        data = Blog.objects.filter(author=request.user.id)
        return render(request,'home.html',{'records':data})
    else:
        return render(request,'login.html')

def login(request):
    """this view function will provide 2 methods for login one is Google and One is Facebook,
    But first it will check user is already logged in or not """
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:

        return render(request,'login.html')

def logout_user(request):
    """This view function will do user logout and redirect to login page"""
    logout(request)
    return redirect('login')

def blogapi(request):
    """ this blogapi is fetching data from model and converting that data in pyton native using serializers, after that
    returning those data in Json format"""
    data=Blog.objects.values('author__username','date','heading','blog')
    data=data.annotate(author=F('author__username'))
    serializer=BlogSerializer(data,many=True)
    return JsonResponse(serializer.data)

class JsonResponse(HttpResponse):
    """this Class is used for converting data in json and giving response into the json format, this class is used in blogapi view"""
    def __init__(self,data,**kwargs):
        content=JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JsonResponse,self).__init__(content,**kwargs)

@login_required()
def addblog(request):
    """this view is used for adding new blog by user, first it check the user is logged in or not
    then check if this request is get then we will provide html page for blog addition
    if request is post means it requesting for adding new blog in model , by taking all info we will add new blog in model"""
    if request.method=="GET":
        return render(request,"Addblog.html")
    if request.method=="POST":
        heading1=request.POST['heading']
        blog1=request.POST['blog']
        b=Blog(author=request.user,heading=heading1,blog=blog1)
        b.save()
        return HttpResponse("Blog added successfully")

def updateblog(request):
    """Update Blog is for updating the Blog's heading or Blog's containt or both,
    if request is get means user want to go to update page, from where user provide data after doing some modification
    provide data in POST metho. take those data and modify in model by using filter and Update method"""
    if request.method=="GET":
        b_id=int(request.GET['id'])
        b=Blog.objects.get(pk=b_id)
        return render(request,"updateblog.html",{'records':b})
    if request.method=="POST":
        heading=request.POST['heading']
        blog=request.POST['blog']
        b_id=int(request.POST['id'])
        b=Blog.objects.filter(pk=b_id).update(heading=heading,blog=blog)
        return HttpResponse("Updated successfully")
@login_required()
def viewblog(request):
    """ In this view we will get id of blog which user want to view
    then we will fecth all info of  that blog whose id is same as user given id and show into viewblog.html """
    id=request.GET['id']
    data=Blog.objects.get(pk=id)
    return render(request,"viewblog.html",{'records':data})

