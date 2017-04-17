from Sven_method import Find_Interval


class Dichotomy(Find_Interval):
    def __init__(self, coeffs_d=None, starting_point_d=None, delta_d=None, epsilon=None):
        super().__init__(coeffs_d, starting_point_d, delta_d)
        self.epsilon = epsilon

    def get_atrs(self):
        if self.epsilon is None:
            self.epsilon = float(input('Enter an Epsilon: '))
        return self.epsilon

    def half_interval(self, interval, Sven_Method):
        while True:
            center = (interval[0] + interval[1]) / 2
            right_center = (center + interval[1]) / 2
            left_center = (center + interval[0]) / 2

            func_center = Sven_Method.func(center)
            func_right_center = Sven_Method.func(right_center)
            func_left_center = Sven_Method.func(left_center)

            if func_left_center >= func_center >= func_right_center:
                interval = (round(center, self.ACCURACY), round(interval[1], self.ACCURACY))

            elif func_right_center >= func_center >= func_left_center:
                interval = (round(interval[0], self.ACCURACY), round(center, self.ACCURACY))

            elif func_right_center >= func_center and func_left_center >= func_center:
                interval = (round(left_center, self.ACCURACY), round(right_center, self.ACCURACY))

            print('Current interval =', interval)

            if interval[1] - interval[0] <= self.epsilon:
                print('Done')
                return interval
            else:
                return self.half_interval(interval, Sven_Method)

    def search_by_dichotome(self):
        Sven_Method = Find_Interval(self.coeffs, self.starting_point, self.delta)
        interval = Sven_Method.finder()
        self.get_atrs()

        new_interval = self.half_interval(interval, Sven_Method)
        return new_interval


if __name__ == '__main__':

    print('Answer:',  Dichotomy([1, -200, 10000], 30, 5, 10).search_by_dichotome())
    # Dichotomy([1, -200, 10000], 30, 5, 10).finder()
    #
    # dichotomy = Dichotomy()
    # print('Sven method interval: ', dichotomy.finder(), '\nDichotomy method answer: ', dichotomy.search_by_dichotome())
    input()
