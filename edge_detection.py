def nabla(I, k, j):
    '''
    |(k  , j)    (k,    j + 1)|
    |(k+1, j)    (k + 1, j + 1)|
    '''
    i1 = (abs(I[k + 1][j] - I[k][j]) + abs(I[k + 1][j + 1] - I[k][j + 1])) >> 2  # horizontal direction
    i2 = (abs(I[k][j + 1] - I[k][j]) + abs(I[k + 1][j + 1] - I[k + 1][j])) >> 2  # vertical direction
    return (pow(i1, 2) + pow(i2, 2)) ** 0.5


def edge_detection(img, epsilon):
    m = len(img)
    n = len(img[0])
    edge_image = [[0 for j in range(n)] for i in range(m)]
    for k in range(m - 1):
        for l in range(n - 1):
            if nabla(img, k, l) >= epsilon:
                edge_image[k][l] = 1
    return edge_image


if __name__ == "__main__":
    img = [
        [0, 0, 5, 0],
        [0, 0, 4, 0],
        [0, 0, 6, 0],
        [0, 0, 10, 0],
        [0, 0, 0, 0]
    ]
    edges = edge_detection(img, epsilon=2)

