def wordInRange():
    #Type your code here
    file_input = input()
    word1 = input()
    word2 = input()
   
    with open(file_input, 'r') as file:
        inputs = file.readlines()
        for i in inputs:
            if word1[0:9] <= i[0:9] <= word2[0:9]:
                print(i.strip() + " - in range")
            else:
                print(i.strip() + " - not in range")

    return
if __name__ == '__main__':
    wordInRange()