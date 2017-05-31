"""
import scipy.optimize

fun = lambda x: (3 * (x[0] - 4) ** 2 + (x[1] - 2) ** 2)
x0 = [7.0, 5.0]
print(scipy.optimize.minimize(fun, x0, args=(), method='Nelder-Mead'))
"""

import matplotlib.pyplot as plot
import numpy as np
from matplotlib import pyplot
from One_dimensional_methods.Pauel import Pauel


# plot first condition (circle, minimum OUT of circle)
def plot_condition_1():
    plot.axes()
    circle_1 = plot.Circle((0, 0), radius=1.0, fc='y')
    plot.gca().add_patch(circle_1)


# plot second condition (circle, minimum IN circle)
def plot_condition_2():
    plot.axes()
    circle_2 = plot.Circle((0, 0), radius=2.0, fc='y')
    plot.gca().add_patch(circle_2)


# linear condition and plotting
def plot_condition_3():
    # pauel_method = Pauel([1, 0.1, -0.1], starting_point_p=1, delta_p=0.5, epsilon_p=10)
    pauel_method = Pauel([1, 0.1, -0.1], starting_point_p=1, delta_p=0.1, epsilon_p=0.1)
    answer = pauel_method.get_answer_by_pauel()
    print('Answer by Pauel:', answer)
    x = np.arange(-2, 2, .002)
    plot.plot(x, 1 - x)
    plot.plot(answer[0], answer[1], 'ro')


# circle in circle, minimun OUT of circles
def plot_condition_4():
    plot.axes()

    circle_1 = plot.Circle((0, 0), radius=1, fc='y')
    circle_2 = plot.Circle((0, 0), radius=0.7, fc='w')

    plot.gca().add_patch(circle_1)
    plot.gca().add_patch(circle_2)


# circle in circle, minimun IN of circles
def plot_condition_5():
    plot.axes()

    circle_1 = plot.Circle((1, 1), radius=1, fc='y')
    circle_2 = plot.Circle((1, 1), radius=0.7, fc='w')

    plot.gca().add_patch(circle_1)
    plot.gca().add_patch(circle_2)


def condition(x, y):
    # condition 1 - circle, minimum OUT of circle
    if x ** 2 + y ** 2 - 1 >= 0:
        pass
        # return 100

    # condition 2 - circle, minimum IN of circle
    if x ** 2 + y ** 2 - 4 >= 0:
        pass
        # return 100

    # condition 3 - linear
    if (x + y - 1 >= 0) and (y + 1 <= 0) or (-3 * x + y - 5 > 0):
        pass
        # return 100

    # condition 4 - circle in circle, center=(0, 0)
    if x ** 2 + y ** 2 - 1 > 0 and x ** 2 + y ** 2 - 0.49 > 0:
        pass
        # return 100

    # condition 5 - circle in circle, center=(1, 1)
    if x ** 2 + y ** 2 - 1 - 1 < 0 and x ** 2 + y ** 2 - 1 - 0.49 < 0:
        pass
        # return 100


class Nelder_Mid:
    ACCURACY = 3
    N = 2

    def __init__(self, points=None, thetta=None, betta=None, gamma=None, epsilon=0.00001, num_of_func_count=0):
        if thetta is None:
            thetta = 1.0
        if betta is None:
            betta = 0.5
        if gamma is None:
            gamma = 2.0
        if points is None:
            points = [-1.2, 0.0]
            # points = [7.0, 7.0]

        self.points_to_graph = []
        self.num_of_iterations = 0
        self.epsilon = epsilon
        self.thetta = thetta
        self.gamma = gamma
        self.betta = betta
        self.minus_betta = -self.betta
        self.num_of_func_count = num_of_func_count
        self.x = points
        self.M = []
        self.cycling_coef = 4

    # get 3 points of starting triangle
    def get_started_triangle(self):

        side = 1.6
        x_2 = [self.x[0] + side, self.x[1]]
        x_3 = [self.x[0] / 2.0 + x_2[0] / 2.0, -side]

        self.x = [[-1.2, 0.0], [x_2[0], x_2[1]], [x_3[0], x_3[1]]]

        # self.x = [[7.0, 5.0], [7.0, 7.0], [9.0, 7.0]]

    # find a value of function in point (x, y)
    def calculate_function(self, x, y):
        self.num_of_func_count += 1
        # return float(3 * (x - 4) ** 2 + (y - 2) ** 2)
        return float((x - 1) ** 2 + 100 * ((x ** 2 - y) ** 2))

    # increase print number of iteration
    def print_iteration(self):
        self.num_of_iterations += 1
        print('--- Iteration #', self.num_of_iterations, '---')

    def print_input_points(self):
        print('--- INPUT DATA ---')
        print(self.x[0][0], '   ', self.x[0][1])
        print(self.x[1][0], '   ', self.x[1][1])
        print(self.x[2][0], '   ', self.x[2][1])
        print('-' * 80)
        self.points_to_graph.append([[self.x[0][0], self.x[0][1]],
                                     [self.x[1][0], self.x[1][1]],
                                     [self.x[2][0], self.x[2][1]]])

    # printing points of triange to console AND adding points to list to plot the triangles
    def print_points(self):
        print(self.x[0][0], '   ', self.x[0][1])
        print(self.x[1][0], '   ', self.x[1][1])
        print(self.x[2][0], '   ', self.x[2][1])
        print('Number of counting function: ', self.num_of_func_count)
        print('-' * 80)
        self.points_to_graph.append([[self.x[0][0], self.x[0][1]],
                                     [self.x[1][0], self.x[1][1]],
                                     [self.x[2][0], self.x[2][1]]])

    # finding x center
    def find_x_c(self, g, l):
        return [(l[0] + g[0]) / self.N, (l[1] + g[1]) / self.N]

    # finding new x
    def find_x_H(self, h):
        return [h[0] + (1 + self.thetta) * (self.x[self.N + 1][0] - h[0]),
                h[1] + (1 + self.thetta) * (self.x[self.N + 1][1] - h[1])]

    # sort 3 points in decrease mode
    def sort_points(self):

        h, g, l = self.x[0], self.x[1], self.x[2]
        all_funcs = [self.calculate_function(*self.x[0]),
                     self.calculate_function(*self.x[1]),
                     self.calculate_function(*self.x[2])]

        for i in range(self.N + 1):
            # current_func = self.calculate_function(self.x[i][0], self.x[i][1])
            current_func = all_funcs[i]
            if self.calculate_function(h[0], h[1]) < current_func:
                h = self.x[i]
            if self.calculate_function(l[0], l[1]) > current_func:
                l = self.x[i]

        for i in range(self.N + 1):
            if self.x[i] != h and self.x[i] != l:
                g = self.x[i]
        return [h, g, l]

    # adding 3 points to check cycling
    def add_to_check_cycling(self, h, g, l):
        self.M.append(g[:])
        self.M.append(h[:])
        self.M.append(l[:])

    # do a compression of triangle with betta = 0.5
    def do_compression(self, h, x_c):
        print('---> Zjumannia (betta =', self.betta, ') <--')
        return [h[0] + (1 + self.betta) * (x_c[0] - h[0]), h[1] + (1 + self.betta) * (x_c[1] - h[1])]

    # do a compression of triangle with betta = -0.5
    def do_compression_minus(self, h, x_c):
        print('---> Zjumannia (betta =', self.minus_betta, ') <--')
        return [h[0] + (1 + self.minus_betta) * (x_c[0] - h[0]), h[1] + (1 + self.minus_betta) * (x_c[1] - h[1])]

    # do a pulling of triangle
    def do_pulling(self, h, x_c):
        return [h[0] + (1 + self.gamma) * (x_c[0] - h[0]), h[1] + (1 + self.gamma) * (x_c[1] - h[1])]

    # checking if points not cycling
    def is_cycling(self):
        if len(self.M) >= 9:
            for i in range(len(self.M)):
                number = 0
                for j in range(len(self.M)):
                    if self.M[j] == self.M[i]:
                        number += 1
                if number >= self.cycling_coef:
                    self.print_iteration()
                    print('THERE IS A CYCLE IN', self.M[i], 'Reduction ----->')
                    self.M = []
                    return True

    # do a reduction of triangle
    def do_reduction(self):
        for i in range(self.N):
            self.x[i] = [self.x[2][0] + (1 - self.betta) * (self.x[i][0] - self.x[2][0]),
                         self.x[2][1] + (1 - self.betta) * (self.x[i][1] - self.x[2][1])]

    # do a mirror of triangle
    def do_mirror(self, h, x_H):
        print('---> Vidobrajennia <--')
        h[0] = x_H[0]
        h[1] = x_H[1]
        return h

    # exit condition
    def calc_end_criteria(self):
        _sum = 0
        x_c = [(self.x[0][0] + self.x[1][0] + self.x[2][0]) / (self.N + 1),
               (self.x[0][1] + self.x[1][1] + self.x[2][1]) / (self.N + 1)]
        f_x_c = self.calculate_function(x_c[0], x_c[1])
        for k in range(self.N + 1):
            s1 = self.calculate_function(*self.x[k])
            _sum += (s1 - f_x_c) ** 2
        return _sum / (self.N + 1)
        # end = max(np.sqrt((self.x[0][0] - self.x[0][1]) ** 2 + (self.x[1][0] - self.x[1][1]) ** 2),
        #            np.sqrt((self.x[1][0] - self.x[1][1]) ** 2 + (self.x[2][0] - self.x[2][1]) ** 2),
        #            np.sqrt((self.x[2][0] - self.x[2][1]) ** 2 + (self.x[0][0] - self.x[0][1]) ** 2))
        # print('max = ', end)
        # return end

    # find minimal value and index
    def find_min_index(self, _min):
        m = 0
        for k in range(self.N + 1):
            current = self.calculate_function(*self.x[k])
            if current < _min:
                m = k
                _min = current
        return m, _min

    """Operations with graphics"""
    # plotting main grafic
    def plot_main_grafic(self):

        # x = np.arange(0, 10, .002)
        # plot.plot(x, np.sqrt(3 * ((x - 4) ** 2)) + 2)
        # plot.plot(4, 2, 'ro')

        x = np.arange(-2.0, 2.0, .002)
        plot.plot(x, ((x - 1) / 10) + x ** 2)
        plot.plot(1, 1, 'ro')

        # plot_condition_1()
        # plot_condition_2()  # 707
        # plot_condition_3()  # not working
        # plot_condition_4()  # Done
        # plot_condition_5()

    # plotting all triangles
    def plot_triangels(self):

        self.plot_main_grafic()

        x = []
        y = []
        number = 1
        repeating = []
        for j in range(len(self.points_to_graph)):
            for i in range(3):
                x.append(self.points_to_graph[j][i][0])
                y.append(self.points_to_graph[j][i][1])
                if [x[-1], y[-1]] in repeating:
                    pass
                else:
                    repeating.append([x[-1], y[-1]])
                    plot.annotate('{}'.format(number), xy=(x[-1], y[-1]))
                    number += 1

        plot.scatter(x, y)

        for three in self.points_to_graph:
            for point in three:
                for point2 in three:
                    pyplot.plot([point[0], point2[0]], [point[1], point2[1]], 'r')
        pyplot.show()

    # main finding cycle
    def find(self):
        _sum = self.epsilon + 1

        self.get_started_triangle()
        self.print_input_points()

        self.add_to_check_cycling(self.x[0], self.x[1], self.x[2])

        while _sum > self.epsilon:
            self.print_iteration()

            # Обнулюємо масив крім перших трьох значень( значень трикутника )
            self.x[self.N + 1:] = []

            self.x = self.sort_points()
            h, g, l = self.x[0], self.x[1], self.x[2]

            # Знаходимо х_ц і додаємо в кінець списку
            x_c = self.find_x_c(g, l)
            self.x.append(x_c)

            # Знаходимо х_Н і додаємо в кінець списку
            x_H = self.find_x_H(h)
            self.x.append(x_H)

            mass = condition(*x_H)
            if mass == 100:
                print(x_H)
                print('/' * 120)
                x_H[0], x_H[1] = 1000000, 1000000

            f_x_H = self.calculate_function(*x_H)

            # Перевірка на розтягнення
            if f_x_H <= self.calculate_function(*l):  # x_H < low
                h = self.do_pulling(h, x_c)
                print('--> Roztyagenie <--' * 10)
                self.x[0] = h

                # # Розтягнення
                # if self.calculate_function(*h) < f_x_H:
                #     print('--> Roztyagenie <--'*10)
                #     self.x[0] = h
                # else:
                #     print('kkk')
                #     self.x[0] = x_H

            # Відображення
            elif f_x_H <= self.calculate_function(*g):
                self.x[0] = self.do_mirror(h, x_H)

            # Зжимання
            elif f_x_H <= self.calculate_function(*h):
                self.x[0] = self.do_compression(h, x_c)
            elif f_x_H > self.calculate_function(*h):
                self.x[0] = self.do_compression_minus(h, x_c)

            self.add_to_check_cycling(self.x[0], self.x[1], self.x[2])
            self.print_points()

            """ Якщо одна точка стоїть на місті М=4 раз """
            if self.is_cycling():
                self.do_reduction()
                print('-Reduction- ' * 5)
                self.print_points()
                self.add_to_check_cycling(self.x[0], self.x[1], self.x[2])

            _sum = self.calc_end_criteria()

        _min = self.calculate_function(*self.x[0])
        m, _min = self.find_min_index(_min)
        print('f(', self.x[m][0], ',', self.x[m][1], ') =', _min)


if __name__ == '__main__':
    Nelder_Mid = Nelder_Mid()
    Nelder_Mid.find()
    Nelder_Mid.plot_triangels()
