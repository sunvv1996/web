# -*-coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from blog import models
# Create your views here.
def index(request):
    bbs_list = models.BBS.objects.all()
    return render(request, 'index.html',{'bbs_list':bbs_list})

def bbs_detail(request, bbs_id):
    bbs = models.BBS.objects.get(id = bbs_id)
    return render_to_response('bbs_detail.html', {'bbs_obj':bbs})

