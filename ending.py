def end_num(num):
    pre_end = "осталось"
    end = "дней"
    if num % 10 == 1:
        pre_end = "остался"
        end = "день" 
    elif num % 10 in range(2,5):
        end = "дня"
    return "До премии " + pre_end + " " + str(num) + " " + end + "! Готовься к собеседованиям!"