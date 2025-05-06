# Ex.05 Design a Website for Server Side Processing
## Date:06/05/2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
math.html

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lamp Filament Power Calculator</title>
</head>
<body>
    <h1>Calculate Lamp Filament Power</h1>
    <form method="post">
        {% csrf_token %}
        <label for="intensity">Intensity (Amps):</label>
        <input type="number" step="any" name="intensity" id="intensity" required><br><br>

        <label for="resistance">Resistance (Ohms):</label>
        <input type="number" step="any" name="resistance" id="resistance" required><br><br>

        <button type="submit">Calculate Power</button>
    </form>

    {% if power is not None %}
        <h2>Result</h2>
        <p>Intensity (I): {{ intensity }} Amps</p>
        <p>Resistance (R): {{ resistance }} Ohms</p>
        <p><strong>Power (P): {{ power }} Watts</strong></p>
    {% endif %}
</body>
</html>
 
 views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.calculate_power, name='calculate_power'),
]
```


## SERVER SIDE PROCESSING:
![alt text](<Screenshot 2025-05-06 114448.png>)


## HOMEPAGE:
![alt text](<Screenshot 2025-05-06 114507.png>)

## RESULT:
The program for performing server side processing is completed successfully.
