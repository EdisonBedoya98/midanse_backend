from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

import polyglot
from polyglot.text import Text, Word
from polyglot.detect import Detector

@api_view(['GET', 'POST'])
def view_test(request):
    if request.method == 'GET':   
        arabic_text = u"""
أفاد مصدر امني في قيادة عمليات صلاح الدين في العراق بأن " القوات الامنية تتوقف لليوم
الثالث على التوالي عن التقدم الى داخل مدينة تكريت بسبب
انتشار قناصي التنظيم الذي يطلق على نفسه اسم "الدولة الاسلامية" والعبوات الناسفة
والمنازل المفخخة والانتحاريين، فضلا عن ان القوات الامنية تنتظر وصول تعزيزات اضافية ".
"""
        detector = Detector(arabic_text)
        print(detector.language)
        return Response({'data': 'hola del endpoint Get' , 'count': '1' })
    elif request.method == 'POST':
        data=request.data
        return Response(data, status=status.HTTP_201_CREATED)