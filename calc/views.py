from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'calc/home.html')


def about(request):
    return render(request, 'calc/about.html')


def count(request):
    wordcount = request.GET['textbox']
    lines = wordcount.split()
    worddict ={}
    for word in lines:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] =1
    return render(request, 'calc/count.html', {'wordcount':wordcount,'lines':len(lines),'worddict':worddict.items()})