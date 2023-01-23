from tkinter import *
import customtkinter

# Création de la fenêtre principale, en la nommant et en lui donnant une taille. 
main = Tk()
main.title("Calculatrice 9000")
main.geometry("380x400")

# Création d'une variable qui stockera le calcul
input = ""
calcul_en_cours = ""
# Création d'une variable "Stringvar" qui stockera le résultats
output = StringVar()

# Creation d'une liste pour stocker les calculs effectuer
historique = []

 # historique
ouverture_historique = False

liste_historique = Listbox()


# Fonction pour voir l'historique
def montrer_historique():
  global ouverture_historique, liste_historique
  
  
  if ouverture_historique:
    liste_historique.destroy()
    ouverture_historique = False
  else:
    liste_historique = Listbox(main, fg="black", bg="light gray")
    liste_historique.place(x=10, y=80, width=360, height=120)
    for calculation in historique:
      liste_historique.insert(END, calculation) 
    ouverture_historique = True

# Fonction pour clear l'historique
def effacer_historique():
  historique.clear()
  
  
  
# Fonction pour enregistrer le calcul
def clic_bouton(clic):
  global input, calcul_en_cours
  calcul_en_cours += clic
  input += clic
  output.set(input)
    
  
  # Fonction pour calculer
def calculer():
  global input, calcul_en_cours
  try:
    résultat = eval(input)
    input = str(résultat)
    output.set(résultat)
    historique.append(calcul_en_cours + " = " + str(résultat))
    calcul_en_cours = str(résultat)
  except(ValueError, SyntaxError):
    output.set("Entré non valide.")
    input = ""
    
    
# Fonction pour effacer le calcul
def effacer():
    global input, calcul_en_cours
    input = ""
    calcul_en_cours = ""
    output.set("")
    
# Fonction pour calculer un carré
def carré():
    global input
    try:
        input = float(input)
        résultat = input**2
        input = str(résultat)
        output.set(résultat)
    except:
        output.set("Entré non valide.")
        input = ""

# Fonction pour calculer une racine carré
def racine():
  global input
  try:
    input = float(input)
    résultat = input**(1/2)
    input = str(résultat)
    output.set(résultat)
  except:
    output.set(résultat)
    input = ""

def effacer_dernier():
  global input, calcul_en_cours
  input = input[:-1]
  calcul_en_cours = calcul_en_cours[:-1]
  output.set(input)


# Bouton pour afficher l'historique
bouton_historique = customtkinter.CTkButton(
  main, 
  command= montrer_historique,
  corner_radius=5,
  text = "Historique",
  )



bouton_historique.place(
  x=0,
  y=0, 
  height=32,
  width=120
  )

# Clear history button
effacer_historique_bouton = customtkinter.CTkButton(
  main,
  corner_radius=5
)
effacer_historique_bouton = Button(
  main, 
  relief=RAISED, 
  activebackground="gray", 
  activeforeground="dark gray", 
  text="Effacer Historique", 
  command= effacer_historique
  )
effacer_historique_bouton.place(
  x=0, 
  y=32, 
  height=32, 
  width=120
)





# Mise en place de l'espace pour le resultat
résultat = Entry(
  main, 
  bg="black", 
  font=("Sergoe UI", 25, "bold"), 
  fg="white", 
  )
résultat = customtkinter.CTkEntry(
  main,
  corner_radius=10,
  textvariable=output,
  justify=RIGHT
)
résultat.place(
  x=120, 
  y=0, 
  height=70, 
  width=260
  )

# Boutons de la première ligne 
bouton_racine = customtkinter.CTkButton(
  main, 
  text="sqrt", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command= racine
  )
  
bouton_racine.place(
  x=0, 
  y=80, 
  height=60, 
  width=95
  )

bouton_carré = customtkinter.CTkButton(
  main, 
  text="x²", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command= carré
)
bouton_carré.place(
  x=95, 
  y=80, 
  height=60, 
  width=95
  )


bouton_multi = customtkinter.CTkButton(
  main, 
  text="x", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("*")
)
bouton_multi.place(
  x=190, 
  y=80, 
  height=60, 
  width=95
  )



bouton_retour = customtkinter.CTkButton(
  main, 
  text="⌫", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command= effacer_dernier
)
bouton_retour.place(
  x=285, 
  y=80, 
  height=60, 
  width=95
  )

# Boutons de la deuxième ligne
bouton_7 = customtkinter.CTkButton(
  main, 
  text="7", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("7")
  
)
bouton_7.place(
  x=0, 
  y=145, 
  height=60, 
  width=95
  )

bouton_8 = customtkinter.CTkButton(
  main, 
  text="8", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("8")
)
bouton_8.place(
  x=95, 
  y=145, 
  height=60, 
  width=95
  )

bouton_9 = customtkinter.CTkButton(
  main, 
  text="9", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("9")
)
bouton_9.place(
  x=190, 
  y=145, 
  height=60, 
  width=95
  )

bouton_div = customtkinter.CTkButton(
  main, 
  text="/", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("/")
)
bouton_div.place(
  x=285, 
  y=145, 
  height=60, 
  width=95
)

# Boutons de la troisième ligne
bouton_4 = customtkinter.CTkButton(
  main, 
  text="4", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("4")
)
bouton_4.place(
  x=0, 
  y=210, 
  height=60, 
  width=95
)

bouton_5 = customtkinter.CTkButton(
  main, 
  text="5", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("5")
)
bouton_5.place(
  x=95, 
  y=210, 
  height=60, 
  width=95
)

bouton_6 = customtkinter.CTkButton(
  main, 
  text="6", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("6")
)
bouton_6.place(
  x=190, 
  y=210, 
  height=60, 
  width=95
)
bouton_plus = customtkinter.CTkButton(
  main, 
  text="+", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("+")
)
bouton_plus.place(
  x=285, 
  y=210, 
  height=60, 
  width=95
)


# Boutons de la quatrième ligne
bouton_1 = customtkinter.CTkButton(
  main, 
  text="1", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("1")
)
bouton_1.place(
  x=0, 
  y=275, 
  height=60, 
  width=95
)

# 
bouton_2 = customtkinter.CTkButton(
  main, 
  text="2", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("2")
)
bouton_2.place(
  x=95, 
  y=275, 
  height=60, 
  width=95
)

# 
bouton_3 = customtkinter.CTkButton(
  main, 
  text="3", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("3")
)
bouton_3.place(
  x=190, 
  y=275, 
  height=60, 
  width=95
)

# MOINS
bouton_moins = customtkinter.CTkButton(
  main, 
  text="-", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("-")
)
bouton_moins.place(
  x=285, 
  y=275, 
  height=60, 
  width=95
)

# Boutons de la cinquième ligne
bouton_clear = customtkinter.CTkButton(
  main, 
  text="C", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: effacer()
)
bouton_clear.place(
  x=0, 
  y=340, 
  height=60, 
  width=95
)


bouton_0 = customtkinter.CTkButton(
  main, 
  text="0", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton("0")
  )
bouton_0.place(
  x=95, 
  y=340, 
  height=60, 
  width=95
)


bouton_point = customtkinter.CTkButton(
  main, 
  text=".", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command=lambda: clic_bouton(".")
)
bouton_point.place(
  x=190, 
  y=340, 
  height=60, 
  width=95
)


bouton_egale = customtkinter.CTkButton(
  main, 
  text="=", 
  font=("Sergoe UI", 14), 
  corner_radius=10,
  fg_color="black",
  text_color="silver",
  command= calculer
)
bouton_egale.place(
  x=285, 
  y=340, 
  height=60, 
  width=95
)

main.mainloop()
