from django.shortcuts import render
from .models import Calculator

def calculate_interest(request):
    if request.method == 'POST':
        principal = float(request.POST.get('principal'))
        rate = float(request.POST.get('rate'))
        time = float(request.POST.get('time'))
        
        # Calculate interest
        interest = (principal * rate * time) / 100
        
        # Save data to database
        Calculator.objects.create(
            principal_amount=principal,
            interest_rate=rate,
            time_period=time
        )
        
        return render(request, 'result.html', {'interest': interest})
    return render(request, 'index.html')
