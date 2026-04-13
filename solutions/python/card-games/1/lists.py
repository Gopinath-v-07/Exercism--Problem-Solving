"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return[number,number+1,number+2]
            
def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1+rounds_2


def list_contains_round(rounds, number):
    

   for i in rounds:
       if i == number:
           return True
   return False


def card_average(hand):
    

  return sum(hand) / len(hand)


def approx_average_is_average(hand):
    true_average = sum(hand) / len(hand)
    
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]
    
    return first_last_avg == true_average or middle_card == true_average


def average_even_is_average_odd(hand):
   if len(hand) == 0:
        return False
   even_sum = 0
   odd_sum = 0
   even_count = 0
   odd_count = 0
   for i in range(len(hand)):
        if i % 2 == 0:
            even_sum += hand[i]
            even_count += 1
        else:
            odd_sum += hand[i]
            odd_count += 1
   even_avg = even_sum / even_count if even_count != 0 else 0
   odd_avg = odd_sum / odd_count if odd_count != 0 else 0
   return even_avg == odd_avg
   


def maybe_double_last(hand):
    for i in range(len(hand)):
        if hand[-1]==11:
            hand[-1]=11*2
    return hand

