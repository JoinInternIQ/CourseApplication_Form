from django.shortcuts import render, redirect
from .forms import InternshipApplicationForm
from .models import InternshipApplication
from django.core.mail import send_mail

def internship_form_view(request):
    if request.method == 'POST':
        form = InternshipApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)

            # Save the form
            instance.save()

            # Email setup
            subject = '📬 New Internship Application Submitted'
            message = f"""
A new internship application has been submitted.

Name: {instance.name}
Gender: {instance.gender}
Date of Birth: {instance.dob}
Phone: {instance.phone}
Email: {instance.email}
Address: {instance.address}


Department: {instance.department}
Year of Study: {instance.year_of_study}
Batch: {instance.batch_from} - {instance.batch_to}
College: {instance.college_name}
Preferred Domain: {instance.domains}

            """

            admin_email = 'joininterniq@gmail.com'
            send_mail(
                subject,
                message,
                'joininterniq@gmail.com',
                [admin_email],
                fail_silently=False
            )

            return redirect('success')
        else:
            # ✅ Now it's safe
            print("Form is not valid")
            print(form.errors)
    else:
        form = InternshipApplicationForm()

    return render(request, 'internship_form.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')
