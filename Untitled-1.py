print("Hi, i am an ai bot from Udupi hotel.How was your food_quality?")
food_quality = input("excellent/bad = ").lower()
if food_quality == "excellent":
   print("Thank you,i am glad you liked the food and please visit us again")
elif food_quality=="bad":
     reason = input("reason(lack in flavour/poor service by servers/high prices):").lower()
     if reason=="lack in flavour":
        print("we are sorry we will speak with our chef.Please do visit us again,thank you!")
     elif reason=="poor service": 
        print("we are sorry we will improve our servers service.Please do visit us again,thank you!")
     elif reason=="high prices":
        print("we will reduce the prices how much ever possible.Please do visit us again,thank you!")
    
        