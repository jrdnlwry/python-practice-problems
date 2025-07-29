def conditional_probability(data, x, y):
    """
    We are given a dataset of observations as a list of tuples, each tuple is of the form (X, Y), 
    where X and Y are categorical variables (i.e., color, animal).

    Implement a function to compute the conditional probability P(Y=y | X=x), 
    the probability that Y equals a specific value y, given that X equals a special value x.
    
    The function should return the probability P(Y=y|X=x).


    We want the conditional probability that Y=y given that X=x.
    """

    y_count = 0
    x_count = 0

    for i in data:
        if i[0] == x and i[1] == y:
            y_count += 1
        if i[0] == x:
            x_count += 1

    try:
        return round(y_count / x_count, 4)
    
    except ZeroDivisionError:
        return 0.0



data = [('male', 'yes'), ('female', 'no'), ('male', 'no'), ('male', 'yes'), ('female', 'yes')]

print(conditional_probability(data, 'male', 'yes'))

