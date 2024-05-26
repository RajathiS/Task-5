list = [[9, 3, 6], ["guvi", 5, "ntwrk"], [6, "guvi", 8]]
print("The original list : " + str(list))
string_instances = [elem for sublist in list for elem in sublist if isinstance(elem, str)]
print("The string : " + str(string_instances))
int_instances = [elem for sublist in list for elem in sublist if isinstance(elem, int)]
print("The integer : " + str(int_instances))