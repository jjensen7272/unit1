#Jacob Jensen
#9/17/18

def average():
    score1 =  float(input("input 10 scores"))
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
