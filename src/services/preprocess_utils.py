import typing as tp

import cv2
import numpy as np
import torch

MAX_UINT8 = 255


def preprocess_image(image: np.ndarray, target_image_size: tp.Tuple[int, int]) -> torch.Tensor:
    """Препроцессинг имаджнетом.

    :param image: RGB изображение;
    :param target_image_size: целевой размер изображения;
    :return: батч с одним изображением.
    """
    image = image.astype(np.float32)
    image = cv2.resize(image, target_image_size) / MAX_UINT8
    image = np.transpose(image, (2, 0, 1))
    image -= np.array([0.485, 0.456, 0.406])[:, None, None]
    image /= np.array([0.229, 0.224, 0.225])[:, None, None]
    return torch.from_numpy(image)[None]
