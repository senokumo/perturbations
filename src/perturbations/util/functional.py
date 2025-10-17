from functools import reduce

def pipe(*functions):
    def piped(x):
        return reduce(
            lambda result, func: func(result),
            functions,
            x
        )
    
def map_dict(f, dict) -> dict:
    return dict([(k, f(v)) for (k, v) in my_dictionary.iteritems()])
