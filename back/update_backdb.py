# 数据库操作 更新
from django.http import JsonResponse

from back.models import Color


def backdb_update(index, index_color):
    print(index_color)
    print(index)

    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test = Color.objects.get(id=(int(index)+1))
    print(test.color)
    test.color = index_color
    test.save()
    print("===")
    # 另外一种方式
    # Test.objects.filter(id=1).update(name='Google')
    # 修改所有的列
    # Test.objects.all().update(name='Google')
    #return JsonResponse({"result": "修改成功"})


def update(request):
    if request.method == "POST":
        index = request.POST.get('index')
        print(index + "-----------------------")
        print(request.POST)
        index_color = request.POST.get('index_color')
        print(index_color)
        backdb_update(index, index_color)
        return JsonResponse({"result": "success"})
    else:
        return JsonResponse({"result": "fail"})