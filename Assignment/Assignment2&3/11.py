def unzip_list_of_tuples(list1):
    unzipped_lists = list(zip(list1))
    return unzipped_lists


inp = [(1, 'a'), (2, 'b'), (3, 'c')]
output_lists = unzip_list_of_tuples(inp)
print(output_lists)
