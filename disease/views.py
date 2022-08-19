from django.shortcuts import render
import pickle
from disease.models import breastCancer
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
# Create your views here.

def predict(values, dic):
    if len(values) == 8:
        model = pickle.load(open('models/diabetes.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('models/breast_cancer.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('models/kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('models/liver.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]



def home(request):
    # if request.method=='POST':

    return render(request,'home.html')

def cancerPage(request):
    if request.method=='POST':
        radius_mean = request.POST['radius_mean']
        texture_mean = request.POST['texture_mean']
        perimeter_mean = request.POST['perimeter_mean']
        area_mean = request.POST['area_mean']
        smoothness_mean = request.POST['smoothness_mean']
        compactness_mean = request.POST['compactness_mean']
        concavity_mean = request.POST['concavity_mean']
        concave_points_mean = request.POST['concave_points_mean']
        symmetry_mean = request.POST['symmetry_mean']





        data = breastCancer.objects.create(
                                            radius_mean=radius_mean,
                                            texture_mean=texture_mean,
                                            perimeter_mean=perimeter_mean,
                                            area_mean=area_mean,
                                            smoothness_mean=smoothness_mean,
                                            compactness_mean=compactness_mean,
                                            concavity_mean=concavity_mean,
                                            concave_points_mean=concave_points_mean,
                                            symmetry_mean = symmetry_mean,




                                            )
        data.save()
    return render(request,'breast_cancer.html')

def heartPage(request):
    return render(request,'heart.html')

def kidneyPage(request):
    return render(request,'kidney.html')

def liverPage(request):
    return render(request,'liver.html')

def malariaPage(request):
    return render(request,'malaria.html')

def diabetesPage(request):
    return render(request,'diabetes.html')

def pneumoniaPage(request):
    return render(request,'pneumonia.html')


def predictPage(request):
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except:
        message = { 'msg' : "Please enter valid Data"}
        return render(request,"home.html", message)

    return render(request,'predict.html', pred)

def malariapredictPage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image'])
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,3))
                img = img.astype(np.float64)
                model = load_model("models/malaria.h5")
                pred = np.argmax(model.predict(img)[0])
        except:
            message = "Please upload an Image"
            return render(request,'malaria.html', message = message)
    return render(request,'malaria_predict.html', pred = pred)

def pneumoniapredictPage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,1))
                img = img / 255.0
                model = load_model("models/pneumonia.h5")
                pred = np.argmax(model.predict(img)[0])
        except:
            message = "Please upload an Image"
            return render(request,'pneumonia.html', message = message)
    return render(request,'pneumonia_predict.html', pred = pred)