from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .serializers import *

import polyglot
from polyglot.text import Text, Word
from polyglot.detect import Detector
import json
from joblib import dump, load

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
        modelBOfWords = load('midanse/util/modeloBagOfWords.joblib')    
        trasnformedTextBofW = modelBOfWords.transform([content])

        clf = load('midanse/util/lrmodel.joblib')
        y = clf.predict(trasnformedTextBofW)

  

        detector = Detector(content)
        print(detector.language.name)
        return Response({'name':detector.language.name,'code':detector.language.code,'confidence':detector.language.confidence,'feeling':y})


def model(self, parameter_list):
    clf = load('midanse/util/lrmodel.joblib')
    y = clf.predict()
    return y

   