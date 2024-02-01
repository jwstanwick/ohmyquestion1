import random

BLOOD_TYPE_PROB ={
	'O': 0.45,
	'A': 0.40,
	'B': 0.11,
	'AB': 0.04
}

def get_random_blood_type():
	rand_num = random.randint(1, 100)
	if (rand_num <= 45):
		return 'O'
	elif (rand_num <= 85):
		return 'A'
	elif (rand_num <= 96):
		return 'B'
	else:
		return 'AB'


def main():
    
    return

if __name__ == "__main__":
    main()