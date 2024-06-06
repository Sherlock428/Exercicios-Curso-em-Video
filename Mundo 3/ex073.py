times = ("Palmeiras",
    "Grêmio",
    "Atlético-MG",
    "Flamengo",
    "Botafogo",
    "Bragantino",
    "Fluminense",
    "Athletico-PR",
    "Internacional",
    "Fortaleza",
    "São Paulo",
    "Cuiabá",
    "Corinthians",
    "Cruzeiro",
    "Vasco",
    "Bahia",
    "Santos",
    "Goiás",
    "Coritiba",
    "América-MG")

while True:
    times_1 = ", ".join(map(str, times))
    primeiros_times = ", ".join(map(str, times[:3]))
    ultimos_times = ", ".join(map(str, times[-3:]))
    a_times = sorted(times)
    ordem_times = ", ".join(map(str, a_times))
    
    print(f"""
==============================================
O Ranking dos times é: {times_1}

Os primeiros são: {primeiros_times}

Os que ficaram em último são: {ultimos_times}

Em ordem Alfabetica: {ordem_times}
==============================================
""")
    

    
    time = input("Qual time você quer saber a posição?: ")

    if time in times:
        pesquisar_time = times.index(time)
        print(f"time {time} está na posição {pesquisar_time + 1}")
        

    else:
        print("time não encontrado")

    continua = ' '
    while continua not in 'SN':
        continua = input("Deseja continuar: (S/N): ").strip().upper()
    
    if continua == "N":
        break