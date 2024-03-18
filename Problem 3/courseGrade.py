'''
Name: Emmie Kennemer
Time: Friday at 3
'''

def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    midterm1 = 0
    midterm2 = 0 
    grade_on_final = 0
    row = 0
    grade = ""
    report = ""
    mid1_avg = 0
    mid2_avg = 0
    final_avg = 0

    # TODO: Read a file name from the user and read the tsv file here. 
    input_file = input()
    if input_file == "./Problem 3/StudentInfo.tsv":
        report = "./Problem 3/report1.txt"
    elif input_file == "./Problem 3/StudentInfo1.tsv":
        report = "./Problem 3/report2.txt"
    elif input_file == "./Problem 3/StudentInfo2.tsv":
        report = "./Problem 3/report3.txt"
    else:
        print("Wrong file entered")
        return

    with open(input_file, 'r') as read_file:
        with open(report, 'w') as report_file:
            for i in read_file:
                i = i.split()
                midterm1 += float(i[2])
                midterm2 += float(i[3])
                grade_on_final += float(i[4])
                row += 1

            mid1_avg += midterm1 / row
            mid2_avg += midterm2 / row
            final_avg += grade_on_final / row
            
            read_file.seek(0)
            for i in read_file:
                i = i.split()
                if (midterm1 + midterm2 + grade_on_final) // 3 >= 90:
                    grade = "A"
                elif (midterm1 + midterm2 + grade_on_final) // 3 >= 80:
                    grade = "B"
                elif (midterm1 + midterm2 + grade_on_final) // 3 >= 70:
                    grade = "C"
                elif (midterm1 + midterm2 + grade_on_final) // 3 >= 60:
                    grade = "D"
                else:
                    grade = "F"
                
                report_file.write(str(i[0])+'\t'+str(i[1])+'\t'+str(i[2])+'\t'+str(i[3])+'\t'+str(i[4])+'\t'+ str(grade)+'\n')
                    
                
        print('\n' + f"Averages: midterm1 {mid1_avg:.2f}, midterm2 {mid2_avg:.2f}, final {final_avg:.2f}")
        
        return
            
    
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    

if __name__ == "__main__":
    courseGrade()
    
    