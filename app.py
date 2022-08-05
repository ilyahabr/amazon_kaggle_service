import uvicorn
from fastapi import FastAPI
from omegaconf import OmegaConf

from src.containers.containers import AppContainer
from src.routes.routers import router as app_router
from src.routes import amazon as amazon_routes


def create_app() -> FastAPI:
    container = AppContainer()
    cfg = OmegaConf.load('config/config.yml')
    container.config.from_dict(cfg)
    container.wire([amazon_routes])

    app = FastAPI()
    set_routers(app)
    return app


def set_routers(app: FastAPI):
    app.include_router(app_router, prefix='/amazon', tags=['amazon'])


app = create_app()

if __name__ == '__main__':
    uvicorn.run(app, port=2444, host='localhost')
