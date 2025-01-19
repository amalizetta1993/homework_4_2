import utils
import re

users_list = [] #для пользователей с их данными
user_data_list = ['','','',''] #для данных одного пользователя
reg_pattern = utils.get_reg_data()

#заполнение данных пользователей
while len(users_list) != 3: #первый цикл, пока пользователей меньше трех
    i=0
    while i!=4:   #второй цикл, пока данных меньше четырех          
        if i == 0:
            while i != 1:
                user_data = input('Введите имя пользователя: ')               
                user_data_list[i] = utils.reg_check(user_data, reg_pattern[0], users_list) 
                if user_data_list[i] != None:
                    i+=1
                    print('Имя принято')
                else:
                    i=0
                    print('Содержит неподходящие символы')
        elif i == 1:
            while i != 2:
                user_data = input('Введите фамилию пользователя: ')
                user_data_list[i] = utils.reg_check(user_data, reg_pattern[0], users_list)
                if user_data_list[i] != None:
                    print('Фамилия принята')
                    i+=1
                else:
                    print('Содержит неподходящие символы')
                    i=1
        elif i == 2:
            while i != 3:
                user_data = input('Введите телефон в формате ****(**)*******: ')
                user_data_list[i] = utils.reg_check(user_data, reg_pattern[1], users_list)
                if user_data_list[i] != None:
                    print('Телефон принят')
                    i+=1
                else:
                    print('Телефон не соответствует формату ****(**)*******')
                    i=2
        elif i == 3:
            while i != 4:
                user_data = input('Введите email на Яндексе: ')            
                user_data_list[i] = utils.reg_check(user_data, reg_pattern[2], users_list)
                if user_data_list[i] != None:
                    print('Почта принята')
                    i+=1
                else:
                    print('Почта должна содержать @yandex.ru')
                    i=3
                    
    copy = user_data_list.copy()    
    users_list.append(copy)
    
#Вывод пользователей
print(*users_list, sep = "\n")