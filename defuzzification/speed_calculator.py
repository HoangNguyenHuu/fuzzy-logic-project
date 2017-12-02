from scipy.integrate import quad


def write_function(arguments):
    coefficient = arguments[0]
    label = arguments[1]
    min_arg = arguments[2]
    if label == "Fast":
        if min_arg == 1:
            def result_dependency(x):
                if x <= 1:
                    return 0
                if 1 < x <= 1.5:
                    return (x - 1) / 0.5
                return min_arg

            def result_up_dependency(x):
                if x <= 1:
                    return 0
                if 1 < x <= 1.5:
                    return x * (x - 1) / 0.5
                return min_arg * x

            return result_dependency, result_up_dependency, min_arg

        else:
            def result_dependency(x):
                if x <= 1:
                    return 0
                if 1 < x <= coefficient[0]:
                    return (x - 1) / 0.5
                return min_arg

            def result_up_dependency(x):
                if x <= 1:
                    return 0
                if 1 < x <= coefficient[0]:
                    return x * (x - 1) / 0.5
                return min_arg * x

            return result_dependency, result_up_dependency, min_arg

    if label == "Slower":
        if len(coefficient) == 1:
            def result_dependency(x):
                if 0.5 < x <= 1:
                    return (x - 0.5) / 0.5
                if 1 < x <= 1.5:
                    return (1.5 - x) / 0.5
                return 0

            def result_up_dependency(x):
                if 0.5 < x <= 1:
                    return x * (x - 0.5) / 0.5
                if 1 < x <= 1.5:
                    return x * (1.5 - x) / 0.5
                return 0

            return result_dependency, result_up_dependency, min_arg

        if len(coefficient) == 2:
            def result_dependency(x):
                if 0.5 < x <= coefficient[0]:
                    return (x - 0.5) / 0.5
                if coefficient[0] < x <= coefficient[1]:
                    return min_arg
                if coefficient[1] < x <= 1.5:
                    return (1.5 - x) / 0.5
                return 0

            def result_up_dependency(x):
                if 0.5 < x <= coefficient[0]:
                    return x * (x - 0.5) / 0.5
                if coefficient[0] < x <= coefficient[1]:
                    return min_arg * x
                if coefficient[1] < x <= 1.5:
                    return x * (1.5 - x) / 0.5
                return 0

            return result_dependency, result_up_dependency, min_arg

    if label == "Slow":
        # if len(coefficient) == 1:
        #     def result_dependency(x):
        #         if 0 < x <= 0.5:
        #             return x / 0.5
        #         if 0.5 < x <= 1:
        #             return (1 - x) / 0.5
        #         return 0
        #
        #     def result_up_dependency(x):
        #         if 0 < x <= 0.5:
        #             return x * x / 0.5
        #         if 0.5 < x <= 1:
        #             return (1 - x) * x / 0.5
        #         return 0
        #
        #     return result_dependency, result_up_dependency, min_arg
        #
        # if len(coefficient) == 2:
        def result_dependency(x):
            if 0.5 < x <= coefficient[0]:
                return min_arg
            # if coefficient[0] < x <= coefficient[1]:
            #     return min_arg
            if coefficient[0] < x <= 1:
                return (1 - x) / 0.5
            return 0

        def result_up_dependency(x):
            if 0.5 < x <= coefficient[0]:
                return x * x / 0.5
            # if coefficient[0] < x <= coefficient[1]:
            #     return min_arg * x
            if coefficient[0] < x <= 1:
                return (1 - x) * x / 0.5
            return 0

        return result_dependency, result_up_dependency, min_arg

    if label == "Stop":
        if min_arg == 1:
            def result_dependency(x):
                if 0 <= x <= 0.01:
                    return (0.01 - x) / 0.01
                return 0

            def result_up_dependency(x):
                if 0 <= x <= 0.01:
                    return x * (0.01 - x) / 0.01
                return 0

            return result_dependency, result_up_dependency, min_arg
        else:
            def result_dependency(x):
                if 0 <= x < coefficient[0]:
                    return min_arg
                if coefficient[0] <= x < 0.01:
                    return (0.01 - x) / 0.01
                return 0

            def result_up_dependency(x):
                if 0 <= x < coefficient[0]:
                    return min_arg * x
                if coefficient[0] <= x < 0.01:
                    return x * (0.01 - x) / 0.01
                return 0

            return result_dependency, result_up_dependency, min_arg


def calculate_speed(arguments):
    fx, xfx, weight = write_function(arguments)
    numerator, err1 = quad(xfx, 0, 2)
    denominator, err2 = quad(fx, 0, 2)
    speed = numerator / denominator
    return speed, weight
