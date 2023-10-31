import database, logic

print("Primeiro Cenário - Trazendo todos os inscritos com o filtro vazio.")
print(logic.search(database.courses, []))
print()

print("Segundo Cenário - Trazendo somente os inscritos em um determinado curso.")
print(logic.search(database.courses, ['espanhol']))
print()

print("Terceiro Cenário - Trazendo somente os inscritos em um determinado curso em um determinado nível.")
print(logic.search(database.courses, ['espanhol', 'iniciante']))
print()

print("Quarto Cenário - Trazendo somente os inscritos de um determinado curso, nivel e turno..")
print(logic.search(database.courses, ['ingles', 'avancado', 'manha']))
print()
