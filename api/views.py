import json

from django.forms import model_to_dict
from django.http import JsonResponse, request
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.http import HttpResponse

import requests

# dev
# trgtUrl="https://dev-pm.cjone.com"
# local
trgtUrl = "http://localhost:8080"

api_dict = {
    'pm1001': '/pm/v1/pmt/minfo/regi/do',  # 결제예약정보
    'pm1005': '/pm/v1/pmt/mthd/auth/do',  # 결제요청
    'pm1006': '/pm/v1/pmt/mthd/aprv/do',  # 결제승인
    'pm1010': '/pm/v1/pmt/cncl/all/do',  # 결제전체취소
    'pm1011': '/pm/v1/pmt/cncl/part/do',  # 결제부분취소
    'pm1015': '/pm/v1/pmt/aprv/noti'  # 승인결과통지

}


@method_decorator(csrf_exempt, name='dispatch')
def post(request):
    data = json.loads(request.body.decode('utf8'))
    url = trgtUrl + api_dict[data['apiId']]

    header = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'MERCHANT-KEY': data['merchantKey']
        , 'MERCHANT-ID': data['merchantId']}

    print("Call Url : " + url)

    res = requests.post(url, headers=header, data=request.body, verify=False)

    return HttpResponse(res)
