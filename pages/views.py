from django.http import HttpResponse
from django.template import loader
from .models import Members
from .forms import MembersForm


def members(request):
  form = MembersForm()

  if request.method == "POST" :


def members(request):
  mymembers = Members.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {

    'mymembers': mymembers,
    'form' = form
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())