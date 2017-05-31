
class Find_Interval:
    ACCURACY = 3

    def __init__(self, starting_point=None, delta=None):

        if delta is None:
            delta = [0, -3.9]
        if starting_point is None:
            starting_point = [27.4, 27.4]
        self.starting_point = starting_point
        self.delta = delta

    def func(self, x1, x2):
        return (x1 - 18)**2 + x1*x2 + 4*(x2)**2

    def walker_right(self):
        combo = 2
        count_delta = 3

        while self.func(self.starting_point[0] + (self.delta[0] * (count_delta - combo)),
                        self.starting_point[1] + (self.delta[1]) * (count_delta - combo)) > \
                self.func(self.starting_point[0] + (self.delta[0] * count_delta),
                          self.starting_point[1] + (self.delta[1] * count_delta)):
            combo *= 2
            count_delta += combo

        x_break = [self.starting_point[0] + self.delta[0] * count_delta,
                   self.starting_point[1] + self.delta[1] * count_delta]
        x_before_break = [self.starting_point[0] + self.delta[0] * (count_delta - combo / 2),
                          self.starting_point[1] + self.delta[1] * (count_delta - combo / 2)]
        x_before_before_break = [self.starting_point[0] + self.delta[0] * (count_delta - combo),
                                 self.starting_point[1] + self.delta[1] * (count_delta - combo)]
        print('x_b L:', x_break, x_before_break, x_before_before_break)


        if self.func(x_before_break[0], x_before_break[1]) < \
                self.func(x_before_before_break[0], x_before_before_break[1]):
            return [[round(x_before_before_break[0], self.ACCURACY), round(x_break[0], self.ACCURACY)],
                    [round(x_before_before_break[1], self.ACCURACY), round(x_break[1], self.ACCURACY)]]
        else:
            return [[round(self.starting_point[0] + self.delta[0] * (count_delta - combo * (3 / 2)), self.ACCURACY),
                    round(x_before_break[0], self.ACCURACY)],
                    [round(self.starting_point[1] + self.delta[1] * (count_delta - combo * (3 / 2)), self.ACCURACY),
                    round(x_before_break[1], self.ACCURACY)]]

    def walker_left(self):

        combo = 2
        count_delta = 3

        while self.func(self.starting_point[0] - (self.delta[0] * (count_delta - combo)),
                        self.starting_point[1] - (self.delta[1] * (count_delta - combo))) > \
                self.func(self.starting_point[0] - (self.delta[0] * count_delta),
                          self.starting_point[1] - (self.delta[1] * count_delta)):
            combo *= 2
            count_delta += combo
        x_break = [self.starting_point[0] - self.delta[0] * count_delta,
                   self.starting_point[1] - self.delta[1] * count_delta]
        x_before_break = [self.starting_point[0] - self.delta[0] * (count_delta - combo / 2),
                          self.starting_point[1] - self.delta[1] * (count_delta - combo / 2)]
        x_before_before_break = [self.starting_point[0] - self.delta[0] * (count_delta - combo),
                                 self.starting_point[1] - self.delta[1] * (count_delta - combo)]
        print('x_b L:', x_break, x_before_break, x_before_before_break)

        if self.func(x_before_break[0], x_before_break[1]) < \
                self.func(x_before_before_break[0], x_before_before_break[1]):
            return [[round(x_break[0], self.ACCURACY), round(x_before_before_break[0], self.ACCURACY)],
                    [round(x_break[1], self.ACCURACY), round(x_before_before_break[1], self.ACCURACY)]]
        else:
            return [[round(x_before_break[0], self.ACCURACY),
                    round(self.starting_point[0] - self.delta[0] * (count_delta - combo * (3 / 2)), self.ACCURACY)],
                    [round(x_before_break[1], self.ACCURACY),
                    round(self.starting_point[1] - self.delta[1] * (count_delta - combo * (3 / 2)), self.ACCURACY)]]

    # Example f = (100 - x)^2 = x*x - 200x + 10 000
    def finder(self):
        if self.func(self.starting_point[0] - self.delta[0], self.starting_point[1] - self.delta[1]) > \
                self.func(self.starting_point[0] + self.delta[0], self.starting_point[1] + self.delta[1]):
            return self.walker_right()
        elif self.func(self.starting_point[0] - self.delta[0], self.starting_point[1] - self.delta[1]) < \
                self.func(self.starting_point[0] + self.delta[0], self.starting_point[1] + self.delta[1]):
            return self.walker_left()
        else:
            return [self.starting_point[0], self.starting_point[1]]

if __name__ == '__main__':

    Sven_methon = Find_Interval()
    interval = Sven_methon.finder()
    print('Interval =', interval)
    print('Function =', Find_Interval().func(interval[0][0], interval[0][1]), '-', Find_Interval().func(interval[1][0], interval[1][1]))
    # print('Function =', Find_Interval().func(interval[1][0], interval[1][1]))
    input()
