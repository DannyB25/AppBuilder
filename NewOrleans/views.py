from django.shortcuts import render, get_object_or_404, redirect #renders HTML template with given data and redirects to the different URL
from .forms import HappyPlaceForm #imports the HappyPlaceForm from forms.py to handle form data
from .models import HappyPlace

def home(request):
    return render(request, 'NewOrleans/home.html')
def history(request):
    return render(request, 'NewOrleans/history.html')
def food(request):
    return render(request, 'NewOrleans/food.html')
def fun(request):
    if request.method == 'POST': #checks to see if request method is POST/form has been submitted
        form = HappyPlaceForm(request.POST) #creates an instance of HappyPlaceForm with POST data, which populates the form with submitted data
        if form.is_valid(): #makes sure form is valid according to the models rules/restrictions
            form.save() #if everything is correct, this saves the form data to the db as new HappyPlace instance
            return redirect('thank_you') #redirects to thank you page
    else:
        form = HappyPlaceForm()  #if the request method is GET, a blank form is created

    return render(request, 'NewOrleans/fun.html', {'form': form}) #renders the fun.html template, passing the form instance to the template context. This allows form to be displayed whether it is new or one with errors

def thank_you(request):
    return render(request, 'NewOrleans/thank_you.html') #path for user to go to thank you page

def retro(request):
    #collect all items from the database
    items = HappyPlace.objects.all()
    #then pass database info to the template
    return render(request, 'NewOrleans/retro.html', {'items': items})

def details(request, pk):
    more = get_object_or_404(HappyPlace, pk=pk)
    return render(request, 'NewOrleans/details.html', {'more': more})

def edit(request, pk):
    #retrieves the user requested model item from the database or gives a 404 error
    place = get_object_or_404(HappyPlace, pk=pk)

    if request.method == 'POST':
        if 'delete' in request.POST:
            #if delete button is pressed, then delete that item
            place.delete()
            return redirect('retro') #takes user to retrospective page after item is deleted
        else:
            #this is the form for editing an item
            form = HappyPlaceForm(request.POST, instance=place)
            if form.is_valid():
                form.save()
                return redirect('retro') #redirects to retrospective after saving
    else:
        form = HappyPlaceForm(instance=place)

    return render(request, 'NewOrleans/edit.html', {'form': form, 'place':place})
