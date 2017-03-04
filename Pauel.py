from Sven_method import Find_Interval
import math


class Pauel(Find_Interval):
    def __init__(self, coeffs_p=None, starting_point_p=None, delta_p=None, epsilon_p=None):
        super().__init__(coeffs_p, starting_point_p, delta_p)
        self.epsilon_p = epsilon_p

    def get_epsilon_p(self):
        self.epsilon_p = float(input('Enter Epsilon: '))

    def end_criterion(self, x2, f2, x_correction, f_correction):
        return (math.fabs(x2 - x_correction) <= self.epsilon_p) and (math.fabs(f2 - f_correction) <= self.epsilon_p)

    def x_correction(self, interval, Swen_metod):
        x2 = (interval[0] + interval[1]) / 2
        f1 = Swen_metod.func(interval[0])
        f3 = Swen_metod.func(interval[1])
        f2 = Swen_metod.func(x2)
        delta_x = math.fabs(interval[1] - x2)

        return x2 + (delta_x * (f1 - f3)) / (2 * (f1 - 2 * f2 + f3))

    def x_correction_2(self, interval, Swen_metod):
        x1 = interval[0]
        x2 = (interval[0] + interval[1]) / 2
        x3 = interval[1]
        f1 = Swen_metod.func(interval[0])
        f3 = Swen_metod.func(interval[1])
        f2 = Swen_metod.func(x2)
        a1 = (f2 - f1) / (x2 - x1)
        a2 = (((f3 - f1) / (x3 - x1)) - ((f2 - f1) / (x2 - x1))) / (x3 - x2)
        return (x1 + x2) / 2 - a1 / (2 * a2)

    def half_searching(self, interval, Swen_metod, x2, f2):

        x_correction_2 = self.x_correction_2(interval, Swen_metod)
        f_correction_2 = Swen_metod.func(x_correction_2)
        if self.end_criterion(x2, f2, x_correction_2, f_correction_2):
            return x2, x_correction_2
        else:
            if f2 >= f_correction_2:
                half_interval = (x2, interval[1])
            else:
                half_interval = (interval[0], x2)
            return self.half_searching(half_interval, Swen_metod, x_correction_2, f_correction_2)

    def get_answer_by_pauel(self):
        Swen_metod = Find_Interval(self.coeffs, self.starting_point, self.delta)
        interval = Swen_metod.finder()

        if self.epsilon_p is None:
            self.get_epsilon_p()

        x2 = (interval[0] + interval[1]) / 2
        f2 = Swen_metod.func(x2)

        x_correction = self.x_correction(interval, Swen_metod)
        f_correction = Swen_metod.func(x_correction)

        if f2 >= f_correction:
            half_interval = (x2, interval[1])
        else:
            half_interval = (interval[0], x2)
        return self.half_searching(half_interval, Swen_metod, x_correction, f_correction)


if __name__ == '__main__':
     pauel = Pauel([1, -200, 10000], starting_point_p=30, delta_p=5, epsilon_p=10)
    #
     print('Sven method interval: ', pauel.finder(),
           '\nPauel method answer: ', pauel.get_answer_by_pauel())
     input()
    #pauel_2 = Pauel()
    #print('Sven method interval: ', pauel_2.finder(), '\nGolden cut method answer: ', pauel_2.get_answer_by_pauel())
    #input()

