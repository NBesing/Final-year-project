from django.shortcuts import render
from .models import Assessment

def assessment_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'assessment/assessment_list.html', {'assessments': assessments})

def assessment_detail(request, pk):
    assessment = Assessment.objects.get(pk=pk)
    return render(request, 'assessment/assessment_detail.html', {'assessment': assessment})
