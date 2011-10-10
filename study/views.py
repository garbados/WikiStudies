# Create your views here.
from django.template import Context, loader
from django.http import HttpResponse
from study.models import *
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404

# study functions
def studyIndex(request):
    latest_study_list = Study.objects.all().order_by('id')[:5]
    t = loader.get_template('studyIndex.html')
    c = Context({
        'latest_study_list': latest_study_list,
    })
    return HttpResponse(t.render(c))
    
def studyDetail(request, study_id):
    s = get_object_or_404(Study, pk=study_id)
    return render_to_response('studyDetail.html', {'study': s})
