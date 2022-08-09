from fastapi.testclient import TestClient
from http import HTTPStatus


def test_amazon_list(client: TestClient):
    response = client.get('/amazon/amazon_classes')
    assert response.status_code == HTTPStatus.OK

    amazon_classes = response.json()['amazon_classes']

    assert isinstance(amazon_classes, list)


def test_predict(client: TestClient, sample_image_bytes: bytes):
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/amazon/predict', files=files)

    assert response.status_code == HTTPStatus.OK

    predicted_amazon_classes = response.json()['amazon_classes']

    assert isinstance(predicted_amazon_classes, list)


def test_predict_proba(client: TestClient, sample_image_bytes: bytes):
    files = {
        'image': sample_image_bytes,
    }
    response = client.post('/amazon/predict_proba', files=files)

    assert response.status_code == HTTPStatus.OK

    amazon2prob = response.json()

    for amazon_prob in amazon2prob.values():
        assert amazon_prob <= 1

