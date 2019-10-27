def moments(image):
    mu_00 = mu_10 = mu_01 = mu_11 = 0
    for x in range(len(image)):
        for y in range(len(image[0])):
            mu_00 += image[i][j]
            mu_10 += image[i][j] * x
            mu_01 += image[i][j] * y
            mu_11 += image[i][j] * x * y
    return [mu_00, mu_01, mu_10, mu_11]

