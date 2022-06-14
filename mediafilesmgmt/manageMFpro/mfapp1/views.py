from django.shortcuts import render, redirect
from .forms import EmployeeForm
from mfapp1.models import Employee
# Create your views here.
def emp_View(request):
    form = EmployeeForm()
    template_name = 'mfapp1/emploform.html'

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showempinfo_url')
    context = {'form': form}
    return render(request, template_name, context)

def Showemp_View(request):
    data = Employee.objects.all()
    template_name ='mfapp1/showemp_info.html'
    context = {'obj' : data}
    return render(request, template_name, context)

def Update_View(request, id):
    data = Employee.objects.get(id = id)
    form = EmployeeForm(instance=data)
    template_name = 'mfapp1/Emploform.html'
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=data)
        form.is_valid()
        form.save()
        return redirect('showempinfo_url')
    return render(request, template_name, context)

def Delete_View(request, id):
    data = Employee.objects.get(id = id)
    template_name = 'mfapp1/confirmation.html'
    context = {'obj':data}
    if request.method == 'POST':
        data.delete()
        return redirect('showempinfo_url')
    return render(request, template_name, context)

# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# import io
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter

# def GenaratePDF(request):
#     buf = io.BytesIO()
#     c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob = c.beginText()
#     textob.setTextOrigin(inch,inch)
#     textob.setFont('Helvetica', 14)
#     lines =[]
#     farm = Employee.objects.all()

    # for f in farm:
    #     lines.append(f.emp_name)
    #     lines.append(f.profile)
    #     lines.append(f.salary)
    #     lines.append(f.email)
    #     lines.append(" ")

    # for line in lines:
    #     textob.textLine(line)

    # c.drawText(textob)
    # c.showPage()
    # c.save()

    # buf.seek(0)

    # return FileResponse(buf, as_attachment=True, filename='xyz.pdf')

# def perticularData(request, id):
#     buf = io.BytesIO()
#     c= canvas.Canvas(buf, pagesize=letter, bottomup=0)
#     textob = c.beginText()
#     textob.setTextOrigin(inch,inch)
#     textob.setFont('Helvetica', 14)

#     farm = Employee.objects.get(id=id)
#     NM=farm.emp_name
#     PR=farm.profile
#     SAL=farm.salary
#     ML=farm.email
   
#     lines=[NM,PR,SAL,ML]
    
    # for line in lines:
    #     textob.textLine(line)
    # c.drawText(textob)
    # c.showPage()
    # c.save()

    # buf.seek(0)

    # return FileResponse(buf, as_attachment=True, filename='xyz.pdf')
        
   









