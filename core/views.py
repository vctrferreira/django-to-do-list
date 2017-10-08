# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from core.models import Item

import uuid


class TodoListView(ListView):

    model = Item
    template_name = "all_items.html"
    def render_to_response(self, context, **response_kwargs):
        response = super(TodoListView, self).render_to_response(context, **response_kwargs)
        if not self.request.COOKIES.get("todo_cookie_identifier"):
            response.set_cookie("todo_cookie_identifier", uuid.uuid4().hex) 
        return response

    def get_queryset(self, **kwargs):
        return Item.objects.filter(created_by=self.request.COOKIES.get("todo_cookie_identifier"))


    def post(self, *args, **kwargs):
        data = self.request
        if not data.POST.get("title_todo") is "":
            item = Item(title=data.POST.get("title_todo"), created_by=data.COOKIES.get("todo_cookie_identifier"), completed=False, priority=1)
            item.save()
        return redirect("core.create_new_todo")
