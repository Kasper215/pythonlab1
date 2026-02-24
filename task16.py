import random
import itertools
from datetime import datetime, timedelta

def generate_tournament():
    teams = [
        "Зенит", "Спартак", "ЦСКА", "Локомотив", 
        "Краснодар", "Динамо", "Ростов", "Ахмат",
        "Реал Мадрид", "Бавария", "Ливерпуль", "Манчестер Сити",
        "ПСЖ", "Ювентус", "Барселона", "Челси"
    ]
    
    random.shuffle(teams)
    
    groups = {}
    for i in range(4):
        groups[f"Группа {chr(65+i)}"] = teams[i*4 : (i+1)*4]
    
    print("--- СОСТАВ ГРУПП ---")
    for group_name, members in groups.items():
        print(f"{group_name}: {', '.join(members)}")
    print("\n--- КАЛЕНДАРЬ ИГР ---")

    current_year = datetime.now().year
    game_date = datetime(current_year, 9, 14, 22, 45)
    
    
    rounds = [[], [], []] # 3 игровых дня
    
    for group_name, members in groups.items():
        m = members
        rounds[0].append((m[0], m[1], group_name))
        rounds[0].append((m[2], m[3], group_name))
        
        rounds[1].append((m[0], m[2], group_name))
        rounds[1].append((m[1], m[3], group_name))
        
        rounds[2].append((m[0], m[3], group_name))
        rounds[2].append((m[1], m[2], group_name))

    for i, games in enumerate(rounds, 1):
        date_str = game_date.strftime("%d/%m/%Y, %H:%M")
        print(f"Тур {i} - {date_str}:")
        for team1, team2, g_name in games:
            print(f"  [{g_name}] {team1} - {team2}")
        
        game_date += timedelta(weeks=2)

if __name__ == "__main__":
    generate_tournament()
