from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

import polyglot
from polyglot.text import Text, Word
from polyglot.detect import Detector
import json

@api_view(['GET', 'POST'])
def view_test(request):
    if request.method == 'GET':   
        text = request
        detector = Detector(text)
        print(detector.language)
        return Response({'data': 'ji' , 'count': '1' })
    elif request.method == 'POST':
        print(request)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['text']
        detector = Detector(content)
        print(detector.language.name)
        return Response({'name':detector.language.name,'code':detector.language.code,'confidence':detector.language.confidence}, status=status.HTTP_201_CREATED)