import numpy as np
from PIL import Image


def cutout_center(image: np.ndarray, width=30, height=30):
    """ 切割出图像中心
    :param image: 输入图像
    :param width: 中心部分宽度(px)
    :param height: 中心部分高度(px)
    """
    im = np.asarray(image)
    shape = np.shape(image)
    center = (shape[0] / 2, shape[1] / 2)
    half_width = width / 2
    half_height = height / 2
    limit_dim1 = (
        int(center[0] - half_height),
        int(center[0] + half_height)
    )
    limit_dim2 = (
        int(center[1] - half_width),
        int(center[1] + half_width)
    )
    cutted = im[limit_dim1[0]:limit_dim1[1], limit_dim2[0]:limit_dim2[1]]
    return cutted


def split_by_color_distance(
    image: np.ndarray,
    center: np.ndarray,
    distance: float,
    measure=lambda x, y: np.linalg.norm(x - y, axis=-1)):
    """ 按RGB颜色距离分割图像
    :param image: 图像，arraylike
    :param center: 中心点
    :param distance: 距离参数
    :param measure: 距离计算方法，默认欧氏距离
    """

    # check data
    im = np.asarray(image)
    center = np.asarray(center)
    im_shape = np.shape(im)
    center_shape = np.shape(center)

    assert len(im_shape) == 3, "We only support rgb images!"
    assert len(center_shape) == 1

    if center_shape[0] == 1:
        center = np.array([center[0] for _ in range(3)])
    else:
        assert center_shape[0] == 3
    
    # process
    processed = measure(image, center)
    filtered = processed < distance

    return filtered

