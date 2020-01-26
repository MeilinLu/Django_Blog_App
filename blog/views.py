# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .model import Post, Comment
from datetime import datetime
from .forms import commentForm

# Create your views here.
def index(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    return renden(request, 'blog/post_list.html', {'posts': posts})

