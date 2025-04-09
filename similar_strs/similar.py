

def indicesToRemove(str1, str2):
    indices = []
    for i in range(len(str1)):
        if str1[:i] + str1[i+1:] == str2:
            indices.append(i)

    if not indices:
        return [-1]
    return indices
