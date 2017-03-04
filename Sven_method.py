
class Find_Interval:
    ACCURACY = 3

    def __init__(self, coeffs=None, starting_point=None, delta=None):
        if coeffs is None:
            coeffs = []
        self.coeffs = coeffs
        self.starting_point = starting_point
        self.delta = delta

    def get_values(self):
        if self.coeffs == [] and self.starting_point is None and self.delta is None:
            highest_power = int(input('Input the highest power of function:'))
            for i in range(highest_power + 1):
                self.coeffs.append(float(input('Input coef near x^{}: '.format(highest_power - i))))
            self.starting_point = float(input('Input your starting point:'))
            self.delta = float(input('Input your step:'))
        else:
            return self.coeffs, self.starting_point, self.delta
        return self.coeffs, self.starting_point, self.delta

    def func(self, x):
        value = 0
        for i in range(len(self.coeffs)):
            powered_x = 1
            for j in range(len(self.coeffs) - i - 1):
                powered_x *= x
            value += self.coeffs[i] * powered_x
        return value

    def walker_right(self):
        if self.func(self.starting_point) > self.func(self.starting_point + self.delta):  # Рухаємось вправо I цикл
            combo = 2
            count_delta = 3

            while self.func(self.starting_point + (self.delta * (count_delta - combo))) > \
                    self.func(self.starting_point + (self.delta * count_delta)):
                combo *= 2
                count_delta += combo

            x_break = self.starting_point + self.delta * count_delta
            x_before_break = self.starting_point + self.delta * (count_delta - combo / 2)
            x_before_before_break = self.starting_point + self.delta * (count_delta - combo)

            if self.func(x_before_break) < self.func(x_before_before_break):
                return round(x_before_before_break, self.ACCURACY), round(x_break, self.ACCURACY)
            else:
                return round(self.starting_point + self.delta * (count_delta - combo * (3 / 2)), self.ACCURACY), \
                       round(x_before_break, self.ACCURACY)

    def walker_left(self):

        if self.func(self.starting_point) > self.func(self.starting_point - self.delta):  # Рухаємось вліво I цикл
            combo = 2
            count_delta = 3

            while self.func(self.starting_point - (self.delta * (count_delta - combo))) > \
                    self.func(self.starting_point - (self.delta * count_delta)):
                combo *= 2
                count_delta += combo
            x_break = self.starting_point - self.delta * count_delta
            x_before_break = self.starting_point - self.delta * (count_delta - combo / 2)
            x_before_before_break = self.starting_point - self.delta * (count_delta - combo)

            if self.func(x_before_break) < self.func(x_before_before_break):
                return round(x_break, self.ACCURACY), round(x_before_before_break, self.ACCURACY)
            else:
                return round(x_before_break, self.ACCURACY), \
                       round(self.starting_point - self.delta * (count_delta - combo * (3 / 2)), self.ACCURACY)

    # Example f = (100 - x)^2 = x*x - 200x + 10 000
    def finder(self):
        self.get_values()
        if self.func(self.starting_point - self.delta) > self.func(self.starting_point + self.delta):

            return self.walker_right()
        elif self.func(self.starting_point - self.delta) < self.func(self.starting_point + self.delta):
            return self.walker_left()
        else:
            return self.starting_point, self.starting_point


if __name__ == '__main__':
    # Sven_Method = Find_Interval([1, -200, 10000], starting_point=10, delta=5)
    # print('Interval =', Sven_Method.finder())  # (65.0, 145.0)

    print('Interval =', Find_Interval().finder())
    input()