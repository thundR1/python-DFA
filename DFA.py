# Name : Youssef Elsayed Abd-Elkader Nasr Amin
# ID : 201900314
n = int(input("Enter The Number of States : "))
states = [input("Enter The States : ") for i in range (0, n)]
num_of_input_symbols = int(input("Enter The Number of Input symbols : "))
input_symbols = [input("Enter The Input Symbol : ") for j in range(0, num_of_input_symbols)]
num_of_final_states = int(input("Enter The Number of Final States : "))
final_states = [input("Enter Final State : ") for k in range(0, num_of_final_states)]

DFA = [0 for i in range(len(states))]
for i in range(len(states)):
    DFA[i] = [0 for j in range(len(input_symbols))]
    for j in range(len(input_symbols)):
        DFA[i][j] = input('From ' + states[i] + ' if ' + input_symbols[j] + ' goto : ')

def permute(arg1, arg2):
    my_list.append(DFA[states.index(arg1)][input_symbols.index(arg2)])
    return DFA[states.index(arg1)][input_symbols.index(arg2)]

while True:
    my_list = []
    start_state = states[0]
    my_string = input("\nEnter Your String : ")
    for i in my_string:
        start = permute(start_state, i)
    if(my_list[-1] in final_states):
        print("\nAccepted")
        print(my_list)
    else:
        print("\nRejected")
        print(my_list)