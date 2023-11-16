from util_data_generator import *
import random
from ema_workbench.analysis import prim
import sys

def error_example():
    number_of_data_points = [1600, 3200, 6400]  # number of points to experiment with
    number_of_dimensions = [10, 15]
    k = 1

    for n in range(len(number_of_data_points)):
        for m in range(len(number_of_dimensions)):
            for i in range(3):
                sys.stdout.write('\r' + 'experiment' + ' ' + str(k) + '/' + str(len(number_of_data_points) * len(number_of_dimensions)*3))
                x, y = generate_data(calculate_y_oakley_ohagan2004, 15, number_of_data_points[n])

                selected_columns = random.sample(list(x.columns), number_of_dimensions[m])
                x = x[selected_columns]

                prim_alg = prim.Prim(x, y, peel_alpha=0.1, threshold=0.7)
                boxes = prim_alg.find_box()
                k = k + 1

if __name__ == "__main__":
    error_example()