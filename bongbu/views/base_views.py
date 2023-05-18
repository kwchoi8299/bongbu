from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from bongbu.models import Question, Realty_News
from django.db.models import Q
#zzz

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) # 답변 내용 검색
        ).distinct()

    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'bongbu/question_list.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'bongbu/question_detail.html', context)

#부동산 뉴스 상세
def realty_news_detail(request, news_id):
    news = get_object_or_404(Realty_News, pk=news_id)
    context = {'news': news}
    return render(request, 'bongbu/realty_news_detail.html', context)

def page_not_found(request, exception):
    return render(request, 'common/404.html', {})