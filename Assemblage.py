from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector
#import select
import cv2
import io
#import numpy as np
import face_recognition
import datetime

# Déclaration de la variable globale pour stocker la référence de l'image
#================================================= App =====================================
video_capture=None
def programe(ids,window):
    global video_capture
    video_capture=cv2.VideoCapture(0)    
    wbcwindow=Toplevel(window)
    wbcwindow.geometry('1119x900')
    wbcwindow.state('zoomed')
    #wbcwindow.configure(bg="#1E202D")
    wbcwindow.resizable(0,0)  
    background=Image.open('images/Screen3png.png')
    backgroundTk=ImageTk.PhotoImage(background)
    labelbg=Label(wbcwindow,image=backgroundTk)
    labelbg.pack()
    frameapp=Frame(wbcwindow,bg='#FFFFFF',width=1000,height=480)
    frameapp.place(x=250,y=100)
    canvaswbc=Label(frameapp,width=550,height=474)
    canvaswbc.place(x=0,y=0)
    #===================== Frame Carte =========================================
    framecarte=Frame(frameapp,width=360,height=200)
    framecarte.place(x=600,y=130)
    frameimg=Label(framecarte)
    frameimg.place(x=20,y=60)
    nameframe=Label(framecarte)
    nameframe.place(x=155,y=60)
    lnameframe=Label(framecarte)
    lnameframe.place(x=155,y=94)
    cneframe=Label(framecarte)
    cneframe.place(x=155,y=130)
    datenframe=Label(framecarte)
    datenframe.place(x=155,y=160)
    nameframevalue=Label(framecarte)
    nameframevalue.place(x=235,y=60)
    lnameframevalue=Label(framecarte)
    lnameframevalue.place(x=235,y=94)
    cneframevalue=Label(framecarte)
    cneframevalue.place(x=235,y=130)
    datenframevalue=Label(framecarte)
    datenframevalue.place(x=235,y=160)
    nameframe.configure(text="Nom :",font=('yu gothic ui',13,'bold'), foreground='#014C83')
    lnameframe.configure(text="Prenom :",font=('yu gothic ui',13,'bold'), foreground='#014C83')
    cneframe.configure(text="CNE :",font=('yu gothic ui ',13,'bold'), foreground='#014C83')
    datenframe.configure(text="Date :",font=('yu gothic ui ',13,'bold'), foreground='#014C83')
    #=============== Message Autorisation ==========================================
    amessageframe=Label(frameapp,bg='#FFFFFF',fg='green')
    amessageframe.place(x=615,y=343)
    aiconframe=Label(frameapp,bg="#FFFFFF")
    aiconframe.place(x=734,y=375)
   
    #================= load autorisation images =======================
    successimg=Image.open("images/success1.png")
    successimgtk=ImageTk.PhotoImage(successimg)
    failureimg=Image.open("images/failure1.png")
    failureimgtk=ImageTk.PhotoImage(failureimg)
    nonimg=Image.open("images/non.png").resize((120,120), Image.BICUBIC)
    nonimgtk=ImageTk.PhotoImage(nonimg)
    #========================================= prog =================================
    def resize_image(image, new_width, new_height):
        return image.resize((new_width, new_height), Image.BICUBIC)

    """# Connexion à la base de données MySQL
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ensajdatabase"
    )
    cursor = conn.cursor()
    id_sale=ids
    # Chargement des visages connus depuis la base de données
    cursor.execute("select nom,image,prenom,cne FROM etudiant where cne in (select cne from examen where idSalle=%s) ",(id_sale,))
    rows = cursor.fetchall()
    noms_connu = []
    encodages_connu = []
    image_connu=[]"""

    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ensajdatabase"
    )
    cursor = conn.cursor()
    id_sale=ids
    # Changement de la requette 
    cursor.execute("SELECT nom, image, prenom ,cne FROM etudiant WHERE cne IN (SELECT cneEtudiant FROM examen WHERE idSalle=%s AND CURTIME() BETWEEN heureDebut AND heureFin AND CURDATE() = dateExamen)", (id_sale,))
    rows = cursor.fetchall()
    noms_connu = []
    encodages_connu = []
    image_connu=[]
    prenom_connu=[]
    cne_connu=[]


    for row in rows:
        noms_connu.append(row[0])
        image_data = row[1]
        image = face_recognition.load_image_file(io.BytesIO(image_data))
        imag=Image.open(io.BytesIO(image_data))
        resizeimg=resize_image(imag,120,120)
        image_connu.append(resizeimg)
        prenom_connu.append(row[2])
        cne_connu.append(row[3])  
    
        # Obtenir les encodages de visage pour chaque visage dans l'image
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            encodages_connu.extend(encodings)

    conn.close()

    def webcam():
        # Capture vidéo depuis la webcam
        global video_capture
        
        # Capture de frame par frame
        ret, frame = video_capture.read()
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Boucle sur chaque visage détecté
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Comparaison du visage détecté avec les visages connus
            correspondances = face_recognition.compare_faces(encodages_connu, face_encoding,tolerance=0.6)
            print(correspondances)
            nom_trouve = "N'est pas autoriser"

            # Vérification s'il y a une correspondance
            if True in correspondances:
                index_correspondance = correspondances.index(True)
                nom_trouve = noms_connu[index_correspondance]
                img_trouve=image_connu[index_correspondance]
                prenom_trouve=prenom_connu[index_correspondance]
                cne_trouve=cne_connu[index_correspondance]
                
                img_trouvetk=ImageTk.PhotoImage(img_trouve)
                frameimg.configure(image=img_trouvetk)
                frameimg.image=img_trouvetk
                nameframevalue.configure(text=nom_trouve,font=('yu gothic ui',13,'bold'))
                
                lnameframevalue.configure(text=prenom_trouve,font=('yu gothic ui',13,'bold'))
                cneframevalue.configure(text=cne_trouve,font=('yu gothic ui ',13,'bold'))
                datenframevalue.configure(text=datetime.date.today(),font=('yu gothic ui ',13,'bold'))
                #=============== Message Autorisation ==========================================
                amessageframe.configure(text="Vous etes autoriser dans cette salle",font=('yu gothic ui',16,'bold'),fg='green')
                aiconframe.configure(image=successimgtk)
                aiconframe.imgtk=successimgtk
            else:
                nameframevalue.configure(text=" ",font=('yu gothic ui',13,'bold'))
                lnameframevalue.configure(text="",font=('yu gothic ui',13,'bold'))
                cneframevalue.configure(text="",font=('yu gothic ui ',13,'bold'))
                datenframevalue.configure(text=datetime.date.today(),font=('yu gothic ui ',13,'bold'))
                nameframevalue.configure(text=" ",font=('yu gothic ui',13,'bold'))
                #=================== Message Autrisation =============================
                amessageframe.configure(text="Vous n'etes pas autoriser dans cette salle ",font=('yu gothic ui',15,'bold'),fg='red')
                aiconframe.configure(image=failureimgtk)
                aiconframe.imgtk=failureimgtk
                frameimg.configure(image=nonimgtk)
                
            # Affichage du rectangle autour du visage et du nom trouvé
            cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 0), 2)
            cv2.putText(frame, nom_trouve, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    
        


        
        #======================================= webcam ============================
        frame_atraite=frame
        img_=cv2.cvtColor(frame_atraite,cv2.COLOR_BGR2RGB)
        _imge=Image.fromarray(img_)
        _imgtk=ImageTk.PhotoImage(image=_imge)
        canvaswbc.configure(image=_imgtk)
        canvaswbc.imgtk=_imgtk
        canvaswbc.after(10,webcam)

        # Attendre l'appui sur la touche 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
    # Libération de la capture vidéo et fermeture de la fenêtre
            video_capture.release()
            cv2.destroyAllWindows()

    webcam()
    wbcwindow.mainloop()

    


def interface2(window) :
    conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="ensajdatabase"
)
    cursor = conn.cursor()
    cursor.execute("SELECT nomSalle, idSalle FROM salle ")
    resultats=cursor.fetchall()
    choices=[]
    id_sales=[]
    for result in resultats:
        choices.append(result[0])
        id_sales.append(result[1])

    conn.close()

    def id_salle():
        choi=combobox.get()
        return id_sales[choices.index(choi)]
    
    #==================================================================================
    window3=Toplevel(window)
    window3.geometry('1119x716')
    window3.state('zoomed')
    window3.configure(bg='#FFFFFF')
    window3.resizable(0,0)
    bg_image1=ImageTk.PhotoImage(Image.open('images/back.png'))
    #bg_image=Label(window3,image=bg_image1)
    #bg_image.image=bg_image1
    #bg_image.pack()

#===================LOGOS============================
    """#Ajouter logo de UCD :
    logoUCD = Image.open("images/UCDlogo.jpeg")
    logoUCD =logoUCD .resize((500,150),Image.LANCZOS)
    logoUCDTK  =ImageTk.PhotoImage(logoUCD )
    f_lbl =Label(window3 , image=logoUCDTK )
    f_lbl.place(x=0 ,y=0 , width=500 , height=150)

    #Ajouter image RF :
    imgRF = Image.open("images/rfimg.jpg")
    imgRF  =imgRF.resize((650,150),Image.LANCZOS)
    imgRFtK  =ImageTk.PhotoImage(imgRF  )
    
    f_lbl =Label(window3 , image=imgRFtK )
    f_lbl.place(x=500 ,y=0 , width=650 , height=150)


    #Ajouter logo de ENSAJ :
    logoEnsaj = Image.open("images/ensajLogo.png")
    logoEnsaj =logoEnsaj .resize((450,150),Image.LANCZOS)
    logoEnsajTK =ImageTk.PhotoImage(logoEnsaj )
    
    f_lbl =Label(window3 , image=logoEnsajTK)
    f_lbl.place(x=1050 ,y=0 , width=500 , height=150)"""

    logoUCD = Image.open("images/logogeneral.jpeg")
    logoUCD =logoUCD.resize((1000,150),Image.LANCZOS)
    logoUCDTK  =ImageTk.PhotoImage(logoUCD )
    f_lbl =Label(window3 , image=logoUCDTK )
    f_lbl.place(x=300 ,y=0 , width=1000 , height=150)


    #=================== Frame root ============================
    sframe=Frame(window3,width=1000,height=500,bg='#000000' , bd=3)
    sframe.place(x=300, y=200)
    #============= side image ======================
    side_image = Image.open('images/sideImg.jpeg').resize((600, 520), Image.LANCZOS)
    side_image=ImageTk.PhotoImage(side_image)
    label_image=Label(sframe,image=side_image, bg='#28282B')
    label_image.image=side_image
    label_image.place(x=0,y=0)
    #=============== side frame =========================
    sideframe=Frame(sframe,bg='#FFFFFF',width=500,height=500)
    sideframe.place(x=600,y=0)
    #================== welcome  text ============================
    textlabel="Explorez et choisissez \nvotre salle de manière \nconfortable !"
    txtlabel=Label(sideframe,text=textlabel,font=('Helvetica', 20, 'bold'),fg='#072783',bg='#FFFFFF')
    txtlabel.place( x=30, y=120)
    #======================== selection =========================
    # Créer une combobox
    selected_choice = StringVar()
    combobox = Combobox(sideframe, values=choices, textvariable=selected_choice,width=40)
    
    combobox.place(x=70,y=250)

    # Sélectionner la première option par défaut
    selected_choice.set(choices[0])
    #=========================== Button valider image ======================
    img_button=ImageTk.PhotoImage(Image.open('images/btnValider.png').resize((250, 100), Image.LANCZOS))    
    label_button=Label(sideframe,image=img_button,bg='#FFFFFF')
    label_button.image=img_button
    label_button.place(x=50,y=320)
    #============================= valider button ==========================

    # Dans la fonction interface2
    btnvalider = Button(sideframe, text="Valider", bd=0, font=('yu gothic ui ', 17, 'bold'), fg='white', width=10, height=2, bg='#004AAD', activebackground='#004AAD', command=lambda: programe(id_salle(),window))
    btnvalider.place(x=80,y=339)
    

    window3.mainloop()

    #========================================        function id salle         =======================================



def firstInterfac():
    window = Tk()
    window.geometry('1166x716')
    window.state('zoomed')
    window.resizable(0, 0)
    
    # Chargement de l'image de fond
    bg_img = Image.open('images/ensajbg.jpeg')
    photo = ImageTk.PhotoImage(bg_img)
    photo_panel = Label(window, image=photo)
    photo_panel.image = photo
    photo_panel.pack(fill='both', expand='yes')

    # Définition de la fonction pour la gestion du focus
    def show_cursor_us(event):
        champEntrer.focus_set()

    def show_cursor_ps(event):
        champEntrerPasswd.focus_set()


       



    # Création du cadre de connexion
    log_frame = Frame(window, bg='#CEF5FE', width=950, height=600 ,bd=2, relief='solid')
    log_frame.place(x=300, y=150)
    txt = 'Bienvenue Professeur '
    heading_label = Label(log_frame, text=txt, font=('arial', 25, 'bold'), bg='#CEF5FE', fg='#039BD8')
    heading_label.place(x=330, y=25)

    # Left side image frame
    left_side_img = Image.open('images/last.png')
    side_photo = ImageTk.PhotoImage(left_side_img)
    side_img_label = Label(log_frame, image=side_photo, bg='#CEF5FE')
    side_img_label.image = side_photo
    side_img_label.place(x=20, y=65, width=400, height=500)

    # Sign up image frame
    signUpimg = Image.open('images/hyy.png')
    photo = ImageTk.PhotoImage(signUpimg)
    signUpimg_frame = Label(log_frame, image=photo, bg='#CEF5FE')
    signUpimg_frame.image = photo
    signUpimg_frame.place(x=550, y=80)

    # Login frame
    login_frame = Label(log_frame, text='Se connecter ', fg='#143573', bg='#CEF5FE',
                                font=('yu gothic ui ', 24, 'bold'))
    login_frame.place(x=540, y=200)

    # Nom d'utilisateur frame
    userName = Label(log_frame, text="Nom d'utilisateur ", bg='#CEF5FE',
                            font=('yu gothic ui ', 13, 'bold'), fg='#4e4f4d')
    userName.place(x=500, y=250)
    champEntrer = Entry(log_frame, relief=FLAT, fg='#000000', width=40,bg='#CEF5FE',font=('Arial', 13))
    champEntrer.configure(insertbackground="white")
    champEntrer.bind("<FocusIn>", show_cursor_us)
    champEntrer.place(x=540, y=280)

    # Ligne frame
    ligne_frame = Canvas(log_frame, width=320, height=2, highlightthickness=0, bg='#000000')
    ligne_frame.place(x=500, y=300)

    # Password frame
    passwd_frame = Label(log_frame, text='Mot de passe ', font=('yu gothic ui', 13, 'bold'),
                                bg='#CEF5FE', fg='#4e4f4d')
    passwd_frame.place(x=500, y=330)
    champEntrerPasswd = Entry(log_frame, width=40, fg='#000000', relief=FLAT, show='*',bg='#CEF5FE',font=('Arial', 13))
    champEntrerPasswd.configure(insertbackground="white")
    champEntrerPasswd.bind("<FocusIn>", show_cursor_ps)
    champEntrerPasswd.place(x=540, y=360)
    lignePsswd = Canvas(log_frame, width=320, height=2, highlightthickness=0 , bg='#000000')
    lignePsswd.place(x=500, y=380)

    # Username icon
    iconimg = Image.open('images/username_icon.png')
    photo = ImageTk.PhotoImage(iconimg)
    usericon_frame = Label(log_frame, image=photo, bg='#CEF5FE')
    usericon_frame.image = photo
    usericon_frame.place(x=500, y=270)

    # Password icon
    passwdIcon = Image.open('images/password_icon.png')
    photo = ImageTk.PhotoImage(passwdIcon)
    passwdIcon_frame = Label(log_frame, image=photo, bg='#CEF5FE')
    passwdIcon_frame.image = photo
    passwdIcon_frame.place(x=500, y=353)

    # Validation button
    buttonImg = Image.open('images/btn1.png')
    photo = ImageTk.PhotoImage(buttonImg)
    buttonImg_frame = Label(log_frame, image=photo, bg='#CEF5FE', width=270)
    buttonImg_frame.image = photo
    buttonImg_frame.place(x=500, y=408)
    logButton = Button(log_frame, text='Se connecter ', font=('yu gothic ui ', 14, 'bold'),
                            bg='#3047ff', cursor='hand2', command=lambda: program(username=champEntrer.get(),passwd=champEntrerPasswd.get(),window=window),
                            activebackground='#3047ff', fg='white', width=19, bd=0)
    logButton.place(x=500, y=420)

    window.mainloop()   
 
# Fonction de programme pour la vérification de connexion
def program(username, passwd,window):
    # Connexion à la base de données MySQL
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="ensajdatabase"
    )
    cursor=conn.cursor()
    #ici j'ai change la reequette "username " a la place de nomUtlisateur et "password"
    cursor.execute("select username from compte where username=%s and password=%s",(username,passwd))
    resultat=cursor.fetchall()
    conn.close()
    if(len(resultat)==0):
        messagebox.showerror("connexion echoue ","nom d'utilisateur ou mot de passe incorrecte ")
    else:
        # Ouverture de la nouvelle fenêtre après connexion réussie
       interface2(window)

# Fonction pour ouvrir une nouvelle fenêtre

if __name__ == '__main__':
    firstInterfac()
