# 写入数据
from django.http import HttpResponse, JsonResponse

from back.models import Color


def backdb(request):
    test1 = Color(color='green')
    test2 = Color(color='green')
    test3 = Color(color='green')
    test1.save()
    test2.save()
    test3.save()
    return JsonResponse({"result": "<p>数据添加成功！</p>"})