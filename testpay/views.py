from django.views.generic import TemplateView
from django.shortcuts import render


class testMain(TemplateView):
    template_name = 'testpay/testmain.html'


class testPc2App(TemplateView):
    template_name = 'testpay/testPc2app.html'

class redirectPage(TemplateView):
    template_name = 'testpay/redirectUrl.html'


    '''def goTestPc2App(request):
        return render(request, 'testpay/testpc2app.html')'''
