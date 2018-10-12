p = 2.5
one_man = p*1.5
low_alco = 0.3
med_alco = 1.6
hard_alco = 2.5
u_hard_alco = 4
def alco_per_m_h(type_alco):
    return int(p/type_alco)

#print (alco_per_m_h(low_alco))

def alco_per_m_n(type_alco):
    return int(one_man/type_alco)

#print (alco_per_m_n(low_alco))

def quantity_of_alco_type(q_man):
    x = (input_1*low_alco + input_2*med_alco + input_3*hard_alco + input_4*u_hard_alco) * q_man
    x1 = (one_man) * q_man / x
    q_low = float(x1*input_1)
    q_med = float(x1*input_2)
    q_hard = float(x1*input_3)
    q_u_hard = float(x1*input_4)
    return (q_low, q_med, q_hard, q_u_hard)





