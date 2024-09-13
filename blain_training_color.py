import random
import time

color_red = "red"
color_green = "green"
color_blue = "blue"
color_yellow = "yellow"
color_map = {1: color_red, 2: color_green, 3: color_blue, 4: color_yellow}

class color_id:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    END = '\033[0m'

class create_color_test1():

    def __init__(self):
        self._color_max_size = len(color_map)

    def get_color_map(self):
        question_id = int(random.random() * self._color_max_size)
        if question_id == 0:
            question_id = self._color_max_size
        question_color = color_map[question_id]
        
        num_red = random.random()
        num_green = random.random()
        num_blue = random.random()
        num_yellow = random.random()
        num_array = [num_red, num_green, num_blue, num_yellow]
        num_array.sort()
        num_sorted_dic = {}
        count = 1
        for num in num_array:
            if num == num_red:
                num_sorted_dic[count] = color_red
            elif num == num_green:
                num_sorted_dic[count] = color_green
            elif num == num_blue:
                num_sorted_dic[count] = color_blue
            elif num == num_yellow:
                num_sorted_dic[count] = color_yellow
            count += 1

        disp_red = random.random()
        disp_green = random.random()
        disp_blue = random.random()
        disp_yellow = random.random()
        disp_array = [disp_red, disp_green, disp_blue, disp_yellow]
        disp_array.sort()
        disp_sorted_dic = {}
        count = 1
        for disp in disp_array:
            if disp == disp_red:
                disp_sorted_dic[count] = color_red
            elif disp == disp_green:
                disp_sorted_dic[count] = color_green
            elif disp == disp_blue:
                disp_sorted_dic[count] = color_blue
            elif disp == disp_yellow:
                disp_sorted_dic[count] = color_yellow
            count += 1

        for key in num_sorted_dic.keys():
            if num_sorted_dic[key] == question_color:
                result_id = key
        
        return num_sorted_dic, disp_sorted_dic, question_id, result_id


def __main__():
    print(end = "please input any key, when start program: ")
    input()
    loop_count = 100
    ok_count = 0
    calc_1 = create_color_test1()
    print("program_count: " + str(loop_count) + ", start")
    start_time = time.time()
    for i in range(loop_count):
        result_color_map, disp_sorted_dic, question_id, result_color_id = calc_1.get_color_map()
        print("color_map: " + str(result_color_map))
        for key in result_color_map.keys():
            if result_color_map[key] == color_red:
                print(end = color_id.RED + str(key) + ": " + disp_sorted_dic[key] + ", " + color_id.END)
            elif result_color_map[key] == color_green:
                print(end = color_id.GREEN + str(key) + ": " + disp_sorted_dic[key] + ", " + color_id.END)
            elif result_color_map[key] == color_blue:
                print(end = color_id.BLUE + str(key) + ": " + disp_sorted_dic[key] + ", " + color_id.END)
            elif result_color_map[key] == color_yellow:
                print(end = color_id.YELLOW + str(key) + ": " + disp_sorted_dic[key] + ", " + color_id.END)
        print("which number is " + color_map[question_id] + " color ?")
        in_result = int(input())
        if (result_color_id == in_result):
            ok_count += 1
        else:
            print("x")
    end_time = time.time()
    print("program_count: " + str(loop_count) + ", ok_count: " + str(ok_count))
    prop_time = end_time - start_time
    print(end = "prop time(s): ")
    print(prop_time)


__main__()
    
