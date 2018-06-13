from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from  .forms import TitleFrom

# Create your views here.
def index(request):
    """博客主页"""
    titles =BlogPost.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/index.html', context)

def title(request, title_id):
    """显示单个标题的所有内容"""
    title = BlogPost.objects.get(id=title_id)
    entries = title.serializable_value('text')
    context = {'title': title, 'entries': entries}
    return render(request, 'blogs/title.html', context)

@login_required
def new_title(request):
    if request.method != 'POST':
        #未提交数据创建一个新表单
        form = TitleFrom()
    else:
        #POST提交的数据，读数据进行处理
        form = TitleFrom(data=request.POST)
        if form.is_valid():
            new_title = form.save(commit=False)
            new_title.owner = request.user
            new_title.save()
            return HttpResponseRedirect(reverse('blogs:index'))

    context = {'form': form}
    return render(request, 'blogs/new_title.html',context)

def edit_title(request, title_id):
    """编辑既有条目"""
    title = BlogPost.objects.get(id=title_id)
    entry = title.serializable_value('text')

    if title.owner == request.user:
        if request.method != 'POST':
            #初次请求，使用当前条目填充表单
            form = TitleFrom(instance=title)
        else:
            #POST提交的数据，对数据进行处理
            form = TitleFrom(instance=title, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('blogs:title', args=[title.id]))

    context = {'title': title, 'entry': entry, 'form': form}
    return render(request, 'blogs/edit_title.html', context)