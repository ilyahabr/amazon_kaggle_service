from dependency_injector import containers, providers

from src.services.amazon_classifier import AmazonClassifier


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    amazon_classifier = providers.Factory(
        AmazonClassifier,
        config=config.services.amazon_classifier,
    )
