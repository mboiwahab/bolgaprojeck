from django.db import models
from django.db.models.deletion import CASCADE


class Question (models.Model):
    question_test=models.CharField(max_length=200)
    pub_date=models.DateField('date published')


class choice(models.Model):
    question=models.ForeignKey(Question, on_delete=CASCADE)
    choice_text=models.CharField(max_length=200)
    votes = models.IntegerField(default=0)




'''In [6]: Question.objects.all()                                                                                                                
Out[6]: <QuerySet []>

In [7]: bolga=Question(question_test="What is your favourate javascript frame work?",pub_date=timezone.now())     
Kennedy-MBP:bolgabd kennedykofiasewie$ python3 manage.py shell

In [5]: from django.utils import timezone                                                                         

In [6]: a=Question(question_test="What is your favorite php framework", pub_date=timezone.now())                  

In [7]: Question.objects.all()                                                                                    
Out[7]: <QuerySet []>

In [8]: a.save()                                                                                                  

In [9]: Question.objects.all()                                                                                    
Out[9]: <QuerySet [<Question: Question object (1)>]>

In [10]:  '''