import master_mind_GUI as mmg
import random

def random_guess_list():
    guess_list = [0,1,2,3,4,5]
    return_list = []
    for i in range(4):
        i = random.choice(guess_list)
        return_list.append(i)
        guess_list.remove(i)
    return return_list

def right_wrong(list_guess, list_random):
    place_right = 0
    place_wrong = 0
    list_random_index = 0

    for i in list_random:
        list_guess_index = 0

        for k in list_guess:
            if i == k and list_guess_index == list_random_index:
                place_right += 1
            elif i == k:
                place_wrong += 1
            list_guess_index += 1

        list_random_index += 1
    return place_right, place_wrong

def program():
    game_window = mmg.create_GUI()
    random_list = random_guess_list()
    row_guess_index = 0

    program = True
    while program:
        if row_guess_index < 7:
            guess_list = mmg.make_guess(row_guess_index, game_window)
            right_place, wrong_place = right_wrong(guess_list, random_list)
            mmg.peg_feedback(row_guess_index, right_place, wrong_place, game_window)
            row_guess_index += 1
        
            if right_place == 4:
                print("Den fyrsiffriga koden är:",random_list)
                mmg.gameover_screen(row_guess_index, "Winner")
                program = False

        else:
            print("Den fyrsiffriga koden är:",random_list)
            mmg.gameover_screen(row_guess_index, "Loser")
            program = False

if __name__ == "__main__":
    program()