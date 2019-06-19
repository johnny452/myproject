#!/usr/bin/python
# -*- coding: utf-8 -*- 
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as FileDialog
from datetime import date
import sqlite3 # modulo de conexion con sqlite3 
from PIL import ImageTk, Image

class Product:
    #conexion con la base de datos
    db_lab = 'vitasis.db'
    
    
    def __init__(self, window):
        
               
        self.wind = window
        self.wind.title('Vitasis Laboratorio Médico')
        self.wind.configure(background = 'gray')

        #carga de la imagen
        img = Image.open('logo QR.png')
        self._image_logo = ImageTk.PhotoImage(img) 
        widget = tk.Label(self.wind, image = self._image_logo).grid( row= 0, column = 0, sticky = W + E)
        
                
        #creando el contenedor REGISTRO DE PACIENTE
        frame = LabelFrame(self.wind, text = 'Registro de paciente', labelanchor = N, font = ('bold'))
        frame.grid(row = 1, column = 0, padx = 5, pady = 20, ipadx = 30, sticky = W)
        frame.configure(background = 'gray')
        
        
        #entrada para nombre
        Label(frame, text = 'Nombre: ', bg = 'gray').grid(row = 1, column = 0)
        self.name = Entry(frame, width = 30)
        self.name.focus()
        self.name.grid(row = 1, column = 1)

        #Entrada de direccion
        Label(frame, text = 'Direccion: ', bg = 'gray').grid(row = 2, column = 0)
        self.adress = Entry(frame, width = 30)
        self.adress.grid(row = 2, column = 1)

        #Edad
        Label(frame, text = 'Edad', bg = 'gray').grid(row = 1, column = 3, padx = 50, pady = 10)
        self.edad = Entry(frame, width = 5)
        self.edad.grid(row = 1, column = 4, pady = 10, sticky = W)
         
        #Sexo
        Label(frame, text = 'Sexo', bg = 'gray').grid(row = 2, column = 3, padx = 10, pady = 10)
        self.sexo = tk.StringVar(frame)
        self.sexo.set('---------')
        sexos = ('Masculino', 'Femenino')
        self.menu_sexo = tk.OptionMenu(frame, self.sexo, *sexos).grid(row = 2, column = 4, pady = 10, sticky = W)
        
        
        #Entrada diagnostico
        Label(frame, text = 'Diagnostico: ', bg = 'gray').grid(row = 3, column = 0, pady = 10)
        self.diag = Entry(frame, width = 30)
        self.diag.grid(row = 3, column = 1)

        #Entrada medico
        Label(frame, text = 'Médico: ', bg = 'gray').grid(row = 3, column = 3, pady = 10)
        self.medico = Entry(frame, width = 30)
        self.medico.grid(row = 3, column = 4, sticky = W)

                       
        #contenedor 2 ORDEN DE SERVICIO y FECHA DE INGRESO
        frame2 = LabelFrame(self.wind, text = 'Orden de servicio', labelanchor = N, font = ('Verdana', 16, 'bold'))
        frame2.grid(row = 1, column = 1, padx = 5, pady = 20, ipadx = 30, sticky = W)
        frame2.configure(background = 'gray')
       

        Label(frame2, text = 'Número de Orden', bg = 'gray').grid(row = 1, column = 1, pady = 3, sticky = W + E)
        #Entry(frame2, textvariable = StringVar(frame2, value = '4856'), state = 'readonly').grid(row = 2, column = 5, pady = 10) #modificar para que la orden de servicio sea un numero que incremente
        self.message1 = Label(frame2, text = '', fg = 'red', font = ('Verdana', 18), bg = 'gray')
        self.message1.grid(row = 2, column = 1, pady = 3, sticky = W + E)  
        self.orden = 1
        #self.numero_orden = self.folio
        self.orden=str(self.orden)
        self.message1['text'] = '{}'.format(self.orden)
        self.folio = int(6)

        Label(frame2, text = 'Fecha de ingreso', bg = 'gray').grid(row = 3, column = 1, pady = 3, sticky = W + E)
        self.fecha_actual = date.today()
        self.message2 = Label(frame2, text = '', fg = 'red', font = ('Verdana', 18), bg = 'gray')
        self.message2.grid(row = 4, column = 1, pady = 3, sticky = W + E)
        self.message2['text'] = '{}'.format(self.fecha_actual.strftime('%d, %b, %Y'))
        
          
        #contenedor 4 estudios
        frame4 = LabelFrame(self.wind, text = 'Estudios de laboratorio', labelanchor = N)
        frame4.grid(row = 2, column = 0, pady = 5, padx = 5, ipadx = 30, sticky = W)
        frame4.configure(background = 'gray')
        
        
        Label(frame4, text = 'Pruebas Clinicas 1', bg = 'gray').grid(row = 1, column = 0, pady = 10, sticky = W + E)
        self.prueba = tk.StringVar(frame4)
        self.prueba.set('---------------------------------------------------------------')
        pruebas = ('ANTIDOPING EN ORINA', 'BIOMETRIA HEMATICA COMPLETA BHC', 'COPROPARASITOSCOPICO EN SERIE DE 3', 'EXAMEN GENERAL DE ORINA', 'ESPERMATOBIOSCOPIA DIRECTA','EXUDADO FARINGEO CON ANTIBIOGRAMA', 'GLUCOSA DESTROXIS', 'GLUCOSA', 'GONADOTROFINA CORIONICA FRACCION BETA', 'GRUPO SANGUINEO Y FACTOR RH',
                   'HEMOGLOBINA GLUCOSILADA', 'PAPANICOLAU', 'PRUEBA INMUNOLOGICA DE EMBARAZO', 'GLUCOSA,COLESTEROL Y TRIGLICERIDOS', 'QUIMICA DE 4 ELEMENTOS', 'QUIMICA DE 5 ELEMENTOS', 'QUIMICA DE 6 ELEMENTOS', 'QUIMICA DE 12 ELEMENTOS', 'QUIMICA DE 18 ELEMENTOS', 'QUIMICA DE 25 ELEMENTOS','QUIMICA DE 32 ELEMENTOS',
                   'REACCIONES FEBRILES', 'TAMIZ METABOLICO NEONATAL CON AMINOACIDOS COMPLETO', 'TIEMPOS DE COAGULACION TTPA,TP, TS, TT', 'UROCULTIVO', 'VDRL', 'VIH PRUEBA DE TAMIZAJE', 'PERFIL HORMONAL FEMENINO BASICO', 'PERFIL HORMONAL GINECOLOGICO','PERFIL LIPIDOS', 'PERFIL PRENATAL', 'PERFIL PROSTATICO', 'PERFIL REUMATICO', 
                   'PERFIL TIROIDEO COMPLETO')                
        self.menu_prueba = tk.OptionMenu(frame4, self.prueba, *pruebas).grid(row = 1, column = 1, sticky = W + E, pady = 10)
        
        
        #fecha de estudio
        Label(frame4, text = ' ', bg = 'gray').grid(row = 1, column = 2, pady = 10, padx = 10, sticky = W)
        message3 = Label(frame4, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message3.grid(row = 1, column = 2, pady = 10, padx = 10, sticky = W)  
        message3['text'] = 'Fecha de estudio'
        self.fecha_estudio = date.today()
        message4 = Label(frame4, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message4.grid(row = 1, column = 3, pady = 10, sticky = W)
        message4['text'] = '{}'.format(self.fecha_estudio.strftime('%d, %b, %Y'))

        
        Label(frame4, text = 'Pruebas Clinicas 2', bg = 'gray').grid(row = 2, column = 0, pady = 10, sticky = W + E)
        self.prueba2 = tk.StringVar(frame4)
        self.prueba2.set('N/A')
        pruebas2 = ('N/A', 'ANTIDOPING EN ORINA', 'BIOMETRIA HEMATICA COMPLETA BHC', 'COPROPARASITOSCOPICO EN SERIE DE 3', 'EXAMEN GENERAL DE ORINA', 'ESPERMATOBIOSCOPIA DIRECTA','EXUDADO FARINGEO CON ANTIBIOGRAMA', 'GLUCOSA DESTROXIS', 'GLUCOSA', 'GONADOTROFINA CORIONICA FRACCION BETA', 'GRUPO SANGUINEO Y FACTOR RH',
                   'HEMOGLOBINA GLUCOSILADA', 'PAPANICOLAU', 'PRUEBA INMUNOLOGICA DE EMBARAZO', 'GLUCOSA,COLESTEROL Y TRIGLICERIDOS', 'QUIMICA DE 4 ELEMENTOS', 'QUIMICA DE 5 ELEMENTOS', 'QUIMICA DE 6 ELEMENTOS', 'QUIMICA DE 12 ELEMENTOS', 'QUIMICA DE 18 ELEMENTOS', 'QUIMICA DE 25 ELEMENTOS','QUIMICA DE 32 ELEMENTOS',
                   'REACCIONES FEBRILES', 'TAMIZ METABOLICO NEONATAL CON AMINOACIDOS COMPLETO', 'TIEMPOS DE COAGULACION TTPA,TP, TS, TT', 'UROCULTIVO', 'VDRL', 'VIH PRUEBA DE TAMIZAJE', 'PERFIL HORMONAL FEMENINO BASICO', 'PERFIL HORMONAL GINECOLOGICO','PERFIL LIPIDOS', 'PERFIL PRENATAL', 'PERFIL PROSTATICO', 'PERFIL REUMATICO', 
                   'PERFIL TIROIDEO COMPLETO')  
        self.menu_prueba2 = tk.OptionMenu(frame4, self.prueba2, *pruebas2).grid(row = 2, column = 1, sticky = W + E, pady = 10)

        #fecha de entrega
        Label(frame4, text = ' ', bg = 'gray').grid(row = 2, column = 2, pady = 10, )
        message5 = Label(frame4, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message5.grid(row = 2, column = 2, pady = 10, padx = 10)  
        message5['text'] = 'Fecha de entrega'
        self.entrega = Entry(frame4, width = 10)
        self.entrega.grid(row = 2, column = 3, sticky = W)

        Label(frame4, text = 'Pruebas Clinicas 3', bg = 'gray').grid(row = 3, column = 0, pady = 10, sticky = W + E)
        self.prueba3 = tk.StringVar(frame4)
        self.prueba3.set('N/A')
        pruebas3 = ('N/A', 'ANTIDOPING EN ORINA', 'BIOMETRIA HEMATICA COMPLETA BHC', 'COPROPARASITOSCOPICO EN SERIE DE 3', 'EXAMEN GENERAL DE ORINA', 'ESPERMATOBIOSCOPIA DIRECTA','EXUDADO FARINGEO CON ANTIBIOGRAMA', 'GLUCOSA DESTROXIS', 'GLUCOSA', 'GONADOTROFINA CORIONICA FRACCION BETA', 'GRUPO SANGUINEO Y FACTOR RH',
                   'HEMOGLOBINA GLUCOSILADA', 'PAPANICOLAU', 'PRUEBA INMUNOLOGICA DE EMBARAZO', 'GLUCOSA,COLESTEROL Y TRIGLICERIDOS', 'QUIMICA DE 4 ELEMENTOS', 'QUIMICA DE 5 ELEMENTOS', 'QUIMICA DE 6 ELEMENTOS', 'QUIMICA DE 12 ELEMENTOS', 'QUIMICA DE 18 ELEMENTOS', 'QUIMICA DE 25 ELEMENTOS','QUIMICA DE 32 ELEMENTOS',
                   'REACCIONES FEBRILES', 'TAMIZ METABOLICO NEONATAL CON AMINOACIDOS COMPLETO', 'TIEMPOS DE COAGULACION TTPA,TP, TS, TT', 'UROCULTIVO', 'VDRL', 'VIH PRUEBA DE TAMIZAJE', 'PERFIL HORMONAL FEMENINO BASICO', 'PERFIL HORMONAL GINECOLOGICO','PERFIL LIPIDOS', 'PERFIL PRENATAL', 'PERFIL PROSTATICO', 'PERFIL REUMATICO', 
                   'PERFIL TIROIDEO COMPLETO')  
        self.menu_prueba3 = tk.OptionMenu(frame4, self.prueba3, *pruebas3).grid(row = 3, column = 1, sticky = W + E, pady = 10)

        #atendido por
        Label(frame4, text = ' ', bg = 'gray').grid(row = 3, column = 2, pady = 10)
        message6 = Label(frame4, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message6.grid(row = 3, column = 2, pady = 10, padx = 10, sticky = W)  
        message6['text'] = 'Atendido por:'
        self.worker = Entry(frame4, width = 10)
        self.worker.grid(row = 3, column = 3, sticky = W)

        Label(frame4, text = 'Pruebas Clinicas 4', bg = 'gray').grid(row = 4, column = 0, pady = 10, sticky = W + E)
        self.prueba4 = tk.StringVar(frame4)
        self.prueba4.set('N/A')
        pruebas4 = ('N/A', 'ANTIDOPING EN ORINA', 'BIOMETRIA HEMATICA COMPLETA BHC', 'COPROPARASITOSCOPICO EN SERIE DE 3', 'EXAMEN GENERAL DE ORINA', 'ESPERMATOBIOSCOPIA DIRECTA','EXUDADO FARINGEO CON ANTIBIOGRAMA', 'GLUCOSA DESTROXIS', 'GLUCOSA', 'GONADOTROFINA CORIONICA FRACCION BETA', 'GRUPO SANGUINEO Y FACTOR RH',
                   'HEMOGLOBINA GLUCOSILADA', 'PAPANICOLAU', 'PRUEBA INMUNOLOGICA DE EMBARAZO', 'GLUCOSA,COLESTEROL Y TRIGLICERIDOS', 'QUIMICA DE 4 ELEMENTOS', 'QUIMICA DE 5 ELEMENTOS', 'QUIMICA DE 6 ELEMENTOS', 'QUIMICA DE 12 ELEMENTOS', 'QUIMICA DE 18 ELEMENTOS', 'QUIMICA DE 25 ELEMENTOS','QUIMICA DE 32 ELEMENTOS',
                   'REACCIONES FEBRILES', 'TAMIZ METABOLICO NEONATAL CON AMINOACIDOS COMPLETO', 'TIEMPOS DE COAGULACION TTPA,TP, TS, TT', 'UROCULTIVO', 'VDRL', 'VIH PRUEBA DE TAMIZAJE', 'PERFIL HORMONAL FEMENINO BASICO', 'PERFIL HORMONAL GINECOLOGICO','PERFIL LIPIDOS', 'PERFIL PRENATAL', 'PERFIL PROSTATICO', 'PERFIL REUMATICO', 
                   'PERFIL TIROIDEO COMPLETO')  
        self.menu_prueba4 = tk.OptionMenu(frame4, self.prueba4, *pruebas4).grid(row = 4, column = 1, sticky = W + E, pady = 10)

        Label(frame4, text = 'Promocion', bg = 'gray').grid(row = 4, column = 2, padx = 10, pady = 10, sticky = W)
        self.promo = tk.StringVar(frame4)
        self.promo.set('---------')
        promos = ('N/A', "50%_de descuento")
        self.menu_promos = tk.OptionMenu(frame4, self.promo, *promos).grid(row = 4, column = 3, pady = 10, sticky = W)

        Label(frame4, text = 'Pruebas Clinicas 5', bg = 'gray').grid(row = 5, column = 0, pady = 10, sticky = W + E)
        self.prueba5 = tk.StringVar(frame4)
        self.prueba5.set('N/A')
        pruebas5 = ('N/A', 'ANTIDOPING EN ORINA', 'BIOMETRIA HEMATICA COMPLETA BHC', 'COPROPARASITOSCOPICO EN SERIE DE 3', 'EXAMEN GENERAL DE ORINA', 'ESPERMATOBIOSCOPIA DIRECTA','EXUDADO FARINGEO CON ANTIBIOGRAMA', 'GLUCOSA DESTROXIS', 'GLUCOSA', 'GONADOTROFINA CORIONICA FRACCION BETA', 'GRUPO SANGUINEO Y FACTOR RH',
                   'HEMOGLOBINA GLUCOSILADA', 'PAPANICOLAU', 'PRUEBA INMUNOLOGICA DE EMBARAZO', 'GLUCOSA,COLESTEROL Y TRIGLICERIDOS', 'QUIMICA DE 4 ELEMENTOS', 'QUIMICA DE 5 ELEMENTOS', 'QUIMICA DE 6 ELEMENTOS', 'QUIMICA DE 12 ELEMENTOS', 'QUIMICA DE 18 ELEMENTOS', 'QUIMICA DE 25 ELEMENTOS','QUIMICA DE 32 ELEMENTOS',
                   'REACCIONES FEBRILES', 'TAMIZ METABOLICO NEONATAL CON AMINOACIDOS COMPLETO', 'TIEMPOS DE COAGULACION TTPA,TP, TS, TT', 'UROCULTIVO', 'VDRL', 'VIH PRUEBA DE TAMIZAJE', 'PERFIL HORMONAL FEMENINO BASICO', 'PERFIL HORMONAL GINECOLOGICO','PERFIL LIPIDOS', 'PERFIL PRENATAL', 'PERFIL PROSTATICO', 'PERFIL REUMATICO', 
                   'PERFIL TIROIDEO COMPLETO')  
        self.menu_prueba5 = tk.OptionMenu(frame4, self.prueba5, *pruebas5).grid(row = 5, column = 1, sticky = W + E, pady = 10)
        
    
       #botones de cargar e imprimir NO OLVIDES EL COMMAND PARA QUE SE REALICE LA RUTINA DE OBTENCION DE PACIENTES
        Button(frame4, text = 'Guardar registro', command = self.guardar).grid(row = 6, column = 2, pady = 10) #command = self.ventana_paciente
        Button(frame4, text = 'Imprimir').grid(row = 6, column = 3, pady = 10)

        #contenedor 5 observaciones
        frame5 = LabelFrame(self.wind, text = 'Observaciones', labelanchor = N )
        frame5.grid(row = 4, column = 0, pady = 5, padx = 5, sticky = W)
        frame5.configure(background = 'gray')
        self.texto = Text(frame5, width = 120, height = 6)
        self.texto.grid(row = 1, column = 0, pady = 10, padx = 10 )

        #contenedor 6 totales 
        frame6 = LabelFrame(self.wind, text = 'Costo a pagar', labelanchor = N)
        frame6.grid(row = 2, column = 1, pady = 10, padx = 5, sticky = N )
        frame6.configure(background = 'gray')
        
        Label(frame6, text = ' ', bg = 'gray').grid(row = 1, column = 1, pady = 10, sticky = W )
        message8 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message8.grid(row = 1, column = 1, pady = 10, padx = 10, sticky = W)  
        message8['text'] = 'Subtotal'
        Label(frame6, text = ' ', bg = 'gray').grid(row = 1, column = 2, pady = 10, sticky = W )
        self.message9 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        self.message9.grid(row = 1, column = 2, pady = 10, padx = 10, sticky = W)  
        self.message9['text'] = '$ 150.00'
        self.subtotal = 150
        
        message10 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message10.grid(row = 2, column = 1, pady = 10, padx = 10, sticky = W)  
        message10['text'] = 'IVA 16%'
        Label(frame6, text = ' ', bg = 'gray').grid(row = 1, column = 2, pady = 10, sticky = W )
        self.message11 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        self.message11.grid(row = 2, column = 2, pady = 10, padx = 10, sticky = W)  
        self.message11['text'] = '$ 24.00'
        
        message12 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message12.grid(row = 3, column = 1, pady = 10, padx = 10, sticky = W)  
        message12['text'] = 'Total'
        Label(frame6, text = ' ', bg = 'gray').grid(row = 1, column = 2, pady = 10,sticky = W )
        self.message13 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        self.message13.grid(row = 3, column = 2, pady = 10, padx = 10, sticky = W)  
        self.message13['text'] = '$ 174.00'
        self.total = 174

        Label(frame6, text = 'Anticipo', bg = 'gray').grid(row = 4, column = 1, padx = 10, pady = 10, sticky = W)
        self.anticipo = Entry(frame6, width = 5)
        self.anticipo.grid(row = 4, column = 2, pady = 10, sticky = W)

        message14 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        message14.grid(row = 5, column = 1, pady = 10, padx = 10, sticky = W)  
        message14['text'] = 'Saldo a pagar'
        Label(frame6, text = ' ', bg = 'gray').grid(row = 1, column = 2, pady = 10, )
        self.message15 = Label(frame6, text = '', fg = 'black', font = ('Verdana', 12), bg = 'gray')
        self.message15.grid(row = 5, column = 2, pady = 10, padx = 10, sticky = W)  
        self.message15['text'] = '$ 0.00'
        self.saldo_a_pagar= 0
        
        
        Button(frame6, text = 'Pagado', command = self.pagar).grid(row = 6, columnspan = 3, pady = 10, padx = 10, sticky = W + E) #command = self.ventana_paciente
    
    

    # Ejecutar consulta
    def run_query(self, query, parameters = ()):
        with sqlite3.connect(self.db_lab) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result
        
     #Ventana emergente para guardar paciente
    def pagar(self):
        messagebox.showinfo('Pagar estudios', 'Monto pagado')
        #print(self.menu_prueba)
            
     # Consulta de datos
        query = 'SELECT * FROM paciente ORDER BY folio DESC'
        #query("SELECT folio, nombre, direccion, edad, sexo, pruebas_clinicas_1, pruebas_clinicas_2, pruebas_clinicas_3, pruebas_clinicas_4, pruebas_clinicas_5, fecha_de_estudio, fecha_de_entrega, antendido, promocion, subtotal,anticipo, total, saldo_a_pagar FROM paciente")
        db_rows = self.run_query(query)

    #validacion 
    def validation(self):
        return len(self.name.get()) != 0 and len(self.adress.get()) != 0 
    
    #Guardar paciente
    def guardar(self):
        print(self.folio)
        print(self.name.get())
        print(self.adress.get())
        print(self.sexo.get())
        print(self.edad.get())
        print(self.diag.get()) # no
        print(self.medico.get()) # no
        print(self.prueba.get())
        print(self.prueba2.get())
        print(self.prueba3.get())
        print(self.prueba4.get())
        print(self.prueba5.get())
        print(self.fecha_estudio)
        print(self.entrega.get())
        print(self.worker.get())
        print(self.promo.get())
        print(self.subtotal)
        print(self.total)
        print(self.anticipo.get())
        print(self.saldo_a_pagar)
        
                 
        if self.validation():
            query = 'INSERT INTO paciente VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
            parameters =  (self.folio, self.name.get(), self.adress.get(), self.edad.get(), self.sexo.get(), self.prueba.get(), self.prueba2.get(), self.prueba3.get(), self.prueba4.get(), self.prueba5.get(), self.fecha_estudio, self.entrega.get(), self.worker.get(), self.promo.get(), self.subtotal, self.anticipo.get(), self.total, self.saldo_a_pagar)
            self.run_query(query, parameters)
            messagebox.showinfo('Guardar', 'Paciente guardado')
            self.name.delete(0, END)
            self.adress.delete(0, END)
            self.edad.delete(0, END)
            self.sexo.set('---------') 
            self.prueba.set('---------------------------------------------------------------'), 
            self.prueba2.set('N/A') 
            self.prueba3.set('N/A') 
            self.prueba4.set('N/A') 
            self.prueba5.set('N/A')
            self.entrega.delete(0, END)
            self.worker.delete(0, END)
            self.promo.set('---------')
            self.diag.delete(0, END) # no
            self.medico.delete(0, END)
            #self.subtotal
            self.anticipo.delete(0, END)
            #self.total 
            #self.saldo_a_pagar
        else:
           messagebox.showwarning('Atención', 'Por favor rellene todos los campos')
         #   self.get_pacient()
           
        #   self.name.delete(0, END)
        #   self.adress.delete(0, END)
        
    

            #numero de orden
    #def orden(self):
       # self.folio = self.folio + 1
        

       
    


    

        



if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()