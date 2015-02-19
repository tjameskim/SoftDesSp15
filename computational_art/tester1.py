def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    # TODO: implement this
    initial_range = float(input_interval_end) - float(input_interval_start)
    end_range = float(output_interval_end) - float(output_interval_start)
    diff = float(val) - float(input_interval_start)

    frac = diff / initial_range
    add = end_range * frac
    return float(output_interval_start) + add

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    