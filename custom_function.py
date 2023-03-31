from csv import *
file_path = '/Users/chiggy/PycharmProjects/test_git/AppleStore.csv'
opened_file = open(file_path)
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    column = []
    for row in apps_data[1:]:
        value = row[index]
        column.append(value)
    return column

# extracting the values for the CSV "prime genre" column as a list.
genres = extract(11)


# creating a frequency table for the list we created in the previous function.
def freq_table(list):
    result = {}
    for element in list:
        if element in result:
            result[element] += 1
        else:
            result[element] = 1
    return result

genres_ft = freq_table(genres)

print(genres_ft)