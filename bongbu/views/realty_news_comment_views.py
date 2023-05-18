from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import Realty_News_Comment_Form
from ..models import Realty_News

def comment_create(request, news_id):
    news = get_object_or_404(Realty_News, pk=news_id)
    if request.method == "POST":
        form = Realty_News_Comment_Form(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now()
            comment.news = news
            comment.save()
            return redirect('bongbu:realty_news_detail', news_id=news.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'news': news, 'form': form}
    return render(request, 'bongbu/realty_news_detail.html', context)