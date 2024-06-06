palavras = ('Aprender', 'Python', 'Minecraft', 'Jogar', 'Fortnite',
            'Realidade', 'Roblox', 'Lua', 'Ruby', 'Rust', 'Discord')


for p in palavras:
    print(f"\nNa {p} temos ", end=' ')
    
    for letra in p.lower():
        if letra in 'aeiou':
             print(f"{letra}", end=' ')
    
