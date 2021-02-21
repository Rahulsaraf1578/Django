# I have created this file - Rahul
from django.http import HttpResponse
from django.shortcuts import render


#Class 1
# def index(request):
#     return HttpResponse("<html><h1>Rahul</h1></html>")
#
# def about(request):
#     return HttpResponse("My love you are looking gorgeous world")

# Class 2
# def index(request):
#     return render(request,'index.html')
#     # return HttpResponse("Home")
#
# def removepunk(request):
#     # Get the text
#     djtext=request.GET.get('text','default')
#     print(djtext)
#     # Analyse the text
#     return HttpResponse("Remove punc <a href='/'>back</a>")
#
# def capfirst(request):
#     return HttpResponse("Capitailize first letter <a href='/'>back</a>")
#
# def newlineremove(request):
#     return HttpResponse("New line remover <a href='/'>back</a>")
#
# def spaceremover(request):
#     return HttpResponse("Space remover <a href='/'>back</a>")
#
# def charcount(request):
#     return HttpResponse("Count character <a href='/'>back</a>")


##############################################################################

# Class 3
# We are using only one end point

# def index(request):
#     return render(request,'index.html')
#     # return HttpResponse("Home")
#
# def analyse(request):
#
#     # Get the text
#     djtext=request.GET.get('text','default')
#     # When we check removepunk then it will take it otherwise it will not take it
#     removepunc =request.GET.get('removepunc','off')
#     fullcaps =request.GET.get('fullcaps','off')
#     nocaps =request.GET.get('nocaps','off')
#     newlineremover =request.GET.get('newlineremover','off')
#
#     # print(removepunc)
#     # print(djtext)
#
#     # Check which checkbox is on
#     if removepunc == "on":
#         punctuations = '''!()-[]{};:,'"<>./?@#$%^&*_~'''
#         analysed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analysed = analysed+char
#         params = {'purpose':'Removed puncuations','analysed_text':analysed}
#         # Analyse the text
#         return render(request,'analyze.html',params)
#
#     elif(fullcaps=="on"):
#         analysed=""
#         for char in djtext:
#             analysed = analysed + char.upper( )
#         params = {'purpose': 'Change to upper text', 'analysed_text': analysed}
#         return render(request,'analyze.html',params)
#
#     elif (nocaps == "on"):
#         analysed = ""
#         for char in djtext:
#             analysed = analysed + char.lower()
#         params = {'purpose': 'Change to lower text', 'analysed_text': analysed}
#         return render(request, 'analyze.html', params)
#
#     elif (newlineremover == "on"):
#         analysed = ""
#         for char in djtext:
#             if char != "\n":
#                 analysed = analysed + char
#         params = {'purpose': 'New line remover', 'analysed_text': analysed}
#         return render(request, 'analyze.html', params)
#
#     else:
#         return HttpResponse("Error")

##############################################################################

# Class 4
# A exercise was given to add buttons so this is the solution
# def ex1(request):
#     sites = ('''
#         <h1>Welcome page</h1>
#         <ul>
#             <li><a href="https://www.youtube.com">Youtube</a></li>
#             <li><a href="https://www.youtube.com">Linkdin</a></li>
#             <li><a href="https://www.linkedin.com">Github</a></li>
#         </ul>
#     ''')
#     return HttpResponse(sites)

##############################################################################

# class 5


# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def ex1(request):
    sites = ['''For Entertainment youtube video''',
             '''For Interaction Facebook''',
             '''For Insight   Ted Talk''',
             '''For Internship   Intenship''',
             ]
    return HttpResponse((sites))

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    print(djtext)

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        # Analyze the text
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if(removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Please select an operation and try again")

    return render(request,'analyze.html',params)
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newline remove first")
#
#
# def spaceremove(request):
#     return HttpResponse("space remover back")
#
# def charcount(request):
#     return HttpResponse("charcount ")





