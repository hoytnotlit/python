

def group_count(input_list):
    """
    make this into a one line dict comprehension
    """

    group_count = { item: input_list.count(item) for item in sorted(set(input_list)) }
    # group_count = {}
    # for item in input_list:

    #     if item not in group_count:
    #         group_count[item] = 0
        
    #     group_count[item] += 1

    return group_count

input_list = ["1", "2", "2", "3","3"]
print(group_count(input_list))