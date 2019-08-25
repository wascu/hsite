from django.shortcuts import render,redirect

# Create your views here.
def login(request):
    if request.method == "POST":
        # form_=AccountForm(request.POST or None, instance=account)
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        message = "所有字段都必须填写！"
        if username and password:
            username = username.strip()
            try:
                user = models.User.object.get(name=username)
            except:
                return render(request,'login/login.html',{"message": message})
            if user.password == password:
                return redirect('/login/index/')
    return render(request,'login/login.html')

def index(request):
    return render(request,'login/index.html')
