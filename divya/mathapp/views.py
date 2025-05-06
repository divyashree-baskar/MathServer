from django.shortcuts import render

def calculate_power(request):
    power = None
    intensity = None
    resistance = None
    if request.method == 'POST':
        try:
            intensity = float(request.POST.get('intensity'))
            resistance = float(request.POST.get('resistance'))
            power = round((intensity ** 2) * resistance, 2)
        except (TypeError, ValueError):
            power = 'Invalid input.'
    return render(request, 'mathapp/math.html', {'power': power, 'intensity': intensity, 'resistance': resistance})
