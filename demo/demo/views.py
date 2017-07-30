from django.shortcuts import render, get_object_or_404
from .models import Person
from .forms import PersonForm, DeletePersonForm
from django.shortcuts import render_to_response, HttpResponseRedirect

def home(request):
    return render(request, "demo/index.html")


def demo(request):
    form = PersonForm()
    person = Person()
    obj = Person.objects.all()
    if request.method=="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "demo/demo.html", {'person': obj, 'form': form})
    else:
        return render(request, "demo/demo.html", {'person': obj, 'form': form})


def demo_delete(request, id):
    new_delete = get_object_or_404(Person, id=id)
    print "This is new delete:      {}".format(new_delete)

    if request.method=='POST':
        form = DeletePersonForm(request.POST, id)
        print "This is id           {}".format(id)

        if form.is_valid():
            new_delete.delete()
            form = PersonForm()
            obj = Person.objects.all()
            # return render(request, 'demo/demo.html', {'person': obj, "form": form})
            return HttpResponseRedirect('http://192.168.0.108:8080/demo')

        else:
            return render(request, 'demo/demo.html')
