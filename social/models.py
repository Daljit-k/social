from django.db import models
class reg(models.Model):
    uname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    re_password = models.CharField(max_length=40)
    def __str__(self):
        return self.username + "==>" +self.email+"==>" +self.password+"==>"+self.re_password

class table1(models.Model):
    username = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
class signup(models.Model):
    uname = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    re_password = models.CharField(max_length=40)
    def __str__(self):
        return self.username + "==>" +self.email+"==>" +self.password+"==>"+self.re_password
class img_table(models.Model):
    uid = models.CharField(max_length=140)
    img = models.FileField()
    fullname = models.CharField(max_length=40)
    bio = models.CharField(max_length=140)
    
    def __str__(self):
        return self.uid + '==>' + self.img + '==>' + self.fullname + '==>'+self.bio

class userpost(models.Model):
    userid = models.CharField(max_length=140)
    img = models.FileField()
    status = models.CharField(max_length=140)
    posttime = models.CharField(max_length=40)
    
    def __str__(self):
        return self.userid + '==>' + self.img + '==>' + self.status + '==>'+self.posttime
class userpost1(models.Model):
    userid = models.CharField(max_length=140)
    img = models.FileField()
    status = models.CharField(max_length=140)
    posttime = models.CharField(max_length=40)
    profilepic = models.FileField(null=True)
    fullname = models.CharField(max_length=40,null=True)
    likes = models.CharField(max_length=140,default=0)
    user_liked = models.CharField(max_length=1400,default=0)
    
    def __str__(self):
        return self.userid + '==>' + self.img + '==>' + self.status + '==>'+self.posttime + '==>' + self.profilepic + '==>' + self.fullname + '==>'+self.likes + '==>'+self.user_liked

class Login_records(models.Model):
    userid = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    login_time = models.CharField(max_length=40)
    logout_time = models.CharField(max_length=40)
    def __str__(self):
        return self.userid + "==>" +self.username+"==>" +self.password+"==>"+self.login_time+"==>"+self.logout_time

class notifications(models.Model):
    fromid = models.CharField(max_length=40)
    toid = models.CharField(max_length=40)
    reqstatus=models.CharField(max_length=40)
    def __str__(self):
        return self.fromid + "==>" +self.toid+"==>" +self.reqstatus #+"==>"+self.login_time+"==>"+self.logout_time


class comments(models.Model):
    cmntrname = models.CharField(max_length=140)
    cmntrpic = models.FileField()
    comment = models.CharField(max_length=140)
    cmntttime = models.CharField(max_length=40)
    cmntrid = models.CharField(max_length=140,default=0)
    postid = models.CharField(max_length=140,default=0)
    
    
    def __str__(self):
        return self.cmntrname + '==>' + self.cmntrpic + '==>' + self.comment + '==>'+self.cmntttime + '==>' + self.cmntrid + '==>' + self.postid# + '==>'+self.likes + '==>'+self.user_liked
    

    
