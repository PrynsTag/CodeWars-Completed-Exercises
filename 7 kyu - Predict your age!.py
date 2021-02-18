from math import sqrt

def predict_age(*args):
    product = list(map(lambda x: x * x, args))
    sumValue = sum(product)
    sqrtResult = sqrt(sumValue)

    return int(sqrtResult / 2)

if __name__ == '__main__':
    print(predict_age(65, 60, 75, 55, 60, 63, 64, 45) == 86)