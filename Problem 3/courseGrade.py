def courseGrade():
    
    # TODO: Declare any necessary variables here. 

    import csv

    file = input()
    students = [] 
    
    with open(f"{file}") as f:
        reader = csv.DictReader(f)
        for i in reader:
            students.append({"last_name": i[0], "first_name": i[1], "midterm1": i[2], "midterm2": i[3], "final": i[4]})




'''
with open(file, 'r') as file1:
        contents = list(csv.reader(file1, delimeter='\t'))
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
    
    with open('report.txt', 'w') as file2:
        for i in range(len(score1)):
            avg_score = (score1[i] + score2[i] + total_score[i]) // 3
            midterm1_avg1 = sum(score1) / len(score1)
            midterm_avg2 = sum(score2) / len(score2)
            final_avg = sum(total_score) / len(total_score)

            letter_grade = ""

            if avg_score >= 90:
                letter_grade = "A"
            elif avg_score >= 80:
                letter_grade = "B"
            elif avg_score >= 70:
                letter_grade = "C"
            elif avg_score >= 60:
                letter_grade = "D"
            else:
                letter_grade = "F"

            print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(last_name[i],
            first_name[i],
            midterm1_avg1[i],
            midterm_avg2[i],
            total_score[i],
            letter_grade), f = file2)
        
        print("\nAverages: midterm {:.2f}, midterm2 {:.2f}, final {:.2f}.format(midterm_avg1, midterm_avg2, final_avg), f = f3")


    return
'''
    

# TODO: Read a file name from the user and read the tsv file here. 
    
           
            
    
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    

if __name__ == "__main__":
    courseGrade()
    
    