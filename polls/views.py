from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

from .forms import CreatePollForm
from polls.models import Poll, Vote

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'polls/home.html', context)


@user_passes_test(lambda u: u.is_superuser)
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'لایحه جدید ساخته شد.')
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }
    return render(request, 'polls/create.html', context)

@login_required(login_url='/login/')
def vote(request, poll_id):

    if not request.user.is_verified():
        return render(request, 'users/verify_error.html')
 
    poll = get_object_or_404(Poll, id=poll_id)
    #poll = Poll.objects.get(pk=poll_id)
    user = request.user


    if not poll.user_can_vote(user):
        context = {
            'voted': True,
            'poll': poll
        }
        return render(request, 'polls/vote.html', context)

    print('hey')
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')

        new_vote = Vote(user=request.user, poll=poll)
        new_vote.save()

        poll.save()

        return redirect('results', poll.id)

    context = {
        'voted': False,
        'poll': poll
    }
    return render(request, 'polls/vote.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'polls/results.html', context)
    