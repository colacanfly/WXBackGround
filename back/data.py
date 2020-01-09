from django.http import HttpResponse

from back.models import Color


def getData():
    # 初始化
    response1 = ""
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Color.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Color.objects.filter(id=1)

    # 获取单个对象
    # response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Color.objects.order_by('color')[0:2]

    # 数据排序
    Color.objects.order_by("id")

    # 上面的方法可以连锁使用
    Color.objects.filter(color="runoob").order_by("id")

    # 列表输出所有数据
    toLost = []
    for var in list:
        toLost.append(var.color)
    response = response1
    return toLost