import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# Wechsel in der aktuellen Pfad der Datei

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
os.chdir(script_dir)
datenbank_txt_name = 'Datenbank_Register_ID.txt'

#%% Erstellung der Klasse Register_ID
class Register_ID:

    # Erstellung der Listen und des json-pack
    ids = []
    first_names = []
    last_names = []
    ages = []
    emails = []
    streets = []
    house_numbers = []
    post_codes = []
    citys = []
    json_pack = {}

    # Erstellung der self init
    def __init__(self, id: int, vorname: str, nachname:str, alter: int, email: str, strasse: str, hausnummer: str, plz: int, stadt: str, **optionals) -> None:
        self.id = id
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter
        self.email = email
        self.strasse = strasse
        self.hausnummer = hausnummer
        self.plz = plz
        self.stadt = stadt
        self.optionals = optionals
        self.add_id(id, vorname, nachname, alter, email, strasse, hausnummer, plz, stadt)
        self.add_json()

    # Funktion zur automtischen Füllung derListen
    def add_id(self, id: int, vorname: str, nachname:str, alter: int, email: str, strasse: str, hausnummer: str, plz: int, stadt: str):
        Register_ID.ids.append(id)
        Register_ID.first_names.append(vorname)
        Register_ID.last_names.append(nachname)
        Register_ID.ages.append(alter)
        Register_ID.emails.append(email)
        Register_ID.streets.append(strasse)
        Register_ID.house_numbers.append(hausnummer)
        Register_ID.post_codes.append(plz)
        Register_ID.citys.append(stadt)

    # Funktion zur automatischen Füllung des json-Dictionary    
    def add_json(self):
        json_eintrag = {
            "vorname": self.vorname,
            "nachname": self.nachname,
            "alter": self.alter,
            "email": self.email,
            "strasse": self.strasse,
            'hausnummer': self.hausnummer,
            "plz": self.plz,
            "stadt": self.stadt,
            "optional": self.optionals
        }
        Register_ID.json_pack[self.id] = json_eintrag

    # Funktion zur Löschung von Einträgen
    @classmethod
    def remove_id(cls, id: int):
        if id in cls.ids:
            index = cls.ids.index(id)
            cls.ids.pop(index)
            cls.first_names.pop(index)
            cls.last_names.pop(index)
            cls.ages.pop(index)
            cls.emails.pop(index)
            cls.streets.pop(index)
            cls.house_numbers.pop(index)
            cls.post_codes.pop(index)
            cls.citys.pop(index)
            cls.json_pack.pop(id, None)
            print('Eintrag wurde gelöscht !\n')

#%% Funktion zur Erstellung des Eintrags in die -> class Register_ID

# Funktion zur Abholung der Daten aus der Klasse -> datenbank_starten -> aus der Methode -> erstellung_neuer_eintrag
def eintrag_erstellen(vorname, nachname, alter, email, strasse, hausnummer, postleitzahl, stadt, **optionals) -> None:

    # Funktion zur Erstellung einer nicht vorhandenen ID-Nummer und Übergabe an die -> class Register ID
    def abfrage_neue_id(id_vorname: str, id_nachname: str, id_age: int, id_email: str, id_strasse: str, id_hausnummer: str, id_plz: int, id_stadt: str, **optionals) -> None:
        id = 1
        while id in Register_ID.ids:
            id += 1
        # Übergabe der Daten zur Erstellung
        Register_ID(id, id_vorname, id_nachname, id_age, id_email, id_strasse, id_hausnummer, id_plz, id_stadt, **optionals)
        # Erstellung der Messagebox wenn Erstellung erfolgreich
        message = (
        f'\n### Neuer Datensatz wird verarbeitet ###\n\n'
        f'ID: {id}\n'
        f'Vorname: {id_vorname}\n'
        f'Nachname: {id_nachname}\n'
        f'Alter: {id_age}\n'
        f'Email: {id_email}\n'
        f'Strasse: {id_strasse} {id_hausnummer}\n'
        f'PLZ / Ort: {id_plz} {id_stadt}\n'
        )    
        if optionals:
            for key, value in optionals.items():
                message += f'{key}: {value}\n'        
        message += '\n### Neuer Datensatz erfolgreich erstellt ###\n'
        messagebox.showinfo("Bestätigung neuer Eintrag", message)
        

    id_vorname = vorname
    id_nachname = nachname
    id_age = alter
    id_email = email
    id_strasse = strasse
    id_hausnummer = hausnummer
    id_plz = postleitzahl
    id_stadt = stadt
    # Weiterleitung der Daten zur ID-Vergabe
    abfrage_neue_id(id_vorname, id_nachname, id_age, id_email, id_strasse, id_hausnummer,  id_plz, id_stadt, **optionals)
      
#%% Laden / Speichern der Datenbank
laden_der_datenbank_inhalt = ''

try:
    with open(datenbank_txt_name) as reader:
        json_pack = json.load(reader)
    laden_der_datenbank_inhalt = 'Datenbank gefunden, laden mit -> Datenbank laden'
except:
    laden_der_datenbank_inhalt = 'Bitte neue Datenbank erstellen mit -> Datenbank laden'

# Funktion zur Speicherung der Datenbank    
def datenbank_speichern():
    if len(Register_ID.ids) < 1:
        messagebox.showerror('Fehler', 'Keine Datenbank geladen !')        
    else:
        with open('Datenbank_Register_ID.txt', 'w') as writer:
            json.dump(Register_ID.json_pack, writer)
        messagebox.showinfo('Save...', 'Datenbank erfolgreich gesichert !')

#%% Programm Start nach laden der Datenbank

# Erstellung der GUI nach Start/Laden
class datenbank_starten():

    def __init__(self, hintergund) -> None:
        self.hintergrund = hintergrund
        self.init_gui()
        
    # Funktion zur Auflistung aller Einträge in der Datenbank
    def alle_eintraege_anzeigen(self):

        # Leerung des Text-Widget als Vorbereitung
        self.text_widget.delete('1.0', tk.END)        
        self.text_widget.insert('1.0', "Vollständige Datensatz geladen...\n\n")    
    
        # Daten formatieren und in das Text-Widget einfügen
        for index in range(len(Register_ID.ids)):
            self.text_widget.insert(tk.END,
                f'ID: {Register_ID.ids[index]} - {Register_ID.first_names[index]} {Register_ID.last_names[index]}, '
                f'{Register_ID.ages[index]} Jahre alt, {Register_ID.emails[index]}, '
                f'{Register_ID.streets[index]} {Register_ID.house_numbers[index]}, '
                f'{Register_ID.post_codes[index]} {Register_ID.citys[index]}\n'
            )
    
    # Erstellung der Flächen auf der GUI 
    def init_gui(self):

        # Fehleranzeige falls Datenbank schon geladen
        if len(Register_ID.ids) > 1:
            messagebox.showinfo("Hinweis", 'Datenbank bereits geladen !')
        
        # Laden der Datenbank
        else:
            datenbank_txt_name = 'Datenbank_Register_ID.txt'    
            try:
                with open(datenbank_txt_name) as reader:
                    json_pack = json.load(reader)    
                print('##### Intialisierung Datenbank #####\n')
                print('Datenbank gefunden, wird geladen...\n')

            # Füllen der Datenbank aus der Datenbankdatei        
                for i in json_pack:
                        vorname = json_pack[i].get('vorname')
                        nachname = json_pack[i].get('nachname')
                        alter = json_pack[i].get('alter')
                        email = json_pack[i].get('email')
                        strasse = json_pack[i].get('strasse')
                        hausnummer = json_pack[i].get('hausnummer')
                        plz = json_pack[i].get('plz')
                        stadt = json_pack[i].get('stadt')
                        optional = json_pack[i].get('optional', {})
                        erstelle_eintrag = Register_ID(int(i),vorname, nachname, alter, email, strasse, hausnummer, plz, stadt, **optional)
                print('##### Initialisierung beendet - Einträge geladen #####\n')
                messagebox.showinfo('Load...', 'Datenbank erfolgreich geladen !')

            # Erstellung einer neuen Datenbank falls keine Datenbank vorhanden
            except:
                print('##### Intialisierung Datenbank #####\n')
                print('Es ist keine aktuelle Datenbank vorhanden. Neue Datenbank erstellt !\n')
                print('##### Intialisierung beendet #####\n')
                with open('Datenbank_Register_ID.txt', 'w') as writer:
                    writer.write('')
                messagebox.showinfo('Build...', 'Datenbank erfolgreich erstellt !')
            # Löschung des Startbildschirms
            startframe.destroy()

            # Erstellung des Programmbildschirms
            self.hauptframe = tk.LabelFrame(hintergrund, bg="lightgrey")
            self.hauptframe.place(x = 27.5, y = 200, width = 1145, height = 572.5)

            # Menüleisten Eintrag 2
            menue2 = tk.Menu(menubar, tearoff=0, font=('arial', 18))
            menubar.add_cascade(label='Einträge', menu=menue2)
            menue2.add_command(label='Eintrag erstellen', command=self.erstellung_neuer_eintrag)
            menue2.add_command(label="Eintrag bearbeiten", command=self.eintraege_bearbeiten)
            menue2.add_command(label="Eintrag löschen", command=self.eintrag_loeschen)

            # Menüleisten Eintrag 3
            menue3 = tk.Menu(menubar, tearoff=0, font=('arial', 18))
            menubar.add_cascade(label='Datensatz', menu=menue3)
            menue3.add_command(label='Kompletten Datensatz anzeigen ( einfache Ansicht, ohne optionale Angaben )', command=self.alle_eintraege_anzeigen)
            menue3.add_separator()

            # Menüleisten Eintrag 4
            menue4 = tk.Menu(menubar, tearoff=0, font=('arial', 18))
            menubar.add_cascade(label='Beenden', menu=menue4)
            menue4.add_command(label='Beenden', command=self.programm_ende)

            # Erstellung des weißen Text-Widget
            self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
            self.text_widget.place(width=850, height=500, x=10, y=60)

            # Erstellung Überschrift
            start_label = ttk.Label(self.hauptframe, text='Personen - Datenbank', font=('arial', 30), padding=5)
            start_label.configure(background='lightgrey')
            start_label.place(x=230)

            # Erstellung der Suche-Leiste
            ueberschrift_suche_felder = tk.Label(self.hauptframe, text='Optionale Detailsuche :', relief='flat', font=('arial', 18))
            ueberschrift_suche_felder.place(x=870, y=60)

            label_id_suche = tk.Label(self.hauptframe, text='ID:', font=('arial',12), anchor='w')
            label_id_suche.place(width=100, height=30, x=870, y=130)
            self.id_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.id_suche.place(width=150, height=30, x=975, y=130)
            self.id_suche.insert(0, '- Eingabe -')
            self.id_suche.bind("<Button-1>", self.clear_entry)
            self.id_suche.bind('<Return>', self.id_suchen) 

            label_vorname_suche = tk.Label(self.hauptframe, text='Vorname:', font=('arial',12), anchor='w')
            label_vorname_suche.place(width=100, height=30, x=870, y=180)
            self.vorname_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.vorname_suche.place(width=150, height=30, x=975, y=180)
            self.vorname_suche.insert(0, '- Eingabe -')
            self.vorname_suche.bind("<Button-1>", self.clear_entry)
            self.vorname_suche.bind('<Return>', self.vorname_suchen)

            label_nachname_suche = tk.Label(self.hauptframe, text='Nachname:', font=('arial',12), anchor='w')
            label_nachname_suche.place(width=100, height=30, x=870, y=230)
            self.nachname_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.nachname_suche.place(width=150, height=30, x=975, y=230)
            self.nachname_suche.insert(0, '- Eingabe -')
            self.nachname_suche.bind("<Button-1>", self.clear_entry)
            self.nachname_suche.bind('<Return>',self.nachname_suchen )

            label_alter_suche = tk.Label(self.hauptframe, text='Alter:', font=('arial',12), anchor='w')
            label_alter_suche.place(width=100, height=30, x=870, y=280)
            self.alter_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.alter_suche.place(width=150, height=30, x=975, y=280)
            self.alter_suche.insert(0, '- Eingabe -')
            self.alter_suche.bind("<Button-1>", self.clear_entry)
            self.alter_suche.bind('<Return>', self.alter_suchen)

            label_email_suche = tk.Label(self.hauptframe, text='E-Mail:', font=('arial',12), anchor='w')
            label_email_suche.place(width=100, height=30, x=870, y=330)
            self.email_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.email_suche.place(width=150, height=30, x=975, y=330)
            self.email_suche.insert(0, '- Eingabe -')
            self.email_suche.bind("<Button-1>", self.clear_entry)
            self.email_suche.bind('<Return>', self.email_suchen)

            label_strasse_suche = tk.Label(self.hauptframe, text='Straße:', font=('arial',12), anchor='w')
            label_strasse_suche.place(width=100, height=30, x=870, y=380)
            self.strasse_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.strasse_suche.place(width=150, height=30, x=975, y=380)
            self.strasse_suche.insert(0, '- Eingabe -')
            self.strasse_suche.bind("<Button-1>", self.clear_entry)
            self.strasse_suche.bind('<Return>', self.strasse_suchen)

            label_hausnummer_suche = tk.Label(self.hauptframe, text='Hausnummer:', font=('arial',12), anchor='w')
            label_hausnummer_suche.place(width=100, height=30, x=870, y=430)
            self.hausnummer_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.hausnummer_suche.place(width=150, height=30, x=975, y=430)
            self.hausnummer_suche.insert(0, '- Eingabe -')
            self.hausnummer_suche.bind("<Button-1>", self.clear_entry)
            self.hausnummer_suche.bind('<Return>', self.hausnummer_suchen)

            label_postleitzahl_suche = tk.Label(self.hauptframe, text='Postleitzahl:', font=('arial',12), anchor='w')
            label_postleitzahl_suche.place(width=100, height=30, x=870, y=480)
            self.postleitzahl_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.postleitzahl_suche.place(width=150, height=30, x=975, y=480)
            self.postleitzahl_suche.insert(0, '- Eingabe -')
            self.postleitzahl_suche.bind("<Button-1>", self.clear_entry)
            self.postleitzahl_suche.bind('<Return>', self.postleitzahl_suchen)

            label_stadt_suche = tk.Label(self.hauptframe, text='Stadt:', font=('arial',12), anchor='w')
            label_stadt_suche.place(width=100, height=30, x=870, y=530)
            self.stadt_suche = tk.Entry(self.hauptframe, font=('arial', 12))
            self.stadt_suche.place(width=150, height=30, x=975, y=530)
            self.stadt_suche.insert(0, '- Eingabe -')
            self.stadt_suche.bind("<Button-1>", self.clear_entry)
            self.stadt_suche.bind('<Return>', self.stadt_suchen) 

    # Programm - Ende
    def programm_ende(self):
        antwort = messagebox.askyesno("Programm schließen", "Möchten Sie speichern wenn das Programm schließt ?")
        
        # Überprüfe die Antwort des Benutzers
        if antwort:                
            datenbank_speichern() 
            root.quit()        
        else:
            root.quit()

    # Funktion zur Erstellung eines neuen Eintrags
    def erstellung_neuer_eintrag(self):

        # Funktion zur Schließung des Eintrag-Erstellen Frames
        def beenden():
            self.neuer_eintrag_frame.destroy()

        # Funktion zum Overlay für Nein-Option für Optionale-Einträge
        def beende_optionals():
            for widget in self.optionals_keys + self.optionals_values:
                widget.destroy()
            self.optionals_keys.clear()
            self.optionals_values.clear()
            destroyframe = tk.Frame(self.neuer_eintrag_frame)
            destroyframe.place(x=400, y=60, width=450, height=370)
        
        # Funktion zur Erweiterung der Optional-Abfrage
        def update_optionals():
            
            # Funktion zur Eingabe der Optionalen Angaben
            def eingabe_optionals():
                    try:
                        anzahl_optionals = int(eingabe_optionals_anzahl.get())
                    except:
                        messagebox.showerror('Fehler', 'Bitte nur Zahlen zwischen 1 - 4 eingeben !')
                    if anzahl_optionals <= 0 or anzahl_optionals > 4:
                        messagebox.showerror('Fehler', 'Bitte nur Zahlen zwischen 1 - 4 eingeben !')
                    else:
                        for anzahl in range(anzahl_optionals):

                            optionals_eingabe_key = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
                            optionals_eingabe_key.place(width=200, height=30, x=402, y= 60 + (anzahl + 1) * 70)
                            self.optionals_keys.append(optionals_eingabe_key)

                            optionals_eingabe_key_label = tk.Label(self.neuer_eintrag_frame, text=f"Key ( Hobbies, Telefon, etc )", font=('arial', 12), anchor='nw')
                            optionals_eingabe_key_label.place(width=200, height=55, x=400, y= 90 + (anzahl + 1) * 70)

                            optionals_eingabe_value = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
                            optionals_eingabe_value.place(width=200, height=30, x=622, y= 60 + (anzahl + 1) * 70)
                            self.optionals_values.append(optionals_eingabe_value)

                            optionals_eingabe_value_label = tk.Label(self.neuer_eintrag_frame, text=f"Value ( Schiwmmen, etc )", font=('arial', 12), anchor='nw')
                            optionals_eingabe_value_label.place(width=200, height=55, x=620, y= 90 + (anzahl + 1) * 70)
          
            if optionals_var.get() == 'ja':
                label_optionals_anzahl = tk.Label(self.neuer_eintrag_frame, text=f"Anzahl optionale Eingaben:", font=('arial', 12), anchor='w')
                label_optionals_anzahl.place(height=30, x=400, y=60)
                eingabe_optionals_anzahl = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
                eingabe_optionals_anzahl.place(width=50, height=30, x=650, y=60)
                button_optionals_anzahl = tk.Button(self.neuer_eintrag_frame, text='Anzahl hinzufügen', font=('arial', 12), command=eingabe_optionals)
                button_optionals_anzahl.place(height=30, x=710, y=60)


        # GUI Anpassung
        self.neuer_eintrag_frame = tk.Frame(self.hauptframe)
        self.neuer_eintrag_frame.place(width=850, height=500, x=10, y=60)

        label_eingabe_vorname = tk.Label(self.neuer_eintrag_frame, text='Vorname', font=('arial',12), anchor='w')
        label_eingabe_vorname.place(width=100, height=30, x=50, y=20)
        self.eingabe_vorname = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_vorname.place(width=150, height=30, x=155, y=20)
        self.eingabe_vorname.insert(0, '- Eingabe -')
        self.eingabe_vorname.bind("<Button-1>", self.clear_entry)

        label_eingabe_nachname = tk.Label(self.neuer_eintrag_frame, text='Nachname', font=('arial',12), anchor='w')
        label_eingabe_nachname.place(width=100, height=30, x=50, y=70)
        self.eingabe_nachname = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_nachname.place(width=150, height=30, x=155, y=70)
        self.eingabe_nachname.insert(0, '- Eingabe -')
        self.eingabe_nachname.bind("<Button-1>", self.clear_entry)

        label_eingabe_alter = tk.Label(self.neuer_eintrag_frame, text='Alter', font=('arial',12), anchor='w')
        label_eingabe_alter.place(width=100, height=30, x=50, y=120)
        self.eingabe_alter = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_alter.place(width=150, height=30, x=155, y=120)
        self.eingabe_alter.insert(0, '- Eingabe -')
        self.eingabe_alter.bind("<Button-1>", self.clear_entry)

        label_eingabe_email = tk.Label(self.neuer_eintrag_frame, text='E-Mail', font=('arial',12), anchor='w')
        label_eingabe_email.place(width=100, height=30, x=50, y=170)
        self.eingabe_email = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_email.place(width=150, height=30, x=155, y=170)
        self.eingabe_email.insert(0, '- Eingabe -')
        self.eingabe_email.bind("<Button-1>", self.clear_entry)

        label_eingabe_strasse = tk.Label(self.neuer_eintrag_frame, text='Straße', font=('arial',12), anchor='w')
        label_eingabe_strasse.place(width=100, height=30, x=50, y=220)
        self.eingabe_strasse = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_strasse.place(width=150, height=30, x=155, y=220)
        self.eingabe_strasse.insert(0, '- Eingabe -')
        self.eingabe_strasse.bind("<Button-1>", self.clear_entry)

        label_eingabe_hausnummer = tk.Label(self.neuer_eintrag_frame, text='Hausnummer', font=('arial',12), anchor='w')
        label_eingabe_hausnummer.place(width=100, height=30, x=50, y=270)
        self.eingabe_hausnummer = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_hausnummer.place(width=150, height=30, x=155, y=270)
        self.eingabe_hausnummer.insert(0, '- Eingabe -')
        self.eingabe_hausnummer.bind("<Button-1>", self.clear_entry)

        label_eingabe_postleitzahl = tk.Label(self.neuer_eintrag_frame, text='Postleitzahl', font=('arial',12), anchor='w')
        label_eingabe_postleitzahl.place(width=100, height=30, x=50, y=320)
        self.eingabe_postleitzahl = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_postleitzahl.place(width=150, height=30, x=155, y=320)
        self.eingabe_postleitzahl.insert(0, '- Eingabe -')
        self.eingabe_postleitzahl.bind("<Button-1>", self.clear_entry)

        label_eingabe_stadt = tk.Label(self.neuer_eintrag_frame, text='Stadt', font=('arial',12), anchor='w')
        label_eingabe_stadt.place(width=100, height=30, x=50, y=370)
        self.eingabe_stadt = tk.Entry(self.neuer_eintrag_frame, font=('arial', 12))
        self.eingabe_stadt.place(width=150, height=30, x=155, y=370)
        self.eingabe_stadt.insert(0, '- Eingabe -')
        self.eingabe_stadt.bind("<Button-1>", self.clear_entry)

        label_optionals = tk.Label(self.neuer_eintrag_frame, text='Optionale Eingabe gewünscht ?', font=('arial',12), anchor='w')
        label_optionals.place(height=30, x=400, y=20)
        optionals_var = tk.StringVar(value="nein")
        ja_button = ttk.Radiobutton(self.neuer_eintrag_frame, text="Ja", variable=optionals_var, value="ja", command=update_optionals)
        ja_button.place(height=30, x=650, y=20)
        nein_button = ttk.Radiobutton(self.neuer_eintrag_frame, text="Nein", variable=optionals_var, value="nein", command=beende_optionals)
        nein_button.place(height=30, x=700, y=20)

        eintrag_erstellen_button= tk.Button(self.neuer_eintrag_frame, text='Eintrag erstellen', font=('arial', 16), command=self.neuer_eintrag_zur_datenbank)
        eintrag_erstellen_button.place(width=200, x=400, y=430)
        beenden_button = tk.Button(self.neuer_eintrag_frame, text='Schließen', font=('arial', 16), command=beenden)
        beenden_button.place(width=200, x=620, y=430)

        # Listen zur aufnahme der Optionalen Abfragen
        self.optionals_keys = []
        self.optionals_values = [] 

    # Funktion zur Sammlung der Eingegeben Daten und Weiterleitung an die Erstellung des Eintrags
    def neuer_eintrag_zur_datenbank(self):
        vorname = self.eingabe_vorname.get().capitalize()
        nachname = self.eingabe_nachname.get().capitalize()
        try:
            alter = int(self.eingabe_alter.get())
        except:
            messagebox.showerror('Fehler', 'Bitte nur Zahlen im Alter eingeben')
        email = self.eingabe_email.get()
        strasse = self.eingabe_strasse.get()
        hausnummer = self.eingabe_hausnummer.get()
        try:
            postleitzahl = int(self.eingabe_postleitzahl.get())
        except:
            messagebox.showerror('Fehler', 'Bitte nur Zahlen iin Postleitzahl eingeben')
        stadt = self.eingabe_stadt.get()
        optionals = {}
        for key, value in zip(self.optionals_keys, self.optionals_values):
            key = key.get()
            value = value.get()
            if key and value:
                optionals[key] = value
        # Leerung der Listen nach Verarbeitung
        self.optionals_keys = []
        self.optionals_values = []
        # Weiterleitung der Daten
        self.neuer_eintrag_frame.destroy()
        eintrag_erstellen(vorname, nachname, alter, email, strasse, hausnummer, postleitzahl, stadt, **optionals)

    # Funktionen zu einzelnen Such-Abfragen für alle Standard Eingaben
    def id_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        try:
            id = int(self.id_suche.get())
            self.id_suche.delete(0, tk.END)        
            index = Register_ID.ids.index(id)
            message = (
            f'ID: {Register_ID.ids[index]}\n'
            f'Vorname: {Register_ID.first_names[index]}\n'
            f'Nachname: {Register_ID.last_names[index]}\n'
            f'Alter: {Register_ID.ages[index]}\n'
            f'Email: {Register_ID.emails[index]}\n'
            f'Straße: {Register_ID.streets[index]} {Register_ID.house_numbers[index]}\n'
            f'PLZ / Ort: {Register_ID.post_codes[index]} {Register_ID.citys[index]}\n'
            )
            self.text_widget.insert('1.0', message)
            person = Register_ID.json_pack.get(id)
            if person:
                if person['optional']:
                    self.text_widget.insert(tk.END, f'\nOptionale Felder für {person['vorname']} {person['nachname']}:\n')
                    for opt_key, opt_value in person['optional'].items():
                        self.text_widget.insert(tk.END, f'{opt_key}: {opt_value}')
                else:
                    self.text_widget.insert(tk.END, f"\nKeine optionalen Felder für {person['vorname']} {person['nachname']}.")
        except:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {id} <- in -IDs- gefunden...')

    def vorname_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        suche = self.vorname_suche.get().capitalize()
        self.vorname_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.first_names) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Vornamen- gefunden...')

    def nachname_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        suche = self.nachname_suche.get().capitalize()
        self.nachname_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.last_names) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Nachnamen- gefunden...')    

    def alter_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        try:
            suche = int(self.alter_suche.get())
            self.alter_suche.delete(0, tk.END)
            index = [i for i, value in enumerate(Register_ID.ages) if value == suche]
            for i in index:
                self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
            if len(index) < 1:
                self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Alter- gefunden...')
        except:
            messagebox.showerror('Fehler', 'Bitte nur Zahlen im Alter angeben')

    def email_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        suche = self.email_suche.get()
        self.email_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.emails) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -E-Mail- gefunden...')

    def strasse_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        suche = self.strasse_suche.get()
        self.strasse_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.streets) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Straße- gefunden...')

    def hausnummer_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        suche = self.hausnummer_suche.get()
        self.hausnummer_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.house_numbers) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Hausnummer- gefunden...')

    def postleitzahl_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        try:
            suche = int(self.postleitzahl_suche.get())
        except ValueError:
            messagebox.showerror('Fehler', 'Bitte nur zahlen in der Postleitzahl angeben')
        self.postleitzahl_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.post_codes) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Postleitzahl- gefunden...')

    def stadt_suchen(self, event):
        self.text_widget.delete('1.0', tk.END)
        self.text_widget = tk.Text(self.hauptframe, wrap="word", font=('arial', 12))
        self.text_widget.place(width=850, height=500, x=10, y=60)
        suche = self.stadt_suche.get()
        self.stadt_suche.delete(0, tk.END)
        index = [i for i, value in enumerate(Register_ID.citys) if value == suche]
        for i in index:
            self.text_widget.insert('1.0', f'ID: {Register_ID.ids[i]} - {Register_ID.first_names[i]} {Register_ID.last_names[i]}, {Register_ID.ages[i]} Jahre alt, {Register_ID.emails[i]}, {Register_ID.streets[i]}, {Register_ID.post_codes[i]} {Register_ID.citys[i]}\n')
        if len(index) < 1:
            self.text_widget.insert('1.0', f'Keine Einträge zu der Eingabe -> {suche} <- in -Stadt- gefunden...')
    
    # Funktion zur Sammlung der Einträge aus eintraege_bearbeiten() und Verabreitung
    def bearbeiteter_eintrag_zur_datenbank(self):
        suche = ''
        try:
            suche = int(self.eingabe_label_id_suche.get())        
        except:
            messagebox.showerror('Fehler', 'Bitte nur Zahlen in der ID - Suche eingeben !')
        vorname = self.eingabe_vorname.get()        
        nachname = self.eingabe_nachname.get()
        alter = self.eingabe_alter.get()
        email = self.eingabe_email.get()
        strasse = self.eingabe_strasse.get()
        hausnummer = self.eingabe_hausnummer.get()
        postleitzahl = self.eingabe_postleitzahl.get()
        stadt = self.eingabe_stadt.get()
        if suche in Register_ID.ids:
            index = Register_ID.ids.index(suche)            
            if len(vorname) > 0:
                Register_ID.first_names[index] = vorname
                Register_ID.json_pack[suche]['vorname'] = vorname
            else:
                pass
            if len(nachname) > 0:
                Register_ID.last_names[index] = nachname
                Register_ID.json_pack[suche]['nachname'] = nachname
            else:
                pass
            if len(alter) > 0:
                try:
                    alter = int(alter)
                except:
                    messagebox.showerror('Fehler', 'Bitte nur Zahlen im Altern eingeben !')
                else:
                    Register_ID.ages[index] = alter
                    Register_ID.json_pack[suche]['alter'] = alter
            else:
                pass
            if len(email) > 0:                
                Register_ID.emails[index] = email
                Register_ID.json_pack[suche]['email'] = email
            else:
                pass
            if len(strasse) > 0:                
                Register_ID.streets[index] = strasse
                Register_ID.json_pack[suche]['strasse'] = strasse
            else:
                pass
            if len(hausnummer) > 0:                
                Register_ID.house_numbers[index] = hausnummer
                Register_ID.json_pack[suche]['hausnummer'] = hausnummer
            else:
                pass
            if len(postleitzahl) > 0:
                try:
                    postleitzahl = int(postleitzahl)                    
                except:
                    messagebox.showerror('Fehler', 'Bitte nur Zahlen in der Postleitzahl angeben !')
                else:    
                    Register_ID.post_codes[index] = postleitzahl
                    Register_ID.json_pack[suche]['plz'] = postleitzahl
            else:
                pass
            if len(stadt) > 0:                
                Register_ID.citys[index] = stadt
                Register_ID.json_pack[suche]['stadt'] = stadt
            else:
                pass
            self.eintrag_bearbeiten_frame.destroy()
            message = (
            f'\n### Datensatz wird bearbeitet ###\n\n'
            f'ID: {suche}\n'
            f'Vorname: {vorname}\n'
            f'Nachname: {nachname}\n'
            f'Alter: {alter}\n'
            f'Email: {email}\n'
            f'Strasse: {strasse} {hausnummer}\n'
            f'PLZ / Ort: {postleitzahl} {stadt}\n'
            )         
            message += '\n### Datensatz erfolgreich bearbeitet ###\n'
            messagebox.showinfo("Bestätigung Eintrag bearbeitet", message)
        
    
    # Funktion zur Eingabe der Bearbeitung der Einträge
    def eintraege_bearbeiten(self):

        self.eintrag_bearbeiten_frame = tk.Frame(self.hauptframe)
        self.eintrag_bearbeiten_frame.place(width=850, height=500, x=10, y=60)

        # Funktion zum Beenden
        def beenden():
            self.eintrag_bearbeiten_frame.destroy()

        # Funktion zur Suche der ID und Anzeige
        def id_suchen():
            try:
                suche = int(self.eingabe_label_id_suche.get())
            except:
                messagebox.showerror('Fehler', 'Bitte nur Zahlen eingeben in der ID-Suche')
            if suche in Register_ID.ids:
                index = Register_ID.ids.index(suche)
                message = (
                f'ID: {Register_ID.ids[index]}\n'
                f'Vorname: {Register_ID.first_names[index]}\n'
                f'Nachname: {Register_ID.last_names[index]}\n'
                f'Alter: {Register_ID.ages[index]}\n'
                f'Email: {Register_ID.emails[index]}\n'
                f'Straße: {Register_ID.streets[index]} {Register_ID.house_numbers[index]}\n'
                f'PLZ / Ort: {Register_ID.post_codes[index]} {Register_ID.citys[index]}\n'
                )
                id_label = tk.Label(self.eintrag_bearbeiten_frame, text=message, font=('arial',16), anchor='w', justify='left')
                id_label.place(x=400, y=80)

                label_eingabe_vorname = tk.Label(self.eintrag_bearbeiten_frame, text='Vorname', font=('arial',12), anchor='w')
                label_eingabe_vorname.place(width=100, height=30, x=50, y=20)
                self.eingabe_vorname = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_vorname.place(width=150, height=30, x=155, y=20)

                label_eingabe_nachname = tk.Label(self.eintrag_bearbeiten_frame, text='Nachname', font=('arial',12), anchor='w')
                label_eingabe_nachname.place(width=100, height=30, x=50, y=70)
                self.eingabe_nachname = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_nachname.place(width=150, height=30, x=155, y=70)

                label_eingabe_alter = tk.Label(self.eintrag_bearbeiten_frame, text='Alter', font=('arial',12), anchor='w')
                label_eingabe_alter.place(width=100, height=30, x=50, y=120)
                self.eingabe_alter = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_alter.place(width=150, height=30, x=155, y=120)

                label_eingabe_email = tk.Label(self.eintrag_bearbeiten_frame, text='E-Mail', font=('arial',12), anchor='w')
                label_eingabe_email.place(width=100, height=30, x=50, y=170)
                self.eingabe_email = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_email.place(width=150, height=30, x=155, y=170)

                label_eingabe_strasse = tk.Label(self.eintrag_bearbeiten_frame, text='Straße', font=('arial',12), anchor='w')
                label_eingabe_strasse.place(width=100, height=30, x=50, y=220)
                self.eingabe_strasse = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_strasse.place(width=150, height=30, x=155, y=220)

                label_eingabe_hausnummer = tk.Label(self.eintrag_bearbeiten_frame, text='Hausnummer', font=('arial',12), anchor='w')
                label_eingabe_hausnummer.place(width=100, height=30, x=50, y=270)
                self.eingabe_hausnummer = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_hausnummer.place(width=150, height=30, x=155, y=270)

                label_eingabe_postleitzahl = tk.Label(self.eintrag_bearbeiten_frame, text='Postleitzahl', font=('arial',12), anchor='w')
                label_eingabe_postleitzahl.place(width=100, height=30, x=50, y=320)
                self.eingabe_postleitzahl = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_postleitzahl.place(width=150, height=30, x=155, y=320)

                label_eingabe_stadt = tk.Label(self.eintrag_bearbeiten_frame, text='Stadt', font=('arial',12), anchor='w')
                label_eingabe_stadt.place(width=100, height=30, x=50, y=370)
                self.eingabe_stadt = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
                self.eingabe_stadt.place(width=150, height=30, x=155, y=370)

                eintrag_erstellen_button= tk.Button(self.eintrag_bearbeiten_frame, text='Eintrag bearbeiten', font=('arial', 16), command=self.bearbeiteter_eintrag_zur_datenbank)
                eintrag_erstellen_button.place(width=200, x=400, y=430)
            else:
                messagebox.showerror('Fehler', f'ID: {suche} nicht gefunden !')
            

        beenden_button = tk.Button(self.eintrag_bearbeiten_frame, text='Schließen', font=('arial', 16), command=beenden)
        beenden_button.place(width=200, x=620, y=430)

        label_id_suche = tk.Label(self.eintrag_bearbeiten_frame, text='Bitte zu bearbeitende ID eingeben:', font=('arial',12), anchor='w')
        label_id_suche.place(height=30, x=400, y=20)
        self.eingabe_label_id_suche = tk.Entry(self.eintrag_bearbeiten_frame, font=('arial', 12))
        self.eingabe_label_id_suche.place(width=50, height=30, x=650, y=20)
        button_label_id_suche = tk.Button(self.eintrag_bearbeiten_frame, text='ID suchen...', font=('arial', 12), command=id_suchen)
        button_label_id_suche.place(height=30, x=710, y=20)

    # Funktion zum Abfragen der ID um Einträge zu löschen
    def eintrag_loeschen(self):
        
        # Funktion zum beenden
        def beenden():
            self.eintrag_loeschen_frame.destroy()

        # Funktion zur Abfrage des Löschvorgangs
        def eintrag_loeschen_abfrage():
            antwort = messagebox.askyesno("Eintrag löschen", "Sind Sie sicher, dass Sie diesen Eintrag unwiderruflich löschen möchten?")
        
            # Überprüfe die Antwort des Benutzers
            if antwort:                
                Register_ID.remove_id(int(self.eingabe_label_id_suche.get()))
                messagebox.showinfo('Eintrag wird gelöscht', 'Eintrag wurde gelöscht !') 
                self.eintrag_loeschen_frame.destroy()               
            else:
                messagebox.showinfo('Eintrag wurde nicht gelöscht', 'Löschvorgang abgebrochen !')

        # Funktion um ID zu suchen
        def id_suchen():
            try:
                suche = int(self.eingabe_label_id_suche.get())
            except:
                messagebox.showerror('Fehler', 'Bitte nur Zahlen eingeben in der ID-Suche')
            if suche in Register_ID.ids:
                index = Register_ID.ids.index(suche)
                message = (
                f'ID: {Register_ID.ids[index]}\n'
                f'Vorname: {Register_ID.first_names[index]}\n'
                f'Nachname: {Register_ID.last_names[index]}\n'
                f'Alter: {Register_ID.ages[index]}\n'
                f'Email: {Register_ID.emails[index]}\n'
                f'Straße: {Register_ID.streets[index]} {Register_ID.house_numbers[index]}\n'
                f'PLZ / Ort: {Register_ID.post_codes[index]} {Register_ID.citys[index]}\n'
                )
            else:
                message = f'ID: {suche} nicht vorhanden'
            id_label = tk.Label(self.eintrag_loeschen_frame, text=message, font=('arial',16), anchor='w', justify='left')
            id_label.place(x=400, y=80)

            eintrag_erstellen_button= tk.Button(self.eintrag_loeschen_frame, text='Eintrag löschen', font=('arial', 16), command=eintrag_loeschen_abfrage)
            eintrag_erstellen_button.place(width=200, x=400, y=430)

        self.eintrag_loeschen_frame = tk.Frame(self.hauptframe)
        self.eintrag_loeschen_frame.place(width=850, height=500, x=10, y=60)

        label_id_suche = tk.Label(self.eintrag_loeschen_frame, text='Bitte zu löschende ID eingeben:', font=('arial',12), anchor='w')
        label_id_suche.place(height=30, x=400, y=20)
        self.eingabe_label_id_suche = tk.Entry(self.eintrag_loeschen_frame, font=('arial', 12))
        self.eingabe_label_id_suche.place(width=50, height=30, x=650, y=20)
        button_label_id_suche = tk.Button(self.eintrag_loeschen_frame, text='ID suchen...', font=('arial', 12), command=id_suchen) 
        button_label_id_suche.place(height=30, x=710, y=20)

        beenden_button = tk.Button(self.eintrag_loeschen_frame, text='Schließen', font=('arial', 16), command=beenden)
        beenden_button.place(width=200, x=620, y=430)

    # Funktion zur leerung eines Entry-Widget
    def clear_entry(self, event):
        event.widget.delete(0, "end")

        
#%% Startfenster

root = tk.Tk()
root.geometry('1200x800')
root.resizable(False, False)

# Hintergrund - Bild setzen
hintergrund = tk.Canvas(root, width=1200, height=800)
hintergrund.pack(fill="both", expand=True)
bild = Image.open('background_main2.jpg') 
bild = bild.resize((1200, 800))
background_image = ImageTk.PhotoImage(bild)
hintergrund.create_image(0, 0, image=background_image, anchor='nw')

# Hauptframe setzen
startframe = tk.LabelFrame(hintergrund, bg="lightgrey")
startframe_width = 1145
startframe_height = 572.5
startframe.place(x = 27.5, y = 200, width = startframe_width, height = startframe_height)

# Erstellung StringVars
laden_der_datenbank = tk.StringVar()
laden_der_datenbank.set(value=laden_der_datenbank_inhalt)
on_klick = tk.StringVar()
table1 = tk.StringVar()
table2 = tk.StringVar()
table3 = tk.StringVar()
table4 = tk.StringVar()

# Erstellung Überschrift Startbildschirm
start_label = ttk.Label(startframe, text='Personen - Datenbank', font=('arial', 40),  padding= 20)
start_label.configure(background='lightgrey')
start_label.pack()

# Label zur Verarbeitung ob Datenbank gefunden oder nicht
start_label_datenbank = ttk.Label(startframe, textvariable=laden_der_datenbank, font=('arial', 24),  padding= 20)
start_label_datenbank.configure(background='lightgrey')
start_label_datenbank.pack()

# Erstellung der Menüleisten
menubar = tk.Menu(root)
root.config(menu=menubar)

# Menü 1

menue1 = tk.Menu(menubar, tearoff=0, font=('arial', 18))
menubar.add_cascade(label='Start', menu=menue1)
menue1.add_command(label='Datenbank laden', command= lambda: datenbank_starten(hintergrund))
menue1.add_command(label='Datenbank speichern', command=datenbank_speichern)

root.mainloop()
