# This file is created by ME (Dhruv)

from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')
    # To get the value of value of checkbox with name = "removepunc"
    removepunc = request.POST.get('removepunc', 'off')
    # To get the value of value of checkbox with name = "fullcaps"
    fullcaps = request.POST.get('fullcaps','off')
    newlineremove = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    removenum = request.POST.get('removenum','off')

    # To Remove punctuation
    if removepunc == "on":
        analyzed = ""
        punc_list = string.punctuation
        for char in djtext:
            if char not in punc_list:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctutions', 'analyzed_text':analyzed}
        
        djtext = analyzed

    # To Capitalize
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Changed to UpperCase', 'analyzed_text':analyzed}

        djtext = analyzed

    # New line Remover
    if (newlineremove == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}

        djtext = analyzed

    # Space Remover
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text':analyzed}

        djtext = analyzed

    # Character counter
    if (charcount == "on"):
        count = 0
        punc_list = string.punctuation
        for char in djtext:
            if (char not in punc_list):
                count += 1
            if (char == "\n") and (char == "\r"):
                pass
            if (djtext[index] == " " and djtext[index + 1] == " "):
                pass

        params = {'purpose':'Character Counter', 'analyzed_text':count}

    # To remove Number
    if (removenum == "on"):
        analyzed = ""
        for char in djtext:
            if not(char.isdigit()):
                analyzed = analyzed + char
        params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}

        djtext = analyzed          

    if ((removepunc != 'on') and (newlineremove != 'on') and (extraspaceremover != 'on') and (fullcaps != "on") and (charcount != 'on') and (removenum != 'on')):

        return HttpResponse("PLEASE SELECT ANY OPERATION...")

    return render(request, "analyze.html", params)

