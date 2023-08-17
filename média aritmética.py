BIM1= float(input("Digite a nota do 1 bimestre:"))
BIM2= float(input("Digite a nota do 2 bimestre:"))
BIM3= float(input("Digite a nota do 3 bimestre:"))
BIM4= float(input("Digite a nota do 4 bimestre:"))
MEDIA= float((BIM1+BIM2+BIM3+BIM4)/4)
print ("Digite a média:",MEDIA)
if MEDIA>=9:
   print ("Aprovado com louvor!")
elif MEDIA>=7:
   print("Aprovado")
elif MEDIA<7:
    print("Reprovado")