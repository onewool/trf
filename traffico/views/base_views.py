from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from django.db.models import Q

from ..models import Question

import logging
logger = logging.getLogger('traffico')

def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'traffico/index.html')

def introduce(request):
    return render(request, 'traffico/introduce.html')

def gyeonggi(request):
    return render(request, 'traffico/area/gyeonggi.html')

def seoul(request):
    return render(request, 'traffico/area/seoul.html')

def gangwon(request):
    return render(request, 'traffico/area/gangwon.html')

def chungcheong(request):
    return render(request, 'traffico/area/chungcheong.html')

def gyeongsang(request):
    return render(request, 'traffico/area/gyeongsang.html')

def jeolla(request):
    return render(request, 'traffico/area/jeolla.html')

def sitemap(request):
    return render(request, 'traffico/sitemap.html')

def board(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) |  # 내용 검색
            Q(answer__content__icontains=kw) |  # 답변 내용 검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이 검색
        ).distinct()
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'traffico/board.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'traffico/question_detail.html', context)