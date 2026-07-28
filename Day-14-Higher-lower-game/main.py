import random
import os

from game_data import data


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def format_country(country):
    return (
        f"{country['name']}\n"
        f"Capital : {country['capital']}\n"
        f"Continent : {country['continent']}"
    )


def check_answer(choice, country_a, country_b):
    if country_a["population"] > country_b["population"]:
        return choice == "A"
    else:
        return choice == "B"


score = 0
game_over = False

country_b = random.choice(data)

while not game_over:

    clear_screen()

    country_a = country_b
    country_b = random.choice(data)

    while country_a == country_b:
        country_b = random.choice(data)

    print("=" * 50)
    print("      HIGHER LOWER - COUNTRIES EDITION")
    print("=" * 50)

    print("\nCompare A")
    print(format_country(country_a))

    print("\nVS\n")

    print("Against B")
    print(format_country(country_b))

    choice = input("\nWhich country has the larger population? (A/B): ").upper()

    while choice not in ["A", "B"]:
        choice = input("Please enter A or B: ").upper()

    if check_answer(choice, country_a, country_b):
        score += 1
        print(f"\n✅ Correct! Your score is {score}")
        input("\nPress Enter to continue...")
    else:
        print("\n❌ Wrong Answer!")
        print(f"\n{country_a['name']} Population : {country_a['population']:,}")
        print(f"{country_b['name']} Population : {country_b['population']:,}")
        print(f"\n🏆 Final Score : {score}")
        game_over = True