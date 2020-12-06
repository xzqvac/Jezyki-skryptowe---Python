import trojkat


help(trojkat)
#sys.path.append("D:/Studia UWr/Języki skryptowe - python/Lista1/Lista 6/trojkat.py")


a = int(input("Podaj dlugosc pierwszego boku"))
b = int(input("Podaj dlugosc drugiego boku"))
c = int(input("Podaj dlugosc trzciego boku"))
if trojkat.check_condition_of_existing_triangle(a, b, c):
    trojkat.calculate_circuit(a, b, c)
    trojkat.calculate_area(a, b, c)
    trojkat.calculate_type_of_triangle(a, b, c)
    trojkat.calculate_type_of_triangle_based_on_angle(a, b, c)
