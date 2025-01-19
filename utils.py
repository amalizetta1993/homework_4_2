#!/usr/bin/env python3

"""Функции для добавления инфо о пользователях и проверка этой инфы"""

import re

#Паттерны проверки введенных данных
def get_reg_data():
    name_pattern = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
    mobile_pattern = re.compile(r'^\+\d{1,3}\(\d{2}\)\d{7}$')
    email_pattern = re.compile(r'^[a-zA-Z0-9]+@yandex.ru$')
    reg_patterns = [name_pattern, mobile_pattern, email_pattern]
    return reg_patterns
 
#Функция для проверки введенных данных    
def reg_check(user_data, reg_pattern, users_list, data_to_check=[]):
    
##################################################################################    
    #функция для проверки уникальности введенных данных (номер телефона и email)   
    def check_unique_data(user_data, data_to_check):                
        j=0
        for j in range(len(data_to_check)):
            if user_data == data_to_check[j]:                               
                print('Такой пользователь уже существует! Введите данные заново')
                return False
        return True
##################################################################################
                
    match = re.match(reg_pattern, user_data)
    unique = True                 
    if users_list == []:
        unique = True
        data_to_check.append(user_data) 
    else:
        if reg_pattern == get_reg_data()[1] or reg_pattern == get_reg_data()[2]: 
            unique = check_unique_data(user_data, data_to_check) 
            data_to_check.append(user_data)   
    if match and unique == True:
        return user_data 
    
