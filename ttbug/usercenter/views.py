from django.shortcuts import render
from django.contrib.auth.models import User
from blocks.models import Blocks
import uuid
import datetime
from django.core.mail import send_mail
from django.utils import timezone
from .models import ActivateCode
# Create your views here.

def register(request):
    blocks = Blocks.objects.all()
    if request.method == "GET":
        return render(request,"register.html",{"blocks":blocks})
    else:
        error = ""
        username = request.POST["username"].strip()
        email = request.POST["email"].strip()
        password = request.POST["password"].strip()
        re_password = request.POST["re_password"].strip()

        if not username or not email or not password or not re_password:
            error = "请仔细检查一遍，各字段均不能为空"
        
        if len(password) < 8:
            error = "密码长度小于8，请重新设置"
        if password != re_password:
            error = "两次密码输出不一致，请重新输入"
        
        if error:
            return render(request,"register.html",{"blocks":blocks,"error":error})
        else:
            user = User.objects.create_user(username,email,password)
            user.is_active = False
            user.save()
        
            new_code = str(uuid.uuid4()).replace("-","")
            expire_time = timezone.now()+datetime.timedelta(days=2)
            code_record = ActivateCode(name=user,code=new_code,expire_timestamp=expire_time)
            code_record.save()
            activate_link = "http://%s/activate/%s" % (request.get_host(),new_code)
            activate_email = '''点击<a href="%s">这里</a>激活''' % activate_link
            send_mail(
                  subject="[TTBug]激活邮件",
                  message="点击链接激活:%s" % activate_link,
                  html_message=activate_email,
                  from_email = "1137048513@qq.com",
                  recipient_list = [email],
                  fail_silently=False
                )
            return render(request,"register_success.html",{"blocks":blocks,"msg":"注册成功,激活邮件已经发送到您的邮箱，请点击邮箱中的激活链接完成激活"})

#用户激活控制器，接受传入的激活码,code和urls中的参数相同
def activate(request,code):
    blocks = Blocks.objects.all()
    query = ActivateCode.objects.filter(code=code,expire_timestamp__gte=timezone.now())
    if query.count() > 0:
        code_record = query[0]
        code_record.name.is_active = True
        code_record.name.save()
        return render(request,"activate_success.html",{"blocks":blocks,"msg":"激活成功，快去登陆吧..."})
    else:
        return render(request,"activate_failed.html",{"blocks":blocks,"msg":"激活失败"})

