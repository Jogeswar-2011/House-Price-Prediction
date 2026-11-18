from django.shortcuts import render
import joblib
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

Basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
model_path = os.path.join(Basedir, 'model', 'house_price_model.pkl')
loaded_model = joblib.load(model_path)

@api_view(['POST'])
def predict_house_price(request):
    lot_area = request.data.get('LotArea')
    bedrooms = request.data.get('BedroomAbvGr')
    features = [[lot_area, bedrooms]]
    prediction = loaded_model.predict(features)
    return Response({'predicted_price': round(float(prediction[0]), 2)})