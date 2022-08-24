ipl_score = [34,45,67,34]

def get_max(data):
    max = data[0]
    for idx in range(1, len(data)):
        if data[idx] > max:
            max = data[idx]

    print("max is ", max)
    return max

get_max(ipl_score)

















