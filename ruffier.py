''' Модуль для расчета результатов пробы Руфье.

Сумма измерений пульса в трех попытках (до нагрузки, сразу после и после короткого отдыха)
в идеале должна быть не более 200 ударов в минуту. 
Мы предлагаем детям измерять свой пульс на протяжении 15 секунд, 
и приводим результат к ударам в минуту умножением на 4:
    S = 4 * (P1 + P2 + P3)
Чем дальше этот результат от идеальных 200 ударов, тем хуже.
Традиционно таблицы даются для величины, делённой на 10. 

Индекс Руфье   
    IR = (S - 200) / 10
оценивается по таблице в соответствии с возрастом:
        7-8             9-10                11-12               13-14               15+ (только для подростков!)
отл.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
хор.    >= 6.5 и < 12   >= 5 и < 10.5       >= 3.5 и < 9        >= 2 и < 7.5        >= 0.5 и < 6
удовл.  >= 12 и < 17    >= 10.5 и < 15.5    >= 9 и < 14         >= 7.5 и < 12.5     >= 6 и < 11
слабый  >= 17 и < 21    >= 15.5 и < 19.5    >= 14 и < 18        >= 12.5 и < 16.5    >= 11 и < 15
неуд.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

для всех возрастов результат "неуд" отстоит от "слабого" на 4, 
тот от "удовлетворительного" на 5, а "хороший" от "уд" - на 5.5

поэтому напишем функцию ruffier_result(r_index, level), которая будет получать
рассчитанный индекс Руфье и уровень "неуд" для возраста тестируемого, и отдавать результат

'''
# здесь задаются строки, с помощью которых изложен результат:
txt_index = "Ваш индекс Руфье: "
txt_workheart = "Работоспособность сердца: "
txt_nodata = '''
нет данных для такого возраста'''
txt_res = [] 
txt_res.append('''низкая. 
Срочно обратитесь к врачу!''')
txt_res.append('''удовлетворительная. 
Обратитесь к врачу!''')
txt_res.append('''средняя. 
Возможно, стоит дополнительно обследоваться у врача.''')
txt_res.append('''
выше среднего''')
txt_res.append('''
высокая''')

def ruffier_index(P1, P2, P3):
    ''' возвращает значение индекса по трем показателям пульса для сверки с таблицей'''
    return (4*(P1+P2+P3)-200)/10

def neud_level(age):
    ''' варианты с возрастом меньше 7 и взрослым надо обрабатывать отдельно, 
    здесь подбираем уровень "неуд" только внутри таблицы:
    в возрасте 7 лет "неуд" - это индекс 21, дальше каждые 2 года он понижается на 1.5 до значения 15 в 15-16 лет '''
    norm_age = (min(age, 15)-7)//2
    result = 21 - norm_age*1.5
    return result
    
def ruffier_result(r_index, level):
    ''' функция получает индекс Руфье и интерпретирует его, 
    возвращает уровень готовности: число от 0 до 4
    (чем выше уровень готовности, тем лучше).  '''
    if r_index >= level:
        return 0
    level -= 4
    if r_index >= level:
        return 1
    level -= 5
    if r_index >= level:
        return 2
    level -= 5.5
    if r_index >= level:
        return 3
    return 4
def test(t1, t2, t3, age):
    ''' эту функцию можно использовать снаружи модуля для подсчетов индекса Руфье.
    Возвращает готовые тексты, которые остается нарисовать в нужном месте
    Использует для текстов константы, заданные в начале этого модуля. '''
        # self.index = (4 * (t1 + t2 + t3)-200)/10
    if age < 7:
        return txt_index + '0'+ txt_nodata
    else:
        ruff_index = ruffier_index(t1, t2, t3)
        result = txt_res[ruffier_result(ruff_index, neud_level(age))]
        res = txt_index + str(ruff_index)+'\n'+txt_workheart+result
        return res
        # index = (4 * (int(t1) + int(t2) + int(t3)) - 200) / 10
        # if age == 7 or age == 8:
        #     if self.index >= 21:
        #         return txt_res1
        #     elif self.index < 21 and self.index >= 17:
        #         return txt_res2
        #     elif self.index < 17 and self.index >=12:
        #         return txt_res3
        #     elif self.index < 12 and self.index >= 6.5:
        #         return txt_res4
        #     else:
        #         return txt_res5
        # if age == 9 or age == 10:
        #     if self.index >= 19.5:
        #         return txt_res1
        #     elif self.index < 19.5 and self.index >= 15.5:
        #         return txt_res2
        #     elif self.index < 15.5 and self.index >= 10.5:
        #         return txt_res3
        #     elif self.index < 10.5 and self.index >= 5:
        #         return txt_res4
        #     else:
        #         return txt_res5
        # if age == 11 or age == 12:
        #     if self.index >= 18:
        #         return txt_res1
        #     elif self.index < 18 and self.index >= 14:
        #         return txt_res2
        #     elif self.index < 14 and self.index >= 9:
        #         return txt_res3
        #     elif self.index < 9 and self.index >= 3.5:
        #         return txt_res4
        #     else:
        #         return txt_res5
        # if age == 13 or age == 14:
        #     if self.index >= 16.5:
        #         return txt_res1
        #     elif self.index < 16.5 and self.index >= 12.5:
        #         return txt_res2
        #     elif self.index < 12.5 and self.index >= 7.5:
        #         return txt_res3
        #     elif self.index < 7.5 and self.index >= 2:
        #         return txt_res4
        #     else:
        #         return txt_res5
        # if age >= 15:
        #     if self.index >= 15:
        #         return txt_res1
        #     elif self.index < 15 and self.index >= 11:
        #         return txt_res2
        #     elif self.index < 11 and self.index >= 6:
        #         return txt_res3
        #     elif self.index < 6 and self.index >= 0.5:
        #         return txt_res4
        #     else:
        #         return txt_res5

