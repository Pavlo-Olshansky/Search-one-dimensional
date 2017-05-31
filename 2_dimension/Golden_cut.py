import math

from Sven_method import Find_Interval


class Golden_cut(Find_Interval):
    def __init__(self, starting_point_g=None, delta_g=None, epsilon_g=None):
        super().__init__(starting_point_g, delta_g)
        self.epsilon_g = epsilon_g

    def get_x1(self, interval, L):
        return [interval[0][0] + 0.382 * L, interval[0][1] + 0.382 * L]

    def get_x2(self, interval, L):
        return [interval[0][0] + 0.618 * L, interval[0][0] + 0.618 * L]

    def get_epsilon(self):
        if self.epsilon_g is None:
            self.epsilon_g = float(input('Input Epsilon: '))

    def find_interval(self, interval, SvenMethod, L, x_1_last_iter=None, x_2_last_iter=None):

        global x_2_next_iter, x_1_next_iter
        x1, x2 = x_1_last_iter, x_2_last_iter

        if x1 is None:
            x1 = self.get_x1(interval, L)
        if x2 is None:
            x2 = self.get_x2(interval, L)

        if SvenMethod.func(*x1) <= SvenMethod.func(*x2):  # f(x1) <= f(x2)
            interval = [interval[0], x2]
            x_2_next_iter = x1
            x_1_next_iter = None
        else:  # f(x1) > f(x2)
            interval = [x1, interval[1]]
            x_1_next_iter = x2
            x_2_next_iter = None
        L = math.sqrt((interval[1][0] - interval[0][0])**2 + (interval[1][1] - interval[0][1])**2)
        print('L=', L, 'interval=', interval)
        if L <= self.epsilon_g:
            return interval
        else:
            return self.find_interval(interval, SvenMethod, L, x_1_last_iter=x_1_next_iter, x_2_last_iter=x_2_next_iter)

    def golden_cut(self):
        SvenMethod = Find_Interval(self.starting_point, self.delta)
        interval = SvenMethod.finder()
        print('SVEN =', interval)
        self.get_epsilon()

        return self.find_interval(interval, SvenMethod, math.sqrt((interval[1][0] - interval[0][0]) ** 2 +
                                                                  (interval[1][1] - interval[0][1]) ** 2))


if __name__ == '__main__':
    # golden_cut = Golden_cut([1, -200, 10000], 30, 5, 10)
    # print('Sven method interval: ', golden_cut.finder(), '\nGolden cut answer: ', golden_cut.golden_cut())

    golden_cut_2 = Golden_cut()
    print('Sven method interval: ', golden_cut_2.finder(), '\nGolden cut method answer: ', golden_cut_2.golden_cut())

    input()
