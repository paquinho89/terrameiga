# your_app/middleware.py
from django.shortcuts import redirect, render
from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

class ErrorRedirectMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        return render(request, 'error.html')
