from django.shortcuts import render

from .forms import JobSeekerForm,VacancyForm
from .models import Contact,Service,JobPost,TimeSheet
from django.shortcuts import get_object_or_404



def index(request):
    page_info = Service.objects.all()
    # print(page_info)
    content = {
        "page_info" :page_info
    }
    return render(request,'website/index.html',content)

def about(request):
    about_us = Service.objects.get(title="About Us")
    points = about_us.points.all()
    context = {
        "about_us": about_us,
        "points": points
    }
    return render(request,'website/about.html', context)


def service(request):
    return render(request,'website/service.html')


def homecare(request):
    home_care = Service.objects.get(title="Home Care")
    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/homecare.html',context)

def job_seeker(request):
    form = JobSeekerForm()
    if request.method == 'POST':
        form = JobSeekerForm(request.POST,request.FILES)
        # print(form.errors)
        if form.is_valid():
            # print("it was here")
            form.save()
            return render(request,'website/job_seeker.html',{'form':form})
    return render(request,'website/job_seeker.html',{'form':form})

def training(request):
    home_care = get_object_or_404(Service,title="Training")

    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/training.html',context)


def time_sheet(request):
    timesheet = TimeSheet.objects.first()
    context = {
        "timesheet":timesheet,
    }
    # print(timesheet)
    return render(request,'website/timesheet.html',context) 



def aged_care(request):
    home_care = get_object_or_404(Service,title="Aged Care")

    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/aged_care.html',context)



def find_jobs(request):
    listed_jobs = JobPost.objects.all()
    context = {
        "jobs":listed_jobs
    }
    return render(request,'website/find_job.html',context)

def job_detail(request,pk):
    job = get_object_or_404(JobPost,pk=pk)
    # print(job.content)
    context = {
        "job":job
    }
    return render(request,'website/job_detail.html',context)


def disability_support(request):
    home_care = get_object_or_404(Service,title="Disability Support")

    points = home_care.points.all()
    context = {
        "home_care": home_care,
        "points": points
    }
    return render(request,'website/disability_support.html',context)


def vacancy(request):
    form = VacancyForm()
    if request.method == 'POST':
        form = VacancyForm(request.POST,request.FILES)
        # print(form.errors)
        if form.is_valid():
            form.save()
            return render(request,'website/vacancy.html',{'form':form})
    return render(request,'website/vacancy.html',{'form':form})


def contact(request):
    return render(request, 'website/contact.html')


def save_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        form_data = Contact(name=name,email=email,phone_number=phone_number,subject=subject,message=message)
        form_data.save()
        
    return render(request, 'website/contact.html')


def privacy_policy(request):
    return render(request, 'website/privacy_policy.html')
    




