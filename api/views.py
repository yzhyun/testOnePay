import json

from django.forms import model_to_dict
from django.http import JsonResponse, request
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.views.generic import ListView
from django.http import HttpResponse

import requests
import hashlib

from django.views.generic.edit import BaseCreateView

from api.models import pm002

@method_decorator(csrf_exempt, name='dispatch')
class ApiGetList(ListView):

    def get(self, request, *args, **kwargs):
        print(request, *args, **kwargs)
        print(request.method)
        tmpList = [
            {'id': 1, 'name': 'd테스트1', 'todo': '테스트 내용 1'},
            {'id': 2, 'name': 'd테스트4', 'todo': '테스트 내용 4'},
            {'id': 3, 'name': 'd테스트2', 'todo': '테스트 내용 2'},
            {'id': 4, 'name': 'd테스트3', 'todo': '테스트 내용 3'},
        ]
        return JsonResponse(data=tmpList, safe=False)

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        body = json.loads(request.body.decode('utf8'))
        context['name'] = body['keyword']
        return self.render_to_response(context)

@method_decorator(csrf_exempt, name='dispatch')
def post(request):
    data=json.loads(request.body.decode('utf8'))
    print(data)

    #devUrl="https://dev-pm.cjone.com"
    devUrl="http://localhost:8080"
    url=devUrl+"/pm/v1/pmt/minfo/regi/do"
    header = {'Content-Type':'application/json', 'charset':'UTF-8', 'MERCHANT-KEY':data['merchantKey'], 'MERCHANT-ID':data['merchantId']}
    #data['signature'] = 'aaa';
    #signature =

    print(data)


    res = requests.post(url, headers=header, data=request.body)



    return HttpResponse(res)