from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.reg_validator(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request,error)
            return redirect('/')

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        gender = request.POST['gender']
        email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(first_name=first_name, last_name=last_name, gender=gender, email=email, password=pw_hash)

        request.session['user_id'] = user.id
        request.session['user_name'] = f"{user.first_name} {user.last_name}"
        return redirect('/success')
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id = request.session['user_id'])
    context = {
        "user_posts": User_Post.objects.all(),
        'user': this_user[0]
    }
    return render(request, 'success.html', context)

def login(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        logged_user = User.objects.filter(email=email)
    if logged_user:
        logged_user = logged_user[0]

        if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
            request.session['user_id'] = logged_user.id
            request.session['user_name'] = f"{logged_user.first_name} {logged_user.last_name}"

            return redirect('/success')
        else:
            messages.error(request, "Not correct password")
    else:
        messages.error(request, "This user does not exist")
        return redirect('/')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def create_post(request):
    message = request.POST['message']
    poster = User.objects.get(id=request.session['user_id'])
    User_Post.objects.create(message=message,poster=poster)
    return redirect('/success')

def add_comment(request,id):
    user_post = User_Post.objects.get(id=id)
    comment = request.POST['comment']
    poster = User.objects.get(id=request.session['user_id'])
    Comment.objects.create(comment=comment,poster=poster,user_post=user_post)
    return redirect('/success')

def like(request,id):
    user_post = User_Post.objects.get(id=id)
    user = User.objects.get(id=request.session['user_id'])
    user_post.likes.add(user)
    return redirect('/success')

def profile(request,id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'profile.html', context)

def edit_pg(request,id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'edit.html', context)

def edit(request,id):
    if request.method == 'POST':
        edit_user = User.objects.get(id=id)
        edit_user.first_name = request.POST['first_name']
        edit_user.last_name = request.POST['last_name']
        edit_user.gender = request.POST['gender']
        edit_user.email = request.POST['email']
        edit_user.password = request.POST['password']
        edit_user.save()
        return redirect(f'/edit_pg/{id}')

def delete_post(request,id):
    destroy = User_Post.objects.get(id=id)
    destroy.delete()
    return redirect('/success')

def delete_comment(request,id):
    destroy = Comment.objects.get(id=id)
    destroy.delete()
    return redirect('/success')