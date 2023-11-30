from django.shortcuts import render
from datetime import datetime,timedelta 

# Create your views here.
def home(request):
    d={'author':'tamim','age':23,'names': ['John', 'Paul', 'Ringo', 'George'],'text': "The quick brown fox jumps over the lazy dog.Django is a high-level Python framework.",'article_date': datetime.now() - timedelta(days=3),'num':[1, 2, 3],
    'product_prices':[
        {'price': 50},
        {'price': 70}, 
        {'price': 20},  
    ],
    'birthday':(datetime.now()),
    'courses':[
           {
               'course_id':1,
               'course_name':'Python',
               'fee':5000
           },
           {
               'course_id':2,
               'course_name':'Django',
               'fee':7900
           },
           {
               'course_id':3,
               'course_name':'Ruby',
               'fee':11000
           }
        ]
    }
    return render(request,'home.html',d)