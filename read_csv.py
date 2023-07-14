import csv

def read_data_from_csv(file_path):
    x = []
    y = []
    z = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)  # Skip the header row
        next(reader)  # Skip the header row
        for row in reader:
            x.append(row[3])    #
            y.append(row[0])    #Area
            z.append(int(row[7].strip() if row[7].strip()!='' else 0))   #Population

    return x,y,z

x, y, z = read_data_from_csv('film.csv')

filtered_idx = list(filter(lambda i: z[i]=='Scorsese', range(len(z))))

x_filtered = [x[i] for i in filtered_idx]
y_filtered = [y[i] for i in filtered_idx]

print(x)
print(y)
print(z)
print(filtered_idx)
print(x_filtered)
print(y_filtered)
