#!/usr/bin/env python3

"""Функции для добавления инфо о пользователях и проверка этой инфы"""

import re

#Паттерны проверки введенных данных
def get_reg_data():
    name_pattern = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
    mobile_pattern = re.compile(r'^\+\d{1,3}\(\d{2}\)\d{7}$')
    email_pattern = re.compile(r'^[a-zA-Z0-9]+@yandex.ru$')
 

#Функция для проверки введенных данных    
def reg_check(user_data, reg_pattern, users_list, data_to_check=None): 
    
    #функция для проверки уникальности введенных данных (номер телефона и email)
    def check_unique_data(user_data, data_to_check):
    








#заполнение данных пользователей
while len(users_list) != 3:
    i=0
    while i!=4:              
        if i == 0:
            while i != 1:
                data = input('Введите имя пользователя: ')
                match = re.match(name_pattern, data)
                if match:
                    print('Имя принято')
                    user_data_list[i] = data 
                    i+=1
                else:
                    print('Содержит неподходящие символы')
                    i=0
        elif i == 1:
            while i != 2:
                data = input('Введите фамилию пользователя: ')
                match = re.match(name_pattern, data)
                if match:
                    print('Фамилия принята')
                    user_data_list[i] = data 
                    i+=1
                else:
                    print('Содержит неподходящие символы')
                    i=1
        elif i == 2:
            while i != 3:
                data = input('Введите телефон в формате ****(**)*******: ')
                match = re.match(mobile_pattern, data)
                if match:
                    print('Телефон принят')
                    user_data_list[i] = data
                    i+=1
                else:
                    print('Телефон не соответствует формату ****(**)*******')
                    i=2
        elif i == 3:
            while i != 4:
                data = input('Введите email на Яндексе: ')            
                match = re.match(email_pattern, data)
                if match:
                    print('Почта принята')
                    user_data_list[i] = data
                    i+=1
                else:
                    print('Почта должна содержать @yandex.ru')
                    i=3
                    
#Проверка на дубликат           
    copy = user_data_list.copy()

    if len(users_list)==0:
        users_list.append(copy)
    else:
        j=0
        count=0
        for j in range(len(users_list)):
            if users_list[j]==copy:
                count+=1
        if count==0:
            users_list.append(copy)                                
        else:
            print('Такой пользователь уже существует! Введите данные заново')
            


