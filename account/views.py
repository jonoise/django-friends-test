from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Account

@login_required()
def account_detail(request):
    user = request.user
    account = Account.objects.get(user=user)
    
    context = {
        'user': user,
        'account': account,
    }

    return render(request, 'account/detail.html', context)