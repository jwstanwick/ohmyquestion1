import random

BLOOD_TYPE_PROB ={
    'O': 0.45,
    'A': 0.40,
    'B': 0.11,
    'AB': 0.04
}

def check_if_compatible(donor, receiver):
    if (donor == 'O'):
        return True
    elif (donor == 'A'):
        return(receiver == 'A' or receiver == 'AB')
    elif (donor == 'B'):
        return(receiver == 'B' or receiver == 'AB')
    else:
        return(receiver == 'AB')

def get_random_blood_type():
    rand_num = random.randint(1, 100)
    if (rand_num <= BLOOD_TYPE_PROB['O']*100):
        return 'O'
    elif (rand_num <= BLOOD_TYPE_PROB['O']*100 + BLOOD_TYPE_PROB['A']*100):
        return 'A'
    elif (rand_num <= BLOOD_TYPE_PROB['O']*100 + BLOOD_TYPE_PROB['A']*100 + BLOOD_TYPE_PROB['B']*100):
        return 'B'
    else:
        return 'AB'

def run_simulation(NUM_PEOPLE, RECEIVER):
    for i in range(NUM_PEOPLE):
        DONOR = get_random_blood_type()
        if (check_if_compatible(DONOR, RECEIVER)):
            return True
        iterations += 1
    return False
                  
def main():
    NUM_SIMULATIONS = 10000
    NUM_PEOPLE = 3
    DESIRED_BLOODTYPE = 'AB'
    
    num_successes = 0
    for i in range(NUM_SIMULATIONS):
        if(run_simulation(NUM_PEOPLE, DESIRED_BLOODTYPE)):
            num_successes += 1
    print("Probability of finding a compatible donor: ", num_successes/NUM_SIMULATIONS)

if __name__ == "__main__":
    main()