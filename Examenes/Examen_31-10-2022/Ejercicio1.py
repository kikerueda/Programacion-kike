'''
Created on Oct 31, 2022

@author: Kiikerueda
'''
'''
Created on Oct 31, 2022

@author: Kiikerueda
''''''
player1=input("Elige el jugador 1 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
while not (player1=="PIEDRA" or player1=="PAPEL" or player1=="TIJERAS" or player1=="LAGARTO" or player1=="SPOCK"):
    player1=input("Elige el jugador 1 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
    
player2=input("Elige el jugador 2 (Piedra / Papel / Tijera / Lagarto / Spock): ").upper()
while not (player2=="PIEDRA" or player2=="PAPEL" or player2=="TIJERAS" or player2=="LAGARTO" or player2=="SPOCK"):
    player2=input("Elige el jugador 2 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()

if player1==player2:
    print("Empatan")
    
if player1=="PIEDRA":
    if player2=="LAGARTO" or player2=="TIJERAS":
        print(f"{player1} GANA ante {player2}")
    elif player2=="PAPEL" or player2=="SPOCK":
        print(f"{player1} PIERDE ante {player2}")
        
if player1=="PAPEL":
    if player2=="PIEDRA" or player2=="SPOCK":
        print(f"{player1} GANA ante {player2}") 
    elif player2=="TIJERAS" or player2=="LAGARTO":
        print(f"{player1} PIERDE ante {player2}")
        
if player1=="TIJERAS":
    if player2=="LAGARTO" or player2=="PAPEL":
        print(f"{player1} GANA ante {player2}")
    elif player2=="SPOCK" or player2=="PIEDRA":
        print(f"{player1} PIERDE ante {player2}")
        
if player1=="LAGARTO":
    if player2=="PAPEL" or player2=="SPOCK":
        print(f"{player1} GANA ante {player2}")  
    elif player2=="TIJERAS" or player2=="PIEDRA":
        print(f"{player1} PIERDE ante {player2}")
        
if player1=="SPOCK":
    if player2=="PIEDRA" or player2=="TIJERAS":
        print(f"{player1} GANA ante {player2}")
    elif player2=="PAPEL" or player2=="LAGARTO":
        print(f"{player1} PIERDE ante {player2}")
'''
        
print("Ejercicio 1.2")

player1=input("Elige el jugador 1 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
while not (player1=="PIEDRA" or player1=="PAPEL" or player1=="TIJERAS" or player1=="LAGARTO" or player1=="SPOCK"):
    player1=input("Elige el jugador 1 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
    
player2=input("Elige el jugador 2 (Piedra / Papel / Tijera / Lagarto / Spock): ").upper()
while not (player2=="PIEDRA" or player2=="PAPEL" or player2=="TIJERAS" or player2=="LAGARTO" or player2=="SPOCK"):
    player2=input("Elige el jugador 2 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
    
while not(player1=="SPOCK" and player2=="SPOCK"):
    if player1==player2:
        print("Empatan")
        
    if player1=="PIEDRA":
        if player2=="LAGARTO" or player2=="TIJERAS":
            print(f"{player1} GANA ante {player2}")
        elif player2=="PAPEL" or player2=="SPOCK":
            print(f"{player1} PIERDE ante {player2}")
            
    if player1=="PAPEL":
        if player2=="PIEDRA" or player2=="SPOCK":
            print(f"{player1} GANA ante {player2}") 
        elif player2=="TIJERAS" or player2=="LAGARTO":
            print(f"{player1} PIERDE ante {player2}")
            
    if player1=="TIJERAS":
        if player2=="LAGARTO" or player2=="PAPEL":
            print(f"{player1} GANA ante {player2}")
        elif player2=="SPOCK" or player2=="PIEDRA":
            print(f"{player1} PIERDE ante {player2}")
            
    if player1=="LAGARTO":
        if player2=="PAPEL" or player2=="SPOCK":
            print(f"{player1} GANA ante {player2}")  
        elif player2=="TIJERAS" or player2=="PIEDRA":
            print(f"{player1} PIERDE ante {player2}")
            
    if player1=="SPOCK":
        if player2=="PIEDRA" or player2=="TIJERAS":
            print(f"{player1} GANA ante {player2}")
        elif player2=="PAPEL" or player2=="LAGARTO":
            print(f"{player1} PIERDE ante {player2}")
    
    player1=input("Elige el jugador 1 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
    while not (player1=="PIEDRA" or player1=="PAPEL" or player1=="TIJERAS" or player1=="LAGARTO" or player1=="SPOCK"):
            player1=input("Elige el jugador 1 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()
    
    player2=input("Elige el jugador 2 (Piedra / Papel / Tijera / Lagarto / Spock): ").upper()
    while not (player2=="PIEDRA" or player2=="PAPEL" or player2=="TIJERAS" or player2=="LAGARTO" or player2=="SPOCK"):
            player2=input("Elige el jugador 2 (Piedra / Papel / Tijeras / Lagarto / Spock): ").upper()


        
    
      
        
        