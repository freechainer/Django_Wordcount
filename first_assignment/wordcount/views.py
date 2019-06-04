from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'wordcount/home.html')


def about(request):
    return render(request, 'wordcount/about.html')


def count(request):
    full_text = request.GET['fulltext']
    
    word_list = full_text.split()
    
    word_dictoinary = {}
    
    for word in word_list:
        if word in word_dictoinary:
            # increase
            word_dictoinary[word] += 1
            # add to the dictionary
            word_dictoinary[word] = 1
    
    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictoinary.items()})