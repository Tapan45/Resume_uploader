from django.shortcuts import render,get_object_or_404,redirect

def function(request):
    return render(request,"home.html")

from .models import resume_Table
def resumedata(request):
    if request.method=='POST':
    
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        locality=request.POST.get('locality')
        city=request.POST.get('city')
        pincode =request.POST.get('pin')
        state=request.POST.get('state')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        
        jobcity = request.POST.getlist('jobcity[]')
        
        profile_image = request.FILES.get('profile_image')
        my_file = request.FILES.get('my_file')
        
        print("name")
       
        resume_Table.objects.create(
            name=name,
            dob=dob,
            gender=gender,
            locality=locality,
            city=city,
            pin=pincode,
            state=state,
            mobile=mobile,
            email=email,
            job_city=jobcity,
            profile_image=profile_image,
            my_file=my_file
        )
        
    return render (request,"home.html")

def show_resume (request):
    obj =resume_Table.objects.all()
    context={
        "Resume" : obj
    }
    return render (request,"home.html",context)

def candidate_detail(request, candidate_id):
    candidate = get_object_or_404(resume_Table, id=candidate_id)
    return render(request, 'candidate.html', {'candidate': candidate})

def delete_data(request, candi_id):
    object = get_object_or_404(resume_Table,id = candi_id)
    object.delete()
    return redirect('show_resume')

def update_data (request,candidate_id):
    obj=get_object_or_404(resume_Table,id=candidate_id)
    
    if request.method == 'POST':
        
        update_name=request.POST.get('name')
        update_dob=request.POST.get('dob')
        update_gender=request.POST.get('gender')
        update_locality=request.POST.get('locality')
        update_city=request.POST.get('city')
        update_pincode=request.POST.get('pin')
        update_state=request.POST.get('state')
        update_mobile=request.POST.get('mobile')
        update_email=request.POST.get('email')
       
        update_jobcity=request.POST.get('jobcity[]')
        update_profile_image =request.FILES.get('profile_image')
        update_my_file=request.FILES.get('my_file')
        
        
        obj.name=update_name
        obj.dob=update_dob
        obj.gender=update_gender
        obj.locality=update_locality
        obj.city=update_city
        obj.pin=update_pincode
        obj.state=update_state
        obj.mobile=update_mobile
        obj.email=update_email
        obj.job_city=update_jobcity
        obj.profile_image=update_profile_image
        obj.my_file=update_my_file
        
        obj.save()
        
        return redirect('show_resume')
    
     
        
        
    context = {
        "obj" : obj
    }
    
    return render(request , "update.html", context)