from django.shortcuts import render

from .models import Tweet
from .forms import TweetForm , UserRegistrationForm
from django.shortcuts import get_object_or_404 , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
def index(request):
    return render(request,'index.html')

def tweet_list(request):
    tweet = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweet':tweet})


# def tweet_create(request):
#     if request.method == 'POST':
#         form = TweetForm(request.POST , request.FILES)
#         if form.is_valid():
#             form.save(commit=False)
#             Tweet.user = request.user
#             Tweet.save()
#             return redirect('tweet_list')
#     else:
#         form = TweetForm()
#     return render(request, 'tweet_edit.html', {'form': form})
 
@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')

    else:
        form = TweetForm()

    return render(request, 'tweet_edit.html', {'form': form})
@login_required
def tweet_edit(request, tweet_pk):
    tweet = get_object_or_404(Tweet, pk=tweet_pk , user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_edit.html', {'form': form})
@login_required
def tweet_delete(request, tweet_pk):
    tweet = get_object_or_404(Tweet, pk=tweet_pk , user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_delete.html', {'tweet': tweet})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             # user.set_password(form.cleaned_data['password'])
#             user.set_password(form.cleaned_data['password1'])

#             user.save()
#             login(request, user)
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
#     return render(request,'registration/register.html',{'form':form})


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
  