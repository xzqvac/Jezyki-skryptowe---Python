def write_list(list):
    print(' '.join([str(item) for item in list]).center(30))

x = input("Podaj liczbe poziomow: ")
line = [1]
write_list(line)
for i in range(int(x) - 1):
    next_line = [1]
    for j in range(len(line) - 1):
        next_line.append(line[j] + line[j + 1])
    next_line.append(1)
    line = next_line
    write_list(line)
