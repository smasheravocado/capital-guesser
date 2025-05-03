#!/usr/bin/env python3

import random
from re import M
import re
import os

# Stackoverflow code
def has_numbers(inputString):
    return bool(re.search(r'^\d+$', inputString))

# Number check from chatgpt
def get_valid_number():
    while True:
        number=input("Contintent list \n\t1. Europe\n\t2. Asia\n\t3. Africa\n\t4. North America\n\t5. Oceania\n\t6. South Amarica\nWhat contenet do you choose [1-6]? ")

        try:
            number = int(number)
            if 1 <= number <= 6:
                return number
            else:
                print("Error: Number must be between 1 and 6.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    return number

# Score functoin to crate/update a file for the score
def score_file(action,score):

    score_filename = '.cg-score'
    
    if action == "read_score":
        try:
            file = open(score_filename, 'r')
            high_score = int(file.read())
        except:
            file = open(score_filename, 'w+')
            file.write("0")
            high_score = 0

        file.close()
        return high_score

    elif action == "set_score":
        file_set = open(score_filename, 'w')
        file_set.write(str(score))
        file_set.close()

os.system('clear')

print("Capital guesser 🗼")
continent=get_valid_number()

high_score = score_file("read_score",0)

''' let the user select the continent '''
if continent == 1:
    capital_list=[["Albania", "Tirana"], ["Andorra", "Andorra la Vella"], ["Armenia", "Yerevan"], ["Austria", "Vienna"], ["Azerbaijan", "Baku"], ["Belarus", "Minsk"], ["Belgium", "Brussels"], ["Bosnia and Herzegovina", "Sarajevo"], ["Bulgaria", "Sofia"], ["Croatia", "Zagreb"], ["Cyprus", "Nicosia"], ["Czech Republic", "Prague"], ["Denmark", "Copenhagen"], ["Estonia", "Tallinn"], ["Finland", "Helsinki"], ["France", "Paris"], ["Georgia", "Tbilisi"], ["Germany", "Berlin"], ["Greece", "Athens"], ["Hungary", "Budapest"], ["Iceland", "Reykjavik"], ["Ireland", "Dublin"], ["Italy", "Rome"], ["Kosovo", "Pristina"], ["Latvia", "Riga"], ["Liechtenstein", "Vaduz"], ["Lithuania", "Vilnius"], ["Luxembourg", "Luxembourg City"], ["Malta", "Valletta"], ["Moldova", "Chisinau"], ["Monaco", "Monaco"], ["Montenegro", "Podgorica"], ["Netherlands", "Amsterdam"], ["North Macedonia", "Skopje"], ["Norway", "Oslo"], ["Poland", "Warsaw"], ["Portugal", "Lisbon"], ["Romania", "Bucharest"], ["Russia", "Moscow"], ["San Marino", "San Marino"], ["Serbia", "Belgrade"], ["Slovakia", "Bratislava"], ["Slovenia", "Ljubljana"], ["Spain", "Madrid"], ["Sweden", "Stockholm"]]
elif continent == 2:
    capital_list=[["Afghanistan", "Kabul"], ["Armenia", "Yerevan"], ["Azerbaijan", "Baku"], ["Bahrain", "Manama"], ["Bangladesh", "Dhaka"], ["Bhutan", "Thimphu"], ["Brunei", "Bandar Seri Begawan"], ["Cambodia", "Phnom Penh"], ["China", "Beijing"], ["Cyprus", "Nicosia"], ["Georgia", "Tbilisi"], ["India", "New Delhi"], ["Indonesia", "Jakarta"], ["Iran", "Tehran"], ["Iraq", "Baghdad"], ["Israel", "Jerusalem"], ["Japan", "Tokyo"], ["Jordan", "Amman"], ["Kazakhstan", "Nur-Sultan"], ["Kuwait", "Kuwait City"], ["Kyrgyzstan", "Bishkek"], ["Laos", "Vientiane"], ["Lebanon", "Beirut"], ["Malaysia", "Kuala Lumpur"], ["Maldives", "Malé"], ["Mongolia", "Ulaanbaatar"], ["Myanmar (Burma)", "Naypyidaw"], ["Nepal", "Kathmandu"], ["North Korea", "Pyongyang"], ["Oman", "Muscat"], ["Pakistan", "Islamabad"], ["Palestine", "Ramallah"], ["Philippines", "Manila"], ["Qatar", "Doha"], ["Russia", "Moscow"], ["Saudi Arabia", "Riyadh"], ["Singapore", "Singapore"], ["South Korea", "Seoul"], ["Sri Lanka", "Colombo"], ["Syria", "Damascus"], ["Tajikistan", "Dushanbe"], ["Thailand", "Bangkok"], ["Timor-Leste", "Dili"], ["Turkey", "Ankara"], ["Turkmenistan", "Ashgabat"], ["United Arab Emirates", "Abu Dhabi"], ["Uzbekistan", "Tashkent"], ["Vietnam", "Hanoi"], ["Yemen", "Sana'a"]]
elif continent == 3:   
    capital_list=[["Algeria", "Algiers"], ["Angola", "Luanda"], ["Benin", "Porto-Novo"], ["Botswana", "Gaborone"], ["Burkina Faso", "Ouagadougou"], ["Burundi", "Bujumbura"], ["Cabo Verde", "Praia"], ["Cameroon", "Yaoundé"], ["Central African Republic", "Bangui"], ["Chad", "N'Djamena"], ["Comoros", "Moroni"], ["Congo (Congo-Brazzaville)", "Brazzaville"], ["Democratic Republic of the Congo (Congo-Kinshasa)", "Kinshasa"], ["Djibouti", "Djibouti"], ["Egypt", "Cairo"], ["Equatorial Guinea", "Malabo"], ["Eritrea", "Asmara"], ["Eswatini (fmr. 'Swaziland')", "Mbabane"], ["Ethiopia", "Addis Ababa"], ["Gabon", "Libreville"], ["Gambia", "Banjul"], ["Ghana", "Accra"], ["Guinea", "Conakry"], ["Guinea-Bissau", "Bissau"], ["Ivory Coast (Côte d'Ivoire)", "Yamoussoukro"], ["Kenya", "Nairobi"], ["Lesotho", "Maseru"], ["Liberia", "Monrovia"], ["Libya", "Tripoli"], ["Madagascar", "Antananarivo"], ["Malawi", "Lilongwe"], ["Mali", "Bamako"], ["Mauritania", "Nouakchott"], ["Mauritius", "Port Louis"], ["Morocco", "Rabat"], ["Mozambique", "Maputo"], ["Namibia", "Windhoek"], ["Niger", "Niamey"], ["Nigeria", "Abuja"], ["Rwanda", "Kigali"], ["São Tomé and Príncipe", "São Tomé"], ["Senegal", "Dakar"], ["Seychelles", "Victoria"], ["Sierra Leone", "Freetown"], ["Somalia", "Mogadishu"], ["South Africa", "Pretoria (administrative), Bloemfontein (judicial), Cape Town (legislative)"], ["South Sudan", "Juba"], ["Sudan", "Khartoum"], ["Togo", "Lomé"], ["Tunisia", "Tunis"], ["Uganda", "Kampala"], ["Zambia", "Lusaka"], ["Zimbabwe", "Harare"]]
elif continent == 4:
    capital_list = [["Antigua and Barbuda", "St. John's"], ["Bahamas", "Nassau"], ["Barbados", "Bridgetown"], ["Belize", "Belmopan"], ["Canada", "Ottawa"], ["Costa Rica", "San José"], ["Cuba", "Havana"], ["Dominica", "Roseau"], ["Dominican Republic", "Santo Domingo"], ["El Salvador", "San Salvador"], ["Grenada", "St. George's"], ["Guatemala", "Guatemala City"], ["Haiti", "Port-au-Prince"], ["Honduras", "Tegucigalpa"], ["Jamaica", "Kingston"], ["Mexico", "Mexico City"], ["Nicaragua", "Managua"], ["Panama", "Panama City"], ["Saint Kitts and Nevis", "Basseterre"], ["Saint Lucia", "Castries"], ["Saint Vincent and the Grenadines", "Kingstown"], ["Trinidad and Tobago", "Port of Spain"], ["United States", "Washington, D.C."]]
elif continent == 5:
    capital_list = [["Australia", "Canberra"], ["Fiji", "Suva"], ["Kiribati", "Tarawa"], ["Marshall Islands", "Majuro"], ["Micronesia", "Palikir"], ["Nauru", "Yaren"], ["New Zealand", "Wellington"], ["Palau", "Ngerulmud"], ["Papua New Guinea", "Port Moresby"], ["Samoa", "Apia"], ["Solomon Islands", "Honiara"], ["Tonga", "Nuku'alofa"], ["Tuvalu", "Funafuti"], ["Vanuatu", "Port Vila"]]
elif continent == 6:
    capital_list = [["Argentina", "Buenos Aires"], ["Bolivia", "Sucre"], ["Brazil", "Brasília"], ["Chile", "Santiago"], ["Colombia", "Bogotá"], ["Ecuador", "Quito"], ["Guyana", "Georgetown"], ["Paraguay", "Asunción"], ["Peru", "Lima"], ["Suriname", "Paramaribo"], ["Uruguay", "Montevideo"], ["Venezuela", "Caracas"]]

capital_count=len(capital_list)
score=0
guess="start"
turns=0

print("The current high score is 🎯 ",high_score)
print("Have fun, you have 20 turns or press q to quit! Enter to skip! ")
print("")

while guess != 'q' and turns != 20:

    random_number=random.randint(0,capital_count)
    #print(random_number)

    country,capital=capital_list[random_number]

    if turns == 19:
        print("It's your last turn! ")

    guess=input("What is the capital of %s? " % country)
    
    turns = turns + 1 

    if guess.lower() == capital.lower():
        print("Great job!")
        score = score + 1
    elif guess == "q":
        print ("Bye")
    else:
        print("Whoops, thats not right, the answer is %s" % capital)
    
if score < high_score:
    print("Nice try, your score was",score)
else: 
    score_file("set_score",score)
    print("Amazing! You beat the high score! Your score is",score,"congratulations 🌈")
    
