#Kim Budischewski

def frequency(text_file):
    """Makes a dictionary of what words and how many there are in the file"""
    new_file = open(text_file, "r")
    new_dict = {}
    check_list = []

    for line in new_file.readlines():

        for word in line.split():
            up_word = word.upper()
            low_word = word.lower()
            cap_word = word.lower().capitalize()

            if word in new_dict:
                new_dict[word] += 1
            elif up_word in new_dict:
                new_dict[up_word] += 1
            elif low_word in new_dict:
                new_dict[low_word] += 1
            elif cap_word in new_dict:
                new_dict[cap_word] += 1
            else:
                new_dict[word] = 1

        # for word in line.split():
        #     check = 0
        #     for check_word in check_list:
        #         if check == 0:
        #             if check_word.lower() == word.lower():
        #                 new_dict[check_word] += 1
        #                 check += 1
        #     if check == 0:
        #         new_dict[word] = 1
        #         check_list.append(word)

    new_file.close()
    return new_dict

def most_frequent(word_dict):
    """Makes a dictionary with the 10 most used words from the sent dictionary"""
    new_top_dict = {}
    new_dict = {}

    if len(word_dict) < 10:
        for key in word_dict:
            new_dict[key] = word_dict[key]
        return new_dict


    #Dict for check and len(top_dict) = 10
    for key in word_dict:
        if len(new_dict) < 10:
            new_dict[key] = word_dict[key]

    for key in new_dict:
        new_key = key
        for ele in word_dict:
            if new_key in new_top_dict: #Check if key is in top_dict 
                new_key = ele
            elif ele not in new_top_dict and word_dict[ele] > word_dict[new_key]:
                new_key = ele

        new_top_dict[new_key] = word_dict[new_key]

    return new_top_dict


def word_count(word_dict):
    """Count the words in dictionary"""
    count = 0
    for key in word_dict:
        count += word_dict[key]
    return count
    
def unique_words(word_dict):
    """Sends back how many keys(words) there are in the dictionary"""
    return len(word_dict)

def mean_frequency(word_dict):
    """Returns the averge number of words used in dictionary"""
    mean = word_count(word_dict)/unique_words(word_dict)
    return mean

def median_frequency(word_dict):
    """Returns the median from the word count in dictionary"""
    word_list = list(word_dict.values())

    word_count = 0
    for key in word_dict:#How many words in word_dict
        word_count += 1

    if word_count == 1:
        return word_list[0]
            
    elif word_count%2 == 0:
        index = word_count/2
        num1 = word_list[int(index)-1]
        num2 = word_list[int(index)]
        return (num1+num2)/2

    else:
        index = (word_count-1)/2
        return word_list[int(index)]

def closest_word(word_dict, rate):
    """Returns the word with the word count closest to number"""
    return_key = ""
    check_dict = {}
    for key in word_dict:
        check = abs(rate-word_dict[key])
        check_dict[key] = check
    return_key = min(check_dict, key=check_dict.get)
    
    return return_key

def main():
    #Start of program
    print("Välkommen till 'Frekvensanalys'")
    file = input("Vilken fil vill du undersöka: ")

    dictionary = frequency(file)
    if not dictionary:
        print("Filen är tom")

    else:
        print()
        print("Filen innehåller")
        print("Antal ord: ", word_count(dictionary))
        print("Antal unika ord: ", unique_words(dictionary),"\n")
        print("Här är de 10 vanligaste orden i filen i fallande ordning.\n")

        top_dict = most_frequent(dictionary)

        print("Ord          Antal förekomster")
        print("------------------------------")
        for k in top_dict:
            print(f"{k:10} {top_dict[k]:10}")
        print()

        print("Av orden i top-listan är")
        print("Frekvens-medelvärdet = ", mean_frequency(top_dict))
        print("Frekvens-medianen = ", median_frequency(top_dict),"\n")

        print(f"Ordet '{closest_word(top_dict, mean_frequency(top_dict))}' har frekvensen som ligger närmast medelvärdet.")
        print()

if __name__ == "__main__":
    main()