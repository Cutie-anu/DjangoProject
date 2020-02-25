from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'newsApp/index.html')
def moviesinfo(request):
	head_msg='Latest Movies Information'
	msg1="Samantha acting with Sarvanand in Jaanu Movie"
	msg2="Hero nani is a natural star"
	msg3="Samantha acting with Sarvanand in Jaanu Movie"
	my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
	return render(request,'newsApp/news.html',context=my_dict)
def sportsinfo(request):
	head_msg='Latest Sports Information'
	msg1="Samantha acting with Sarvanand in Jaanu Movie"
	msg2="Hero nani is a natural star"
	msg3="Samantha acting with Sarvanand in Jaanu Movie"
	my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
	return render(request,'newsApp/news.html',context=my_dict)
def politicsinfo(request):
	head_msg='Latest Politics Information'
	msg1="Samantha acting with Sarvanand in Jaanu Movie"
	msg2="Hero nani is a natural star"
	msg3="Samantha acting with Sarvanand in Jaanu Movie"
	my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
	return render(request,'newsApp/news.html',context=my_dict)