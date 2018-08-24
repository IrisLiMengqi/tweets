from django.shortcuts import render

# Create your views here.
#Create

#Retrieve
def tweet_detail_view(request, id = 1):
	return render(request, "tweet_detail_view.html", {})
def tweet_list_view(request):
	return render(request, "tweet_list_view.html", {})
#Update

#Deletes

#List/Search