#first to take default list
list1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]

def count_frequencies(dic):
    frequencyofdic = {}
    for i in dic:
        if i in frequencyofdic:
            frequencyofdic[i] += 1
        else:
            frequencyofdic[i] = 1
    return frequencyofdic

frequencies = count_frequencies(list1)

# Print the frequencies
for key, value in frequencies.items():
    print(f"{key} : {value}")




