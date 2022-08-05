import cv2
import numpy as np
from dependency_injector.wiring import Provide, inject
from fastapi import Depends, File

from dev_amazon.src.containers.containers import AppContainer
from dev_amazon.src.routes.routers import router
from dev_amazon.src.services.amazon_classifier import AmazonClassifier


@router.get('/amazon_classes')
@inject
def amazon_classes_list(service: AmazonClassifier = Depends(Provide[AppContainer.amazon_classifier])):
    return {
        'amazon_classes': service.classes,
    }


@router.post('/predict')
@inject
def predict(
    image: bytes = File(),
    service: AmazonClassifier = Depends(Provide[AppContainer.amazon_classifier]),
):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    amazon_classes = service.predict(img)

    return {'amazon_classes': amazon_classes}


@router.post('/predict_proba')
@inject
def predict_proba(
    image: bytes = File(),
    service: AmazonClassifier = Depends(Provide[AppContainer.amazon_classifier]),
):
    img = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    return service.predict_proba(img)


@router.get('/health_check')
def health_check():
    return 'OK'
