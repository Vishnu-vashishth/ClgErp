from django.shortcuts import render
from . import models


def request_gate_pass(request):
    return render(request, 'gatepass/base.html')

def manage_gate_pass(request):
    return render(request, 'gatepass/base.html')
