import os.path

import cv2
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from omegaconf import OmegaConf

from app import set_routers
from src.containers.containers import AppContainer

TESTS_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='session')
def app_config():
    return OmegaConf.load(os.path.join(TESTS_DIR, 'test_config.yml'))


@pytest.fixture
def app_container(app_config):
    container = AppContainer()
    container.config.from_dict(app_config)
    return container


@pytest.fixture
def sample_image_np():
    img = cv2.imread(os.path.join(TESTS_DIR, 'images', 'train_32878.jpg'))
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


@pytest.fixture
def sample_image_bytes():
    with open(os.path.join(TESTS_DIR, 'images', 'train_32878.jpg'), 'rb') as f:
        return f.read()


@pytest.fixture
def test_app():
    app = FastAPI()
    set_routers(app)
    return app


@pytest.fixture
def client(test_app):
    return TestClient(test_app)

