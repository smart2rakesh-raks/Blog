from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.template.loader import render_to_string

from user.models import Post
from .forms import productform
from .models import product

