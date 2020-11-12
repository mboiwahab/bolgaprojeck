from django.shortcuts import render
from django.http import HttpResponse
from.models import Question, Choice

def index(request):
    latest_Question_list=Question.objects.order_by
    ('-pub_date')
    #context={
        #'latest_question_list':latest_Question_list
    #}
    return render(request, 'polls/indext.html',latest_Question_list)
