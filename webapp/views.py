from django.shortcuts import render, HttpResponse # To render websites
import json # To handle json objects
import requests # To fetch api

# Api urls
url_breastcancer = 'https://breastcancerprediction.confusedsoul.repl.co/breastcancer_prediction'
url_diabetes = 'https://diabetesprediction.confusedsoul.repl.co/diabetes_prediction'

# Views functions
def index(request):
    return render(request, 'templates/index.html')

def about(request):
    return render(request, 'templates/about.html')

def bmi(request):
    return render(request, 'templates/bmi.html')

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact Page")

def diabetes(request):
  pg = request.POST.get('pgdb', '')  # Get the posted values or empty strings if not provided
  gl = request.POST.get('gldb', '')
  bm = request.POST.get('bmidb', '')
  age = request.POST.get('agedb', '')

  if request.method == 'POST':
    input = {                        # Creating input dictionary
        'Pregnancies' : pg,
        'Glucose' : gl,
        'BMI' : bm,
        'Age' : age
    }
    inp = json.dumps(input)         # Creating json input
    response = requests.post(url_diabetes, data=inp) # Getting response
    result = response.text
  else:
    result = None

  # Pass the form data and result to the template
  return render(request, 'templates/diabetes.html', {'result': result, 'pg': pg, 'gl': gl, 'bm': bm, 'age': age})

def breastcancer(request):
    rm = request.POST.get('rm', '')
    pm = request.POST.get('pm', '')
    am = request.POST.get('am', '')
    cm = request.POST.get('cm', '')
    cnm = request.POST.get('cnm', '')
    cpm = request.POST.get('cpm', '')

    if request.method == 'POST':
        input = {
            'radius': rm,
            'perimeter': pm,
            'area': am,
            'compactness': cm,
            'concativity': cnm,
            'concave_points': cpm
        }
        inp = json.dumps(input)
        response = requests.post(url_breastcancer, data=inp)
        result = response.text
    else:
        result = None

    # Pass the form data and result to the template
    return render(
        request, 'templates/breastcancer.html', {
            'result': result,
            'rm': rm,
            'pm': pm,
            'am': am,
            'cm': cm,
            'cnm': cnm,
            'cpm': cpm
        })