import math
from Sven_method import Find_Interval


class Dichotomy(Find_Interval):
    def __init__(self, starting_point_d=None, delta_d=None, epsilon=None):
        super().__init__(starting_point_d, delta_d)
        self.epsilon = epsilon

    def get_atrs(self):
        if self.epsilon is None:
            self.epsilon = float(input('Enter an Epsilon: '))
        return self.epsilon

    def half_interval(self, interval, Sven_Method):
        while True:
            center = [(interval[0][0] + interval[1][0]) / 2, (interval[0][1] + interval[1][1]) / 2]  # correct
            right_center = [(center[0] + interval[1][0]) / 2, (center[1] + interval[1][1]) / 2]
            left_center = [(center[0] + interval[0][0]) / 2, (center[1] + interval[0][1]) / 2]
            # print('interval, center', interval, center)

            func_center = Sven_Method.func(*center)
            func_right_center = Sven_Method.func(*right_center)
            func_left_center = Sven_Method.func(*left_center)

            if func_left_center >= func_center >= func_right_center:
                interval = [[round(center[0], self.ACCURACY), round(center[0], self.ACCURACY)],
                            [round(interval[1][0], self.ACCURACY), round(interval[1][1], self.ACCURACY)]]

            elif func_right_center >= func_center >= func_left_center:
                interval = [[round(interval[0][0], self.ACCURACY), round(interval[0][1], self.ACCURACY)],
                            [round(center[0], self.ACCURACY), round(center[1], self.ACCURACY)]]

            elif func_right_center >= func_center and func_left_center >= func_center:
                interval = [[round(left_center[0], self.ACCURACY), round(left_center[1], self.ACCURACY)],
                            [round(right_center[0], self.ACCURACY), round(right_center[1], self.ACCURACY)]]

            print('Current interval =', interval)

            if math.sqrt((interval[0][0] - interval[1][0]) ** 2 + (interval[0][1] - interval[1][1]) ** 2) <= \
                    self.epsilon:
                print('Done')
                return interval
            else:
                return self.half_interval(interval, Sven_Method)

    def search_by_dichotome(self):
        Sven_Method = Find_Interval(self.starting_point, self.delta)
        interval = Sven_Method.finder()
        self.get_atrs()

        new_interval = self.half_interval(interval, Sven_Method)
        return new_interval


if __name__ == '__main__':

    # print('Answer:',  Dichotomy([1, -200, 10000], 30, 5, 10).search_by_dichotome())
    # Dichotomy([1, -200, 10000], 30, 5, 10).finder()

    dichotomy = Dichotomy()
    print('Sven method interval: ', dichotomy.finder(),
          '\nDichotomy method answer: ', dichotomy.search_by_dichotome())
    input()
