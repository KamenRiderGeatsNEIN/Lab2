def display_main_menu():
    print ("Enter some numbers separated by commas (e.g. 5, 67, 32)")
   

def get_user_input():
    mystring=input()
    mylist=mystring.split(",")
    newlist=[float(i) for i in mylist]
    return newlist

def calc_average(list):
    sum_of_list = 0
    for i in range(len(list)):
        sum_of_list += list[i]
    average = sum_of_list/len(list)
    print(average)
    if __name__ == "__main__":
        main()

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    newlist=get_user_input()
    calc_average(list=newlist)
if __name__ == "__main__":
    main()