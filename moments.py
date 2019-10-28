def moments(image):
    mu_00 = mu_10 = mu_01 = mu_11 = 0
    for x in range(1, len(image) + 1):
        for y in range(1, len(image[0]) + 1):
            mu_00 += image[x - 1][y - 1]
            mu_10 += image[x - 1][y - 1] * x
            mu_01 += image[x - 1][y - 1] * y
            mu_11 += image[x - 1][y - 1] * x * y
    return [mu_00, mu_01, mu_10, mu_11]

