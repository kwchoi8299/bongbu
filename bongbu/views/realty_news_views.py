from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Realty_News, Question


def realty_news_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    realty_news_list = Realty_News.objects.order_by('-create_date')
    if kw:
        realty_news_list = realty_news_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) # 답변 내용 검색
        ).distinct()

    paginator = Paginator(realty_news_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'realty_news_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'bongbu/realty_news_list.html', context)