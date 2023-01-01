"""
1. Afișați numele vostru urmat și precedat de trei caractere #.
"""
# nume = "### Gabriel Nechifor ###"
# print(nume)


"""
2. Afișați suma dintre penultima și ultima cifră a anului curent folosind o expresie aritmetică.
- Pentru anul 2021 trebuie afișat 3 (2+1). O varianta posibilă foloseste 
  expresia 2021%10 + 2020//10%10, unde % este operator pentru rest, iar // pentru determinarea câtului unei împărțiri.
"""

# anul_curent =  int(input("Please tell me your current year: "))

# print(anul_curent%10 + anul_curent//10%10)

"""
3. Folosind formula 1+2+...+n = n(n+1)/2, afișați suma primelor 100, respectiv 1000 de numere naturale.
Soluţie
Vom folosi pentru rezolvare, expresiile: 1+2+...+100 = 100*(100+1)/2 și 1+2+...+1000 = 1000*(1000+1)/2.
"""

# num_1 = int(input("Please tell me your first number: "))
# num_2 = int(input("Please tell me your second number: "))

# print(num_1*(100+1)/2)
# print(num_2*(100+1)/2)
# print(num_1*(100+1)/2);print(num_2*(100+1)/2)

"""
4. Afișați pe ecran toate cifrele pare, una sub alta.
Soluţie
Vom folosi instrucțiunea print pentru a afișa fiecare cifră pe câte un rând.
"""
# print(0); print(2); print(4)

"""
5. Afișați pe o linie numele şi prenumele vostru, pe a doua linie numărul de telefon, iar pe a treia linie adresa de email.

print(" Gabriel Nechifor", '\n',"03579696969", '\n',"Email@gmail.com")
 or
name = input("Please tell me your name: ")
name = name.title()
Phone_number = input("Please tell me your phone number: ")
email = input("Please tell me your email: ")
print(name)
print(Phone_number)
print(email)
or
print(f"{name}\n{Phone_number} \n{email}")
"""

""""
6. Afișați pe ecran, unul sub altul, cel mai mare şi cel mai mic număr format din trei cifre distincte.
"""
"""
7. Afișați toate numerele naturale formate din două cifre, care se împart exact la 20, 
în ordine descrescătoare pe aceeaşi linie, cu un spaţiu între ele.

print(80, " ", 60, " ", 40, " ", 20)
"""
