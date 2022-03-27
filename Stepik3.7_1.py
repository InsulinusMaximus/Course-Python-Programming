#1 
#Принимаю общее число игр
num_games = int(input())

#Заполняю двумерный массив нулями
games = [[0 for _ in range(4)] for _ in range(num_games)]

#Принимаю игры и количество голов в них

for num_game in range(num_games):
    games[num_game] = input().split(';')
 
#Обрабатываю двумерный массив и перевожу результаты в словарь с ключем <Команда>

def team_res(g):
    team={}
    num_of_games = wins = loses = points= 0
    
    for game in range(len(g)):
        # Если ПЕРВАЯ команда выиграла
        if int(g[game][1]) > int(g[game][3]):
            # Если первой нет в словаре     
            if g[game][0] not in team:
                num_of_games = 1
                wins = 1
                loses = 0
                draw = 0
                points = 3
                team.update({g[game][0] : [num_of_games, wins, draw, loses, points]})
            # Если первая есть в словаре   
            elif g[game][0] in team:
                team[g[game][0]][0] += 1
                team[g[game][0]][1] += 1
                team[g[game][0]][2] += 0
                team[g[game][0]][3] += 0
                team[g[game][0]][4] += 3
                
            # Если второй, проигравшей команды нет в словаре
            if g[game][2] not in team:
                num_of_games = 1
                wins = 0
                draw = 0
                loses = 1
                points = 0
                team.update({g[game][2] : [num_of_games, wins, draw, loses, points]})

            # Если вторая, проигравшая команда есть в словаре
            elif g[game][2] in team:
                team[g[game][2]][0] += 1
                team[g[game][2]][1] += 0
                team[g[game][2]][2] += 0
                team[g[game][2]][3] += 1
                team[g[game][2]][4] += 0

        # Если ВТОРАЯ команда выиграла
        if int(g[game][1]) < int(g[game][3]):
            # Если первой, проигравшей команды нет в словаре     
            if g[game][0] not in team:
                num_of_games = 1
                wins = 0
                draw = 0
                loses = 1
                points = 0
                team.update({g[game][0] : [num_of_games, wins, draw, loses, points]})
            # Если первая, проигравшая команда есть в словаре   
            elif g[game][0] in team:
                team[g[game][0]][0] += 1
                team[g[game][0]][1] += 0
                team[g[game][0]][2] += 0
                team[g[game][0]][3] += 1
                team[g[game][0]][4] += 0
                
            # Если второй команды нет в словаре
            if g[game][2] not in team:
                num_of_games = 1
                wins = 1
                draw = 0
                loses = 0
                points = 3
                team.update({g[game][2] : [num_of_games, wins, draw, loses, points]})

            # Если вторая команда есть в словаре
            elif g[game][2] in team:
                team[g[game][2]][0] += 1
                team[g[game][2]][1] += 1
                team[g[game][2]][2] += 0
                team[g[game][2]][3] += 0
                team[g[game][2]][4] += 3 
        # Если НИЧЬЯ
        if int(g[game][1]) == int(g[game][3]):
            # Если первой нет в словаре     
            if g[game][0] not in team:
                num_of_games = 1
                wins = 0
                draw = 1
                loses = 0
                points = 1
                team.update({g[game][0] : [num_of_games, wins, draw, loses, points]})
            # Если первая есть в словаре   
            elif g[game][0] in team:
                team[g[game][0]][0] += 1
                team[g[game][0]][1] += 0
                team[g[game][0]][2] += 1
                team[g[game][0]][3] += 0
                team[g[game][0]][4] += 1 
            # Если второй нет в словаре
            if g[game][2] not in team:
                num_of_games = 1
                wins = 0
                draw = 1
                loses = 0
                points = 1
                team.update({g[game][2] : [num_of_games, wins, draw, loses, points]})
            # Если вторая есть в словаре   
            elif g[game][2] in team:
                team[g[game][2]][0] += 1
                team[g[game][2]][1] += 0
                team[g[game][2]][2] += 1
                team[g[game][2]][3] += 0
                team[g[game][2]][4] += 1                

    return team

for team, value in team_res(games).items():
    print(team+':', *value)