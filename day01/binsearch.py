def bin_search(data, olek):
    if len(data) == 0:
        return False
    return do_bin_search(data, olek, 0, len(data) - 1)

def do_bin_search(data, olek, start, end):
    
    if start >= end:
        return False

    index = int((start+end)/2)
    value = data[index]

    if value == olek:
        return True

    if value < olek:
        return do_bin_search(data, olek, (index + 1), end)
    else:
        return do_bin_search(data, olek, start, index - 1)

