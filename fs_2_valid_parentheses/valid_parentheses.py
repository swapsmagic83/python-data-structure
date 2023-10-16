def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    count =0
    for paren in parens:
        if paren == '(':
            count = count +1
        elif paren == ')':
            count = count -1
        if count < 0:
            return False
    if count == 0:
        return True
    return False
    
            
