from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from Upload.models import Shop, Img


class UploadView(View):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request):
        # POST获取字符的部分信息
        desc = request.POST.get('desc')
        name = request.POST.get('name')
        # 获取文件部分信息
        # img = request.FILES.get('img')
        shop = Shop(desc=desc, name=name)
        shop.save()

        # 获取多个文件
        img_list = request.FILES.getlist('img')
        images = []
        for image in img_list:
            images.append(Img(img=image, name=shop, type=1))
        # 批量保存
        Img.objects.bulk_create(images)
        return HttpResponse('上传成功')
