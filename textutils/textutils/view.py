from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyse(request):
    #Get the text
    text = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcounter = request.POST.get('charcounter','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analysed_text': analyzed}
        text = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analysed_text': analyzed}
        text = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in text:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analysed_text': analyzed}
        text = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(text):
            if not(text[index] == " " and text[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analysed_text': analyzed}
        text = analyzed


    if (charcounter == "on"):
        count = 0
        for char in text:
            if char != ' ' and char != '\n' and char != '\r' :
                count += 1
        params = {'purpose': 'Total Characters', 'analysed_text': count}
    
    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on"  and fullcaps != "on" and charcounter != "on"):
        return HttpResponse("Please select any operations and try again")

    return render(request, 'analyse.html', params)


def AboutUs(request):
    return render(request,"aboutus.html")

def ContactUs(request):
    return render(request,"contactus.html")