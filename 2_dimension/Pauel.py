from Sven_method import Find_Interval
import math


class Pauel(Find_Interval):
    def __init__(self, starting_point_p=None, delta_p=None, epsilon_p=None):
        super().__init__(starting_point_p, delta_p)
        self.epsilon_p = epsilon_p

    def get_epsilon_p(self):
        self.epsilon_p = float(input('Enter Epsilon: '))

    def end_criterion(self, x2, f2, x_correction, f_correction):
        return math.sqrt((x2[0] - x_correction[0]) ** 2 + (x2[1] - x_correction[1]) ** 2) <= self.epsilon_p and\
               (math.fabs(f2 - f_correction) <= self.epsilon_p)

    def x_correction(self, interval, Swen_metod):
        x2 = [(interval[0][0] + interval[1][0]) / 2, (interval[0][1] + interval[1][1]) / 2]
        f1 = Swen_metod.func(*interval[0])
        f3 = Swen_metod.func(*interval[1])
        f2 = Swen_metod.func(*x2)
        delta_x = math.sqrt((interval[1][0] - x2[0]) ** 2 + (interval[1][1] - x2[1]) ** 2)
        print('1_x* ', [x2[0] + (delta_x * (f1 - f3))
                        / (2 * (f1 - 2 * f2 + f3)),
                x2[1] + (delta_x * (f1 - f3)) / (2 * (f1 - 2 * f2 + f3))])

        return [x2[0] + (delta_x * (f1 - f3)) / (2 * (f1 - 2 * f2 + f3)),
                x2[1] + (delta_x * (f1 - f3)) / (2 * (f1 - 2 * f2 + f3))]

    def x_correction_2(self, interval, Swen_metod):
        x1 = interval[0]
        x2 = [(interval[0][0] + interval[1][0]) / 2, (interval[0][1] + interval[1][1]) / 2]
        x3 = interval[1]
        f1 = Swen_metod.func(*interval[0])
        f3 = Swen_metod.func(*interval[1])
        f2 = Swen_metod.func(*x2)
        a1 = (f2 - f1) / (math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2))
        a2 = (((f3 - f1) / math.sqrt((x3[0] - x1[0]) ** 2 + (x3[1] - x1[1]) ** 2)) -
              ((f2 - f1) / math.sqrt((x2[0] - x1[0]) ** 2 + (x2[1] - x1[1]) ** 2))) / \
             math.sqrt((x3[0] - x2[0]) ** 2 + (x3[1] - x2[1]) ** 2)
        print('2_x* ', [(x1[0] + x2[0]) / 2 - a1 / (2 * a2), (x1[1] + x2[1]) / 2 - a1 / (2 * a2)])
        return [(x1[0] + x2[0]) / 2 - a1 / (2 * a2), (x1[1] + x2[1]) / 2 - a1 / (2 * a2)]

    def half_searching(self, interval, Swen_metod, x2, f2):

        x_correction_2 = self.x_correction_2(interval, Swen_metod)
        f_correction_2 = Swen_metod.func(*x_correction_2)
        if self.end_criterion(x2, f2, x_correction_2, f_correction_2):
            print('2 iter:', interval[0], x2, interval[1], x_correction_2)

            return [x2, x_correction_2]
        else:
            if f2 >= f_correction_2:
                half_interval = [interval[1], x2]
                print('111')

            else:
                print('2')
                half_interval = [interval[0], x2]
                print('3')

            return self.half_searching(half_interval, Swen_metod, x_correction_2, f_correction_2)

    def get_answer_by_pauel(self):
        Swen_metod = Find_Interval(self.starting_point, self.delta)
        interval = Swen_metod.finder()

        if self.epsilon_p is None:
            self.get_epsilon_p()

        x2 = [(interval[0][0] + interval[1][0]) / 2, (interval[0][1] + interval[1][1]) / 2]
        f2 = Swen_metod.func(*x2)
        print('1 iter:', interval[0], x2, interval[1])

        x_correction = self.x_correction(interval, Swen_metod)
        f_correction = Swen_metod.func(*x_correction)

        if f2 >= f_correction:
            half_interval = [x2, interval[1]]

        else:
            half_interval = [interval[0], x2]
        return self.half_searching(half_interval, Swen_metod, x_correction, f_correction)


if __name__ == '__main__':
    pauel = Pauel()
    #
    print('Sven method interval: ', pauel.finder())
    print('\nPauel method answer: ', pauel.get_answer_by_pauel())
    # input()
    #pauel_2 = Pauel()
    #print('Sven method interval: ', pauel_2.finder(), '\nGolden cut method answer: ', pauel_2.get_answer_by_pauel())
    #input()

