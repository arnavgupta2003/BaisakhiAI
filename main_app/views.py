from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import traceback
from rest_framework import status

# IMPORTS

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor 
from sklearn import metrics

# Data Frame for 2nd Service

ndf = pd.read_csv('main_app/csvfiles/yield_cleaned_2.csv')

ndf['Year'] = pd.Categorical(ndf['Year'], ordered = True)
ndf['State'] = pd.Categorical(ndf['State'], ordered = True)
ndf['District'] = pd.Categorical(ndf['District'], ordered = True)
ndf['Season'] = pd.Categorical(ndf['Season'], ordered = True)
ndf['Crop'] = pd.Categorical(ndf['Crop'], ordered = True)

years = (ndf['Year'].cat.categories)
states = (ndf['State'].cat.categories)
districts = (ndf['District'].cat.categories)
seasons = (ndf['Season'].cat.categories)
cropcats = (ndf['Crop'].cat.categories)

crplist = ['Arecanut','Arhar/Tur', 'Bajra', 'Banana', 'Barley','Black pepper', 'Cardamom', 'Cashewnut', 'Castor seed','Coconut','Coriander','Cotton','Cowpea(Lobia)','Dry chillies','Dry Ginger','Garlic','Ginger','Gram','Groundnut','Guar seed','Horse-gram','Jowar','Jute','Khesari','Linseed','Maize','Masoor','Mesta','Moong(Green Gram)','Moth','Niger seed','Oilseeds total','Onion','Other Cereals','Other Kharif pulses']


#Training Models

#Crop
df_crop = pd.read_csv('main_app/csvfiles/npk.csv')
X_crop = df_crop.drop(columns = 'label')
y_crop = df_crop['label']
X_train_crop, X_test_crop, y_train_crop, y_test_crop = train_test_split(X_crop, y_crop, test_size = 0.2, random_state=42)

knn_crop = KNeighborsClassifier(n_neighbors=3)
knn_crop.fit(X_train_crop, y_train_crop)
ac_crop = round(knn_crop.score(X_test_crop, y_test_crop) * 100, 2)

#Yeild
df_yeild = pd.read_csv('main_app/csvfiles/yield_processing_1.csv')
X_yeild = df_yeild.drop(columns=['Unnamed: 0', 'Yield' ], axis=1)
y_yeild = df_yeild['Yield']
X_train_yeild, X_test_yeild, y_train_yeild, y_test_yeild = train_test_split(X_yeild, y_yeild, test_size = 0.2, random_state=42)

reg_yeild = DecisionTreeRegressor(random_state = 42)
reg_yeild.fit(X_train_yeild,y_train_yeild)
ac_pred_yeild = reg_yeild.predict(X_test_yeild)
r2_yeild = metrics.r2_score(y_test_yeild, ac_pred_yeild)


# Create your views here.
def home(request):
    if request.GET :
        dict = request.GET
        try:
            #Pred Crop
            received_data_crop = [dict['nitrogen'], dict['phosphorus'], dict['potassium'], dict['temp'], dict['humidity'], dict['phval'], dict['rainfall']]
            testing_data_crop = [np.array(received_data_crop, dtype='float64')]
            final_pred_crop = knn_crop.predict(testing_data_crop)
            crop_name = str.capitalize(str(final_pred_crop[0]))
            crop_idx=0
            try:
                crop_idx = crplist.index(crop_name)
            except:
                crop_idx=0
            
            #Pred Yeild
            received_data_yeild = [dict['state'], dict['district'], crop_idx, dict['year'], dict['season']]
            testing_data_yeild = [np.array(received_data_yeild, dtype='float64')]
            final_pred_yeild = reg_yeild.predict(testing_data_yeild)

            passThrough = {
                'yield': round(final_pred_yeild[0], 3),
                'crop_name':crop_name,
                'accuracy': ac_crop,
                'netprod':round(float(dict['area']) * float(final_pred_yeild[0]))
            }
            return render(request, 'thanks-1.html', passThrough)

        except:
            traceback.print_exc()    
            return HttpResponse(404)
    else:
        # Add Prediction Years
        sam = pd.Index(['2020-21', '2021-22'])
        yearsNew = years.append(sam)

        # Send Data to Website
        context = {
            'states':states,
            'districts':districts,
            'years':yearsNew,
            'seasons':seasons,
        }
        return render(request, 'index.html', context)