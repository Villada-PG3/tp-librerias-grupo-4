import tkinter as tk
import qrcode
import webbrowser

def generar_qr_y_abrir():
    url = url_entry.get()
    file_name = file_entry.get() + ".png"

    codigo_qr = qrcode.make(url)
    codigo_qr.save(file_name)

    pagina_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <link rel="shortcut icon" href="https://cdn-icons-png.freepik.com/512/91/91868.png">
            <title>Codigo QR generado</title>
        </head>
        <body style="align-items: center;justify-content: center;display: flex; flex-direction: column;font-family: system-ui;">    
            <main style="align-items: center;
                    justify-content: center;
                    height: 250px;
                    display: flex;
                    flex-direction: column;">
                    <h1 style="text-align:center;">Informacion del qr:</h1>
                    <h2>Url Ingresada: <span style="font-weight: 600;
                    color: #46a2fd;">{url}</span></h2>
                    <h2>Archivo guardado como: <span style="font-weight: 600;
                    color: #46a2fd;">{file_name}</span></h2>
                    <a href="https://{url}" target="_blank" style="padding: 10px;
                    border-radius: 10px;
                    color: #fff;
                    font-weight: 500;
                    text-decoration: none;
                    background-color: #46a2fd;">Visitar Sitio</a>
            </main>
            <h1>Qr Generado: </h1>  
            <img style="width:40%; height:40%;" src="{file_name}" alt="Codigo QR generado">
        </body>    
        </html>
        """
    with open("pagina_qr.html", "w") as archivo_html:
        archivo_html.write(pagina_html)
    webbrowser.open_new_tab("pagina_qr.html")
    url_entry.delete(0, tk.END)
    file_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Generador de Código QR")
root.geometry("500x200")
font_size = 16

url_label = tk.Label(root, text="Ingresa la URL sin formato (https:// ó www):")

url_label.place(relx=0.25, rely=0.3, anchor="center")

url_entry = tk.Entry(root)
url_entry.place(relx=0.75, rely=0.3, anchor="center")


file_label = tk.Label(root, text="Ingresa el nombre del archivo a guardar: ")
file_label.place(relx=0.25, rely=0.5, anchor="center")

file_entry = tk.Entry(root)
file_entry.place(relx=0.75, rely=0.5, anchor="center")

generar_button = tk.Button(root, text="Generar y Visualizar QR", command=generar_qr_y_abrir)
generar_button.place(relx=0.5, rely=0.7, anchor="center")

root.mainloop()