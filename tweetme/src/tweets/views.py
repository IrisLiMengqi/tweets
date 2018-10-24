from django.shortcuts import render
from .models import Tweet
from django.views.generic import DetailView, ListView
# Create your views here.
#Create

#Retrieve

class TweetDetailView(DetailView):
	queryset = Tweet.objects.all()

	def get_object(self):
		return Tweet.objects.get(id=1)
class TweetListView(ListView):
	queryset = Tweet.objects.all()

def tweet_detail_view(request, id = 1):
	obj = Tweet.objects.get(id=id) #Get from database
	print(obj)
	context = {
		"object": obj
		
	}
	
	return render(request, "tweets/detail_view.html", context)

def tweet_list_view(request):
	queryset = Tweet.objects.all()
	print(queryset)
	for obj in queryset:
		print(obj.content)
	context = {
		"objects_list": queryset
	}
	return render(request, "tweets/list_view.html", context)
#Update

#Deletes

#List/Search