def is_criticality_balanced(temperature, neutrons_emitted):
    product_temp_and_neutrons_emitted=temperature * neutrons_emitted
    if temperature < 800 and neutrons_emitted > 500 and product_temp_and_neutrons_emitted<500000:
        return True
    return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power= voltage  *  current
    efficiency= (generated_power/theoretical_max_power)*100
    if efficiency >= 80:
       return 'green'
    elif  efficiency >=60:
      return 'orange'
    elif  efficiency >= 30 :
        return 'red'
    else:
        return 'black'
def fail_safe(temperature, neutrons_produced_per_second, threshold):
   fail_safe_percentage= temperature * neutrons_produced_per_second
   if fail_safe_percentage < 0.9 * threshold :
        return 'LOW'
   elif  fail_safe_percentage <=1.1 * threshold:
       return 'NORMAL'
   else : 
       return 'DANGER'
    
