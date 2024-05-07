def micropores(*args,**kwargs):
    result = []
    for arg in args:
        if 'size' in kwargs and arg <= kwargs['size'] or 'size' not in kwargs:
            if 'mult' in kwargs and arg % kwargs['mult']==0 or 'mult' not in kwargs:
                if 'bottom' in kwargs and arg >= kwargs['bottom'] or 'bottom' not in kwargs:
                    result.append(arg)
    return result

