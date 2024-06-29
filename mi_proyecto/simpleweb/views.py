from django.shortcuts import render,redirect
 
from django.http import HttpResponse
# Create your views here.
import mysql.connector as mcdb
conn = mcdb.connect(host="db", user="root", passwd="secret", port= 3306, database='prueba_django_db')
print('Successfully connected to database')
cur = conn.cursor()

def home(request):
    return  render(request,'home.html')


def categorylisting(request):
    cur.execute("SELECT * FROM `tb_category` WHERE `is_deleted` = 0")
    data = cur.fetchall()
    print(list(data))
    return render(request, 'view.html', {'categories': data})


def categorycreate(request):
    return render(request, 'add.html')   


def categoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['txt1']
        cur.execute("INSERT INTO `tb_category` (`category_name`, `is_deleted`) VALUES ('{}', 0)".format(catname))
        conn.commit()
        return redirect(categorycreate) 
    else:
        return redirect(categorycreate)


def categorydelete(request, id):
    print(id)
    cur.execute("UPDATE `tb_category` SET `is_deleted` = 1 WHERE `category_id` = {}".format(id))
    conn.commit()
    return redirect(categorylisting)



def categoryedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_category` where `category_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'edit.html', {'categories': data})   


def categoryupdate(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['txt2']
        cur.execute("update `tb_category` set `category_name` ='{}' where `category_id`='{}'".format(catname,catid))
        conn.commit()
        return redirect(categorylisting) 
    else:
        return redirect(categorylisting)