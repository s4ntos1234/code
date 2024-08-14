from tkinter import *
from tkinter import messagebox 
dict_users_clientes={"Andres":"123", "juan":"123123", "jua22n":"123123","1":"1"}
dict_servicios={"21":"1", "juan":"vunfnvnreinbe9vnvjfjfjfjfjf"}
dict_users_admin={"3112330150":"Messi123","1":"1"}
dict_jobs={}
nombre="" 
def ventana_cliente():
    root.title("Login user")    
    root.withdraw()     
    user=StringVar()
    key=StringVar()
    new_window_client_login=Toplevel()
    etiqueta_usuario=Label(new_window_client_login, text="User").place(x=10, y=10)
    usuario=Entry(new_window_client_login, textvariable=user).place(x=70, y=10)
    etiqueta_contraseña=Label(new_window_client_login,text="password").place(x=10,y=35)
    contraseña=Entry(new_window_client_login, textvariable=key).place(x=70, y=35)
    btn_login=Button(new_window_client_login, text="Login", command=lambda: obtener_variables(user, key,new_window_client_login)).place(x=10, y=60)
    btn_sign_up=Button(new_window_client_login, text="Sign Up", command=lambda: ventana_registrar(new_window_client_login)).place(x=60, y=60)
    btn_back=Button(new_window_client_login, text="Back", command=lambda: regresar_root(new_window_client_login)).place(x=10, y=93)
    
def ventana_registrar(new_window_client_login):
    root.title("Sign up user")
    new_window_client_login.withdraw()
    new_window_register=Toplevel()
    user=StringVar()
    key=StringVar()
    confirm_key=StringVar()
    etiqueta_usuario=Label(new_window_register, text="User").place(x=10, y=10)
    usuario=Entry(new_window_register, textvariable=user).place(x=115, y=10)
    etiqueta_contraseña=Label(new_window_register,text="password").place(x=10,y=35)
    contraseña=Entry(new_window_register, textvariable=key).place(x=115, y=35)
    etiqueta_confirmar_contraseña=Label(new_window_register,text="Confirm password").place(x=10,y=60)
    confirmar_contraseña=Entry(new_window_register,textvariable=confirm_key).place(x=115,y=60)
    btn_back=Button(new_window_register, text="Back", command=lambda: regresar_login(new_window_client_login, new_window_register)).place(x=10, y=110)
    btn_finish_sign_up=Button(new_window_register,text="finish sign up",command=lambda:terminar_sign_up(user.get(),key.get(),confirm_key.get(),new_window_client_login,new_window_register)).place(x=10,y=85)        

def ventana_servicios(new_window_client_login):
    
    
    root.title("Sevices")
    new_window_client_login.withdraw()
    new_window_services=Toplevel()
    valor=StringVar()
    phone=StringVar()
    etiqueta_servicios=Label(new_window_services, text="select a service").place(x=10,y=15)
    drop=OptionMenu(new_window_services,valor,"Catering", "School Feeeding","Company Feeding", "Institutional Administration").place(x=160,y=10)
    etiquta_telefono=Label(new_window_services,text="Enter your phone number").place(x=10,y=50)
    numero_de_telefono=Entry(new_window_services,textvariable=phone).place(x=160,y=50)
    btn_confirmar=Button(new_window_services,text="confirm",command=lambda:confirmar_orden(valor.get(),phone.get())).place(x=10,y=120)
    btn_job=Button(new_window_services,text="Request Job",command=lambda:ventana_job(new_window_services)).place(x=10,y=150)
    btn_back=Button(new_window_services, text="Back", command=lambda: regresar_login2(new_window_client_login, new_window_services)).place(x=10,y=180)
    etiqeta_p_wb=Label(new_window_services,text="Looking for more information? Visit https://aldisagourmet.com/").place(x=10,y=85)

def ventana_job(new_window_services):
    root.title("Request job")
    new_window_services.withdraw()
    new_window_job=Toplevel()
    job=StringVar()
    phone2=StringVar()
    etiqueta_job=Label(new_window_job,text="select a job").place(x=10,y=15)
    drop=OptionMenu(new_window_job,job,"Cashier","Kitchen Helper","Chef").place(x=160,y=15)
    etiqueta_phone2=Label(new_window_job,text="Enter your phone number").place(x=10,y=50)
    phone_2=Entry(new_window_job,textvariable=phone2).place(x=160,y=50)
    btn_confirm_job=Button(new_window_job,text="confirm",command=lambda:obtener_jobs(job.get(),phone2.get())).place(x=10,y=85)
    btn_back=Button(new_window_job, text="Back", command=lambda: regresar_services(new_window_services, new_window_job)).place(x=10, y=115)

def ventana_empleado():
    root.title("Login admin")
    root.withdraw()
    cellphone=StringVar()
    password=StringVar()
    new_window_worker=Toplevel()
    etiqueta_phone=Label(new_window_worker,text="phone").place(x=10,y=10)
    number_cellphone=Entry(new_window_worker,textvariable=cellphone).place(x=80,y=10)
    etiqueta_password=Label(new_window_worker,text="password").place(x=10,y=30)
    password_1=Entry(new_window_worker,textvariable=password).place(x=80,y=30)
    btn_login2=Button(new_window_worker,text="Login",command=lambda:obtener_cuentas(cellphone, password,new_window_worker)).place(x=10,y=50)
    btn_back=Button(new_window_worker,text="Back",command=lambda:regresar_l_admin(root,new_window_worker)).place(x=10,y=80)
    
    
def ventana_solicitudes(new_window_worker):
    root.title("See requested jobs")
    new_window_worker.withdraw()
    new_window_solicitud_s=Toplevel()
    etiqueta_ver_s=Label(new_window_solicitud_s,text="see requested services").place(x=10,y=10)
    boton_imprimir =Button(new_window_solicitud_s, text="request services", command=imprimir_sevices).place(x=145,y=10)
    btn_jobs=Button(new_window_solicitud_s,text="see requested jobs",command=lambda:ventana_solicitud_j(new_window_solicitud_s)).place(x=10,y=40)
    btn_back=Button(new_window_solicitud_s,text="Back",command=lambda:regresar_ver_services(new_window_solicitud_s,new_window_worker)).place(x=10,y=70)
    
def ventana_solicitud_j(new_window_solicitud_s):
    root.title("See jobs")
    new_window_solicitud_s.withdraw()
    new_window_solicitud_j=Toplevel()
    etiqueta_ver_j=Label(new_window_solicitud_j,text="see requested jobs").place(x=10,y=10)
    boton_imprimir =Button(new_window_solicitud_j, text="requested jobs", command=imprimir_jobs).place(x=110,y=10)
    btn_back=Button(new_window_solicitud_j,text="Back",command=lambda:regresar_ver_j(new_window_solicitud_j,new_window_solicitud_s)).place(x=10,y=35)
    
    
def obtener_variables(user, key,new_window_client_login,):
    usuario_ingresado=user.get()
    clave_ingresada=key.get()
    if usuario_ingresado in dict_users_clientes:
        if dict_users_clientes.get(usuario_ingresado)==clave_ingresada:
            nombre=usuario_ingresado
            
            
            ventana_servicios(new_window_client_login)
        else:
            messagebox.showerror("Error","Wrong password")
            
    else:
        messagebox.showerror("Error","Non-existent account")      
    
def regresar_root(new_window_client_login):
    new_window_client_login.withdraw()
    root.deiconify()

def terminar_sign_up(user,key,confirm_key,new_window_client_login, new_window_register): 
    if user not in dict_users_clientes:
        if key==confirm_key:
            dict_users_clientes.update({user:key})
            regresar_login(new_window_client_login, new_window_register)
        else:
            messagebox.showerror("Error","Passwords do not match ")
    else:
        messagebox.showerror("Error", "This user already exists")

def regresar_login(new_window_client_login, new_window_register):
    new_window_register.withdraw()
    new_window_client_login.deiconify()
    
def regresar_login2(new_window_client_login, new_window_services):
    new_window_services.withdraw()
    new_window_client_login.deiconify()
    
def regresar_services(new_window_services, new_window_job):
    new_window_job.withdraw()
    new_window_services.deiconify()
    
def regresar_ver_j(new_window_silcitud_j,new_window_solicitud_s):
    new_window_silcitud_j.withdraw()
    new_window_solicitud_s.deiconify
    
def regresar_ver_services(new_window_solicitud_s,new_window_worker):
    new_window_solicitud_s.withdraw()
    new_window_worker.deiconify()
    
def regresar_l_admin(root,new_window_worker):
    new_window_worker.withdraw()
    root.deiconify()
    
def confirmar_orden(valor,phone):
    dict_servicios.update({valor:phone})
    messagebox.showinfo("Order","Order taken succesfully")
    
def obtener_cuentas(cellphone, password, new_window_worker):
    cellphone_ingresado=cellphone.get()
    password_ingresada=password.get()
    if cellphone_ingresado in dict_users_admin:
        if dict_users_admin.get(cellphone_ingresado)==password_ingresada:
            nombre=cellphone_ingresado
            ventana_solicitudes(new_window_worker)
        else:
            messagebox.showerror("Error","Wrong password")
            
    else:
        messagebox.showerror("Error","Non-existent account")

def obtener_jobs(job,phone2):
    dict_jobs.update({job:phone2})
    messagebox.showinfo("Your job will be taken into account.")
    
def imprimir_sevices():
    messagebox.showinfo("Orders",dict_servicios)
    
def imprimir_jobs():
    print(dict_jobs)

root=Tk()
root.geometry("400x300")
btn=Button(root, text="Client", command=ventana_cliente).place(x=130,y=100)
btn=Button(root, text="Admin", command=ventana_empleado).place(x=220,y=100)
root.mainloop()