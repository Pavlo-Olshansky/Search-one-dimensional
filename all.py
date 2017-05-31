from Sven_method import Find_Interval
from Dichotomy import Dichotomy
from Golden_cut import Golden_cut
from Pauel import Pauel

def do_all():
	coeffs = []

	highest_power = int(input('Input the highest power of function:'))

	for i in range(highest_power + 1):
	    coeffs.append(float(input('Input coef near x^{}: '.format(highest_power - i))))
	starting_point = float(input('Input your starting point:'))
	delta = float(input('Input your step:'))
	eplilon_d = float(input('Enter Epsilon for Dichotomy: '))
	eplilon_g = float(input('Enter Epsilon Golden_cut: '))
	eplilon_p = float(input('Enter Epsilon Pauel: '))
	print('Sven method interval :', Find_Interval(coeffs, starting_point, delta).finder())
	print('Dichotomy method     :', Dichotomy(coeffs, starting_point, delta, eplilon_d).search_by_dichotome())
	print('Golden cut method    :', Golden_cut(coeffs, starting_point, delta, eplilon_g).golden_cut())
	print('Pauel method         :', Pauel(coeffs, starting_point, delta, eplilon_p).get_answer_by_pauel())

if __name__ == '__main__':
	do_all()