def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    falses = [0,None,False,[],'',{},()]
    for falsy in falses:
        for ele in lst:
            if ele == falsy:
                lst.remove(ele)
    return lst            
