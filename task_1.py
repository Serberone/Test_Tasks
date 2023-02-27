import matplotlib.pyplot as plt
import random

#тестовый набор данных
example_train_set = [(0, 1),
    (2, 2),
    (4, 3),
    (9, 8),
    (3, 5)]

xs, ys = zip(*example_train_set)

learning_rate = 0.001

#фунуция для определения правильности предсказания
def loss(predict, actual):
    losses = [(predict[i] - actual[i])**2 for i in range(len(predict))]
    return sum(losses) / len(predict) / 2

#коэф-ы линейной регрессии
a = random.random() * 0.01
b = random.random() * 0.01

#функция для предсказания
def predict(xs):
    preds = [a * x + b for x in xs]
    return preds

loss_hist = []
for i in range(1000):
    preds = predict(xs)
    l = loss(preds, ys)
    loss_hist.append(l)
    da = 0
    db = 0
    for i in range(len(xs)):
        da += xs[i] * (preds[i] - ys[i])
        db += (preds[i] - ys[i])
    da /= len(xs)
    db /= len(xs)
    
    a -= da * learning_rate
    b -= db * learning_rate
    
plt.plot(loss_hist)
plt.show()