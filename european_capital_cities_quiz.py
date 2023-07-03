import random

print("Do you know the difference between Madrid and Monaco? Test your European knowledge of Geography.\nSelect one option by entering its number for each prompt.")

while True:
    countries = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kazakhstan", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom", "Vatican City"]
    capital_cities = ["Tirana", "Andorra la Vella", "Yerevan", "Vienna", "Baku", "Minsk", "Brussels", "Sarajevo", "Sofia", "Zagreb", "Nicosia", "Prague", "Copenhagen", "Tallinn", "Helsinki", "Paris", "Tbilisi", "Berlin", "Athens", "Budapest", "Reykjavík", "Dublin", "Rome", "Astana", "Riga", "Vaduz", "Vilnius", "Luxembourg", "Valletta", "Chișinău", "Monaco", "Podgorica", "Amsterdam", "Skopje", "Oslo", "Warsaw", "Lisbon", "Bucharest", "Moscow", "San Marino", "Belgrade", "Bratislava", "Ljubljana", "Madrid", "Stockholm", "Bern", "Ankara", "Kyiv", "London", "Vatican City"]

    formal_names = ["Republic of Albania", "Principality of Andorra", "Republic of Armenia", "Republic of Austria", "Republic of Azerbaijan", "Republic of Belarus", "Kingdom of Belgium", "Bosnia and Herzegovina", "Republic of Bulgaria", "Republic of Croatia", "Republic of Cyprus", "Czech Republic", "Kingdom of Denmark", "Republic of Estonia", "Republic of Finland", "French Republic", "Georgia", "Federal Republic of Germany", "Hellenic Republic", "Hungary", "Iceland", "Ireland", "Italian Republic", "Republic of Kazakhstan", "Republic of Latvia", "Principality of Liechtenstein", "Republic of Lithuania", "Grand Duchy of Luxembourg", "Republic of Malta", "Republic of Moldova", "Principality of Monaco", "Montenegro", "Kingdom of the Netherlands", "Republic of North Macedonia", "Kingdom of Norway", "Republic of Poland", "Portuguese Republic", "Romania", "Russian Federation", "Republic of San Marino", "Republic of Serbia", "Slovak Republic", "Republic of Slovenia", "Kingdom of Spain", "Kingdom of Sweden", "Swiss Confederation", "Republic of Turkey", "Ukraine", "United Kingdom of Great Britain and Northern Ireland", "Vatican City State"]
    iso_codes = ["ALB", "AND", "ARM", "AUT", "AZE", "BLR", "BEL", "BIH", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "GEO", "DEU", "GRC", "HUN", "ISL", "IRL", "ITA", "KAZ", "LVA", "LIE", "LTU", "LUX", "MLT", "MDA", "MCO", "MNE", "NLD", "MKD", "NOR", "POL", "PRT", "ROU", "RUS", "SMR", "SRB", "SVK", "SVN", "ESP", "SWE", "CHE", "TUR", "UKR", "GBR", "VAT"]

    formal_names_for_sentences = ["the Republic of Albania", "the Principality of Andorra", "the Republic of Armenia", "the Republic of Austria", "the Republic of Azerbaijan", "the Republic of Belarus", "the Kingdom of Belgium", "Bosnia and Herzegovina", "the Republic of Bulgaria", "the Republic of Croatia", "the Republic of Cyprus", "the Czech Republic", "the Kingdom of Denmark", "the Republic of Estonia", "the Republic of Finland", "the French Republic", "Georgia", "the Federal Republic of Germany", "the Hellenic Republic", "Hungary", "Iceland", "Ireland", "the Italian Republic", "the Republic of Kazakhstan", "the Republic of Latvia", "the Principality of Liechtenstein", "the Republic of Lithuania", "the Grand Duchy of Luxembourg", "the Republic of Malta", "the Republic of Moldova", "the Principality of Monaco", "Montenegro", "the Kingdom of the Netherlands", "the Republic of North Macedonia", "the Kingdom of Norway", "the Republic of Poland", "the Portuguese Republic", "Romania", "the Russian Federation", "the Republic of San Marino", "the Republic of Serbia", "the Slovak Republic", "the Republic of Slovenia", "the Kingdom of Spain", "the Kingdom of Sweden", "the Swiss Confederation", "the Republic of Turkey", "Ukraine", "the United Kingdom of Great Britain and Northern Ireland", "the Vatican City State"]

    de_facto_countries = ["Abkhazia", "Artsakh", "Kosovo", "Northern Cyprus", "South Ossetia", "Transnistria"]
    capital_cities_of_de_facto_countries = ["Sukhumi", "Stepanakert", "Pristina", "North Nicosia", "Tskhinvali", "Tiraspol"]

    number_of_correct_answers = 0

    print("\n1 - guess the countries with the given capital cities")
    print("2 - guess the capital cities of the given countries")
    print("3 - guess either the country with the given capital city or vice versa for each question")
    print("4 - view the list of countries")
    print("5 - view the list of capital cities")
    print("6 - view the list of countries and their capital cities, formal names and ISO codes")
    print("7 - stop\n")
    user_input_1 = input("Enter the number here - ")
    if user_input_1 in ["1", "2", "3"]:
        print(f"Select a number from 3 to {len(countries)} for the number of questions (eg: 9).")
        while True:
            user_input_2 = input("Enter the number here - ")
            if user_input_2 in [str(i) for i in range(3, len(countries) + 1)]:
                sampled_range = random.sample(range(len(countries)), int(user_input_2))
                unanswered_countries = [countries[i] for i in sampled_range]
                unanswered_capital_cities = [capital_cities[i] for i in sampled_range]
                while unanswered_countries:
                    random_number_1 = random.randint(0, len(unanswered_countries) - 1)
                    random_number_2 = random.randint(0, 1)
                    if user_input_1 == "1" or (user_input_1 == "3" and random_number_2 == 0):
                        choices = [unanswered_capital_cities[random_number_1]] + random.sample([i for i in (capital_cities + capital_cities_of_de_facto_countries) if i != unanswered_capital_cities[random_number_1]], 3)
                        random.shuffle(choices)
                        print(f"{int(user_input_2) - len(unanswered_countries) + 1}/{int(user_input_2)} Which of the following is the capital city of {unanswered_countries[random_number_1]}?")
                    else:
                        choices = [unanswered_countries[random_number_1]] + random.sample([i for i in (countries + de_facto_countries) if i != unanswered_countries[random_number_1]], 3)
                        random.shuffle(choices)
                        print(f"{int(user_input_2) - len(unanswered_countries) + 1}/{int(user_input_2)} {unanswered_capital_cities[random_number_1]} is the capital city of which of the following?")
                    [print(f"\t{i + 1} - {choices[i]}") for i in range(len(choices))]
                    while True:
                        user_input_3 = input("Enter the number here - ")
                        if user_input_3 in ["1", "2", "3", "4"]:
                            if choices[int(user_input_3) - 1] in [unanswered_countries[random_number_1], unanswered_capital_cities[random_number_1]]:
                                number_of_correct_answers += 1
                                print("Correct!")
                            else:
                                print("Wrong!")
                            print(f"{unanswered_capital_cities[random_number_1]} is the capital city of {formal_names_for_sentences[countries.index(unanswered_countries[random_number_1])]} ({iso_codes[countries.index(unanswered_countries[random_number_1])]}).")
                            formal_names_for_sentences.pop(countries.index(unanswered_countries[random_number_1]))
                            iso_codes.pop(countries.index(unanswered_countries[random_number_1]))
                            countries.remove(unanswered_countries[random_number_1])
                            capital_cities.remove(unanswered_capital_cities[random_number_1])
                            unanswered_countries.pop(random_number_1)
                            unanswered_capital_cities.pop(random_number_1)
                            break
                        else:
                            print("Error!")
                print(f"Your score: {number_of_correct_answers}/{int(user_input_2)} ({number_of_correct_answers * 100/int(user_input_2):.2f}%)")
                if number_of_correct_answers/int(user_input_2) <= 1/3:
                    print("It looks like you might want to revise your European knowledge.")
                elif number_of_correct_answers/int(user_input_2) <= 2/3:
                    print("Not bad, maybe have another go?")
                else:
                    print("Nice work, looks like you've been revising your Geography!")
                break
            else:
                print("Error!")
    if user_input_1 in ["4", "5", "6"]:
        for i in range(len(countries)):
            print([countries, sorted(capital_cities), [f"{j + 1} {countries[j]} - {capital_cities[j]} - {formal_names[j]} - {iso_codes[j]}" for j in range(len(countries))]][int(user_input_1) - 4][i])
    while user_input_1 in ["1", "2", "3", "4", "5", "6"]:
        print("\n1 - start again")
        user_input_4 = input("2 - stop\n")
        if user_input_4 == "1":
            break
        if user_input_4 == "2":
            print("Based on: Quiz: European Capital Cities - CBBC - BBC (https://www.bbc.co.uk/cbbc/quizzes/top-class-european-capital-cities) (UK only)")
            print("References: List of sovereign states and dependent territories in Europe - Wikipedia (https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_in_Europe)")
            break
        print("Error!")
    if user_input_1 == "7" or user_input_4 == "2":
        break
    if user_input_1 not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Error!\n")
