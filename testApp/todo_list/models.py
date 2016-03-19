from __future__ import unicode_literals
import json
from django.db import models

# priority set
Priority_Choice = (
    ('0','low'),
    ('1','medium'),
    ('2','high'),
)

# done or not
Flag = (
    ('0','not done'),
    ('1','done')
)

#user model
class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=40,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    password = models.CharField(max_length=40,blank=False,null=False,unique=True)

    #to string
    def __unicode__(self):
        return self.email

    # for query
    class Meta:
        ordering = ['-u_id']



#todo_list
class Todo(models.Model):
    t_id = models.AutoField(primary_key=True)
    u = models.ForeignKey(User, on_delete=models.CASCADE)
    t_title = models.CharField(max_length=40,blank=False,null=False,unique=True)
    t_date = models.CharField(max_length=40)
    t_priority = models.CharField(max_length=10,choices=Priority_Choice)
    t_choice = models.CharField(max_length=10,choices=Flag)

    #to string
    def __unicode__(self):
        return self.t_title

    # for query
    class Meta:
        ordering = ['-t_id']


