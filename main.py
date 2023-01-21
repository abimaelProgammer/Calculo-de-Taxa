renda = float(input("Digite sua renda anual:"))

if renda > 85528:
    taxa = 14839.02 + 0.32 * (renda - 85528)
else:
    taxa = 0.18 * renda - 556.02
if taxa < 0:
  taxa=0
taxa = round(taxa, 0)
print("A taxa é:", taxa, "thalers")