import tkinter as tk
import vlc

app = tk.Tk()
app.title("Voice Fongbe")
app.geometry("600x400")




label = tk.Label(text="Spéculation")
label.pack()
entry2 = tk.Entry()
entry2.pack()

label = tk.Label(text="Variété")
label.pack()
entry3 = tk.Entry()
entry3.pack()

label = tk.Label(text="Marché")
label.pack()
entry4 = tk.Entry()
entry4.pack()


label = tk.Label(text="Prix")
label.pack()
entry = tk.Entry()
entry.pack()



def spell_callback():
    prix = int(entry.get())
    speculation = str(entry2.get())
    variete = str(entry3.get())
    marche = str(entry4.get())
    denree = speculation+variete
    link = "http://127.0.0.1:5000/read/"+str(prix)+'/'+str(denree)+'/'+str(marche)
    p = vlc.MediaPlayer(link)
    p.play()


button = tk.Button(text="Lire", command=spell_callback)
button.pack()

app.mainloop()
