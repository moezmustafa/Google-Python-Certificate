teams = [ "Dragons", "Wolves", "Tigers", "Lions", "Panthers", "Packers", "Eagles", "Redskins" ]

for home_team in teams :
    for away_team in teams :
        if home_team != away_team :
            print(home_team, "vs", away_team)
