from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Style
import sqlite3

# --------FUNCIONES---------------------------------------------

def conexionBBDD():
    miConexion = sqlite3.connect('Personal')

    try:
        miCursor = miConexion.cursor()
        miCursor.execute("""
           CREATE TABLE DATOSPERSONAL (ID INTEGER PRIMARY KEY AUTOINCREMENT, APELLIDO VARCHAR(50),
           NOMBRE_PERSONAL VARCHAR (59),
           DNI INTEGER (8) UNIQUE)""")

        messagebox.showinfo("BBDD", "Base de datos creada con éxito")

    except:

        messagebox.showwarning("¡Aviso!", "La base de datos ya ha sido creada")


def salir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")

    if valor == "yes":
        root.destroy()

def acercaDe():
    messagebox.showinfo("Acerca de","   Creado por «Meco»\n\n"
                                           "   Version Python: '3.8.1'\n   Licencia libre  ")

def agregar():
    ventanaAgregar = Toplevel(root)
    ventanaAgregar.title("Agregar personal")
    ventanaAgregar.geometry("270x200+460+180")
    ventanaAgregar.resizable(0, 0)
    ventanaAgregar.transient(root)
    miFrameAgregar = Frame(ventanaAgregar)
    miFrameAgregar.pack()

    espacioLabel = Label(miFrameAgregar, text="")
    espacioLabel.grid(row=0, column=0, columnspan=2)
    nombreAddLabel = Label(miFrameAgregar, text="Nombre:")
    nombreAddLabel.grid(row=1, column=0, sticky="se", padx=5, pady=10)
    apellidoAddLabel = Label(miFrameAgregar, text="Apellido:")
    apellidoAddLabel.grid(row=2, column=0, sticky="se", padx=5, pady=10)
    dniAddLabel = Label(miFrameAgregar, text="DNI:")
    dniAddLabel.grid(row=3, column=0, sticky="se", padx=5, pady=10)

    miNombre = StringVar()
    miApellido = StringVar()
    miDni = StringVar()

    nombreAddEntry = Entry(miFrameAgregar, textvariable=miNombre)
    nombreAddEntry.grid(row=1, column=1, padx=5, pady=10, sticky="s")
    apellidoAddEntry = Entry(miFrameAgregar, textvariable=miApellido)
    apellidoAddEntry.grid(row=2, column=1, padx=5, pady=10, sticky="s")
    dniAddEntry = Entry(miFrameAgregar, textvariable=miDni)
    dniAddEntry.grid(row=3, column=1, padx=5, pady=10, sticky="s")

    def crear():
        miConexion = sqlite3.connect('Personal')
        miCursor = miConexion.cursor()
        datos = miApellido.get().upper(), miNombre.get().capitalize(), miDni.get()
        miCursor.execute("""INSERT INTO DATOSPERSONAL VALUES(NULL,?,?,?)""", (datos))

        miConexion.commit()

        # D.E.S changes. lol
        # Excecuting my new functions
        limpiar_tabla(tabla)  # LINE 1
        cargar_datos(miConexion, tabla)  # LINE 2

        messagebox.showinfo("BBDD", "Registrado con éxito")

    def cerrarAgregar():
        aceptarBoton = True

        if aceptarBoton == True:
            ventanaAgregar.destroy()

    aceptarBoton = Button(ventanaAgregar, text="Aceptar",
                          command=lambda: [cerrarAgregar(), crear()])
    aceptarBoton.place(x=100, y=160)
    cancelarBoton = Button(ventanaAgregar, text="Cancelar", command=cerrarAgregar)
    cancelarBoton.place(x=175, y=160)

    # D.E.S changes, lol,
    # Functions added to clear and load data from db
    def limpiar_tabla(tabla):
        """
       Clear the treeview widget.
       Delete all the entries.
       """
        children = tabla.get_children()
        if children:
            tabla.delete(*children)

    def cargar_datos(conexion, tabla):
        """
       Populates the treeivew with data from db.

       param: conexion  an sqlite3 connection object
       param: tabla     a treeivew widget object where data will be inserted/displayed
       """
        try:
            cursor = conexion.cursor()
            datos = cursor.execute("""SELECT * FROM DATOSPERSONAL""")
            for entrada in datos.fetchall():
                tabla.insert('', END, values=entrada)

        except Exception as e:
            print(e)

def actualizar():
    conexion = sqlite3.connect('Personal')
    cursor = conexion.cursor()
    datos1 = cursor.execute("""SELECT * FROM DATOSPERSONAL""")

    children = tabla.get_children()
    if children:
        tabla.delete(*children)

    for usuario in datos1.fetchall():
        tabla.insert('', END, values=usuario)


def editar():

    ventanaEditar=Toplevel(root)
    ventanaEditar.title("Editar Personal")
    ventanaEditar.geometry("270x215+460+180")
    ventanaEditar.resizable(0, 0)
    ventanaEditar.transient(root)
    miFrameEditar=Frame(ventanaEditar)
    miFrameEditar.pack()

    idLabel=Label(miFrameEditar, text="ID:")
    idLabel.config(fg="Red")
    idLabel.grid(row=1, column=0, padx=5, pady=15, sticky="e")
    nombreLabel=Label(miFrameEditar, text="Nombre:")
    nombreLabel.grid(row=2, column=0, padx=5, pady=10, sticky="e")
    apellidoLabel=Label(miFrameEditar, text="Apellido:")
    apellidoLabel.grid(row=3, column=0, padx=5, pady=10,sticky="e")
    dniLabel=Label(miFrameEditar, text="DNI:")
    dniLabel.grid(row=4, column=0, padx=5, pady=10, sticky="e")

    miNombre = StringVar()
    miApellido = StringVar()
    miDni = StringVar()
    miId = StringVar()
    idEntry=Entry(miFrameEditar, textvariable=miId)
    idEntry.grid(row=1, column=1, padx=5, pady=16)
    idEntry.config(fg="red", bg="grey88")
    nombreEntry=Entry(miFrameEditar, textvariable=miNombre)
    nombreEntry.grid(row=2, column=1, padx=5, pady=10)
    apellidoEntry=Entry(miFrameEditar, textvariable=miApellido)
    apellidoEntry.grid(row=3, column=1, padx=5, pady=10)
    dniEntry=Entry(miFrameEditar, textvariable=miDni)
    dniEntry.grid(row=4, column=1, padx=5, pady=10)

    def append_select():
       cur_id = tabla.focus()

       if cur_id:  # do nothing if there"s no selection
            ventanaEditar.insert("", END, values=tabla.item(cur_id)["values"])


    def editarFinal():

        miConexion = sqlite3.connect('Personal')
        miCursor = miConexion.cursor()
        datos2 = miApellido.get().upper(), miNombre.get().capitalize(), miDni.get()
        miCursor.execute("""UPDATE DATOSPERSONAL SET APELLIDO=?, NOMBRE_PERSONAL=?, DNI=? WHERE ID="""+ miId.get(),(datos2))

        miConexion.commit()
        messagebox.showinfo("Aviso","EL registro ha sido actualizado con éxito")

    def botones():
        aceptarButton = True
        if aceptarButton == True:
            ventanaEditar.destroy()

    aceptarButton = Button(ventanaEditar, text="Aceptar", command=lambda:[editarFinal(), botones(), actualizar()])
    aceptarButton.place(x=113, y=180)
    cancelarButton = Button(ventanaEditar, text="Cancelar", command=botones)
    cancelarButton.place(x=185, y=180)

def borrarVentana():

    idBorrar = StringVar()

    ventanaBorrar=Toplevel(root)
    ventanaBorrar.title("Borrar registro")
    ventanaBorrar.geometry("165x135+520+210")
    ventanaBorrar.resizable(0,0)
    ventanaBorrar.transient(root)

    textoLabel=Label(ventanaBorrar, text="Ingrese el ID del registro\na eliminar", justify="left")
    textoLabel.place(x=25, y=10)
    idLabel=Label(ventanaBorrar, text="ID:")
    idLabel.config(fg="red")
    idLabel.place(x=25, y=58)

    idEntry=Entry(ventanaBorrar, width=10, textvariable= idBorrar)
    idEntry.config(bg="yellow")
    idEntry.place(x=50, y=58)

    def borrar():

        miConexion=sqlite3.connect('Personal')
        miCursor=miConexion.cursor()
        miCursor.execute("""DELETE FROM DATOSPERSONAL WHERE ID="""+ idBorrar.get())
        miConexion.commit()
        messagebox.showinfo("Aviso", "El registro ha sido eliminado")

    def botonesBorrar():
        botonAceptar=True

        if botonAceptar== True:
            ventanaBorrar.destroy()

    botonAceptar=Button(ventanaBorrar, text="Aceptar", command=lambda:[borrar(), botonesBorrar(), actualizar()])
    botonAceptar.place(x=23, y=100)
    botonCancelar=Button(ventanaBorrar, text="Cancelar", command=botonesBorrar)
    botonCancelar.place(x=90, y=100)

# ------RAIZ---------------------------------------------------------------------

root = Tk()
root.geometry("360x440+430+90")
root.config(bg="light blue")

# -----MENU----------------------------------------------------------------------

barraMenu = Menu(root)

root.config(menu=barraMenu)

bbddMenu = Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salir)

ayudaMenu = Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...",command=acercaDe)

barraMenu.add_cascade(label="Archivo", menu=bbddMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

miFrame = Frame(root)
miFrame.config(bg="light blue")
miFrame.pack()

# ----BOTON FRAME 1---------------------------------------------

botonActualizar = Button(miFrame, text="Actualizar", command=actualizar)
botonActualizar.config(cursor="hand2", bg="dodger blue")
botonActualizar.grid(row=0, column=0, sticky="sw", padx=10, pady=20)

botonAgregar = Button(miFrame, text="Agregar", command=agregar)
botonAgregar.config(cursor="hand2", bg="lime green")
botonAgregar.grid(row=0, column=1, sticky="sw", padx=10, pady=20)

botonEditar = Button(miFrame, text="Editar", command=editar)
botonEditar.config(cursor="hand2", bg="dark khaki")
botonEditar.grid(row=0, column=2, sticky="sw", padx=10, pady=20)

botonBorrar = Button(miFrame, text="Borrar", command=borrarVentana)
botonBorrar.config(cursor="pirate", bg="red")
botonBorrar.grid(row=0, column=3, sticky="sw", padx=10, pady=20)

# -----TABLA-----------------------------------------------------

miFrame2 = Frame(root)
miFrame2.config(bg="light blue")
miFrame2.pack()

# D.E.S changes:
# setting meaningful column names/fields
column_fields = ("id","apellido", "nombre", "dni",)
tabla = ttk.Treeview(miFrame2, height=15, columns=column_fields)
tabla.config(show="headings")  # showing headings only
tabla.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10)
# passing the new column names or identifiers to the .heading() method
tabla.heading("id", text="ID", anchor="center")
tabla.heading("apellido", text="Apellido", anchor="center")
tabla.heading("nombre", text="Nombre", anchor="center")
tabla.heading("dni", text="DNI", anchor="center")
tabla.column("id", stretch="no", width=30)
tabla.column("nombre", stretch="no", width=90)
tabla.column("apellido", stretch="no", width=90)
tabla.column("dni", stretch="no", width=90)
tabla.rowconfigure(0, weight=1)
tabla.columnconfigure(0, weight=1)
tabla.rowconfigure(1, weight=1)
tabla.columnconfigure(1, weight=1)

root.mainloop()