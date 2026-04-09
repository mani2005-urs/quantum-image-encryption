import numpy as np

def arnold_transform(img, iterations=1):
    n = img.shape[0]
    result = img.copy()

    for _ in range(iterations):
        new_img = np.zeros_like(result)
        for x in range(n):
            for y in range(n):
                x_new = (x + y) % n
                y_new = (x + 2*y) % n
                new_img[x_new, y_new] = result[x, y]
        result = new_img

    return result


def inverse_arnold(img, iterations=1):
    n = img.shape[0]
    result = img.copy()

    for _ in range(iterations):
        new_img = np.zeros_like(result)
        for x in range(n):
            for y in range(n):
                x_new = (2*x - y) % n
                y_new = (-x + y) % n
                new_img[x_new, y_new] = result[x, y]
        result = new_img

    return result