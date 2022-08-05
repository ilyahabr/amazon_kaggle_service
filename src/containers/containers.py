from dependency_injector import containers, providers

from dev_amazon.src.services.amazon_classifier import AmazonClassifier


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    amazon_classifier = providers.Singleton(
        AmazonClassifier,
        config=config.services.amazon_classifier,
    )
