def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    file = input().strip()
    students = [] 
    last_name = []
    first_name = []
    score1 = []
    score2 = []
    total_score = []

    # TODO: Read a file name from the user and read the tsv file here. 
    with open(file, 'r') as file1:
        contents = list(csv.reader(file1, delimeter=''))
        for i in contents:
            last_name = "".join(i[0])
            first_name = "".join(i[1])
            score1 = "".join(i[2])
            score2 = "".join(i[3])
            total_score = "".join(i[4])
            
            students.append(i)
            last_name.append(last_name)
            first_name.append(first_name)
            score1.append(int(score1))
            score2.append(int(score2))
            total_score.append(int(total_score))
            

    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    
    
    return

if __name__ == "__main__":
    courseGrade()
    
    