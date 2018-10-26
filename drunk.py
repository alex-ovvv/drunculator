p = 2.5
one_man = p*1.5
low_alco = 0.3
med_alco = 1.6
hard_alco = 2.5
u_hard_alco = 4

def alco_per_m_h(type_alco):
    return int(p/type_alco)

def alco_per_m_n(type_alco):
    return int(one_man/type_alco)

print("Привет, я drunculator. Первый в мире бот, который считает количество алкоголя, которое необходимо на тусовку")

q_man = input("Расскажи-ка мне, сколько людей ты уже пригласил: ")
q_man = int(q_man)

def sost():
    x = input("Скажи мне, до какого состояния ты хочешь напиться? 1 - просто посидеть, 2 - неплохо накидаться, 3 - говно!!!: ")
    x = int(x)
    if x == 1:
        return one_man == float(one_man)*0.25
    elif x == 2:
        return one_man == float(one_man)*0.6
    elif x == 3:
        return one_man == float(one_man)
    else:
        print("Ты что-то ввел неправильно. Давай еще раз")
        sost()
    return one_man
sost()

print("Теперь я буду спрашивать у тебя в какой пропорции ты хочешь закупить алкоголь. На каждую позицию ты должен назвать цифру от 1 до 10. Где 1 - 100%, значит, что ничего другого ты покупать не будешь")

def q_1():
    input_1 = int(input("Скажи мне, сколько пива ты хочешь взять: "))
    input_2 = int(input("Скажи мне, сколько вина ты хочешь купить: "))
    input_3 = int(input("Скажи мне, сколько крепкого алкоголя (40%) ты хочешь взять: "))
    input_4 = int(input("Скажи мне, сколько абсента ты хочешь взять: "))
    if (input_1 + input_2 + input_3 + input_4) != 10:
       print("Ты написал что-то неправильное. Давай заново")
       q_1()
    else:
        sum_man = input("Введите суммарный вес вашей компании: ")
        sum_man = int(sum_man)
        sum_man = sum_man / q_man

        x = (input_1 * low_alco + input_2 * med_alco + input_3 * hard_alco + input_4 * u_hard_alco) * sum_man
        x1 = (one_man) * q_man / x
        #list_of_alco = []
        q_low = float(x1 * input_1)
        q_med = float(x1 * input_2)
        q_hard = float(x1 * input_3)
        q_u_hard = float(x1 * input_4)
        #list_of_alco.extend(q_low, q_med, q_hard, q_u_hard)
        return (q_low, q_med, q_hard, q_u_hard)

q_1()

#while (True):
    #input_1 = int(input("Скажи мне, сколько пива ты хочешь взять: "))
    #input_2 = int(input("Скажи мне, сколько вина ты хочешь купить: "))
    #input_3 = int(input("Скажи мне, сколько крепкого алкоголя (40%) ты хочешь взять: "))
    #input_4 = int(input("Скажи мне, сколько абсента ты хочешь взять: "))

    #if (input_1 + input_2 + input_3 + input_4) != 10:
     #   print("Ты написал что-то неправильное. Давай заново")
      #  continue

    #else:
     #   print('life is good')
      #  break

#print('ti krasavchik')


sum_man = input("Введите суммарный вес вашей компании: ")
sum_man = int(sum_man)
sum_man = sum_man / q_man

def quantity_of_alco_type(sum_man):
    x = (input_1/10*low_alco + input_2/10*med_alco + input_3/10*hard_alco + input_4/10*u_hard_alco) * q_man
    x1 = (one_man) * q_man / x
    q_low = float(x1*input_1)
    q_med = float(x1*input_2)
    q_hard = float(x1*input_3)
    q_u_hard = float(x1*input_4)
    return (q_low, q_med, q_hard, q_u_hard)

#print (quantity_of_alco_type(sum_man))




