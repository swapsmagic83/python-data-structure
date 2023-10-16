def same_frequency(nums1, nums2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    nums1 = str(nums1)
    nums2 = str(nums2)
    num1_dict={}
    num2_dict = {}
    for num1 in nums1:
        num1_dict[num1] = nums1.count(num1)
    for num2 in nums2:
        num2_dict[num2] = nums2.count(num2)
    if num1_dict == num2_dict:
        return True
    return False
    
