from django.shortcuts import render

def excel_file_report(response):
    return response

def htmlpage(request,template,dic):
    rend= render(request, template, dic)
    return rend