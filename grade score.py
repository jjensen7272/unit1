def average():
    score1 =  float(input("input 10 score percentages"))
    score2 = float(input(""))
    score3 = float(input(""))
    score4 = float(input(""))
    score5 = float(input(""))
    score6 = float(input(""))
    score7 = float(input(""))
    score8 = float(input(""))
    score9 = float(input(""))
    score10 = float(input(""))
    
    score_sum = (score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10)
    score_avg = score_sum/10
    return score_avg

final_average = average()


print("the average of your scores is ",final_average)

if final_average >= 90:
    print ("your grade is A")
else:
    if final_average >= 80:
        print ("your grade is B")
        else:
            if final_average >= 70:
                print ("your")
