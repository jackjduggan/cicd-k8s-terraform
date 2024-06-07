from django.shortcuts import render
from django.http import Http404

from .models import Project

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {
        'projects': projects
    })

def project_detail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        raise Http404('Project Not Found..')
    return render(request, 'project_detail.html', {
        'project': project
    })
