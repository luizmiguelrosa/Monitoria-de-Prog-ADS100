data = input("Digite a sua data de nascimento (DD/MM): ")

# usando essa forma, conseguimos desempacotar todos os dados para cada variável
dia, mes = data.split("/")
dia, mes = int(dia), int(mes)

'''
Áries: de 21 de março a 20 de abril;
Touro: de 21 de abril a 20 de maio;
Gêmeos: de 21 de maio a 20 de junho;
Câncer: de 21 de junho a 22 de julho;
Leão: de 23 de julho a 22 de agosto;
Virgem: de 23 de agosto a 22 de setembro;
Libra: de 23 de setembro a 22 de outubro;
Escorpião: de 23 de outubro a 21 de novembro;
Sagitário: de 22 de novembro a 21 de dezembro;
Capricórnio: de 22 de dezembro a 20 de janeiro;
Aquário: de 21 de janeiro a 18 de fevereiro;
Peixes: de 19 de fevereiro a 20 de março;
'''

if (dia >= 21 and mes == 3) or (dia <=20 and mes == 4):
    signo = "Áries"
# v...

print(f"O signo é {signo}")