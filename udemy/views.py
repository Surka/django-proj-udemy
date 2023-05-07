

from django.shortcuts import render
from django.http import HttpResponse
import operator

# Create your views here.

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count (request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split(' ')
    wordDictionary = {}
    for word in wordlist:
        if word in wordDictionary:
            #increse
            wordDictionary[word] +=1
        else:
            #add to the dictionary
            wordDictionary[word] = 1

    sortWordList = sorted(wordDictionary.items(), key=operator.itemgetter(1), reverse=True)
      
    return render(request,'count.html',{'fulltext': fulltext, 'count':len(wordlist), 'sortedWordList':sortWordList})
