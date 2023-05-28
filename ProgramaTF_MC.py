from customtkinter import *
from tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2
import imutils
import numpy as np
import matplotlib.pyplot as plt

def elegir_imagen():

    path_image = filedialog.askopenfilename(filetypes = [
        ("image", ".jpg"),
        ("image", ".jpeg"),
        ("image", ".png")])
    
    if len(path_image) > 0:
        global image 

        image = cv2.imread(path_image)
        image = imutils.resize(image, height=780)

        imageToShow = imutils.resize(image, width=580)
        imageToShow = cv2.cvtColor(imageToShow, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(imageToShow)
        img = ImageTk.PhotoImage(image=im)

        lblInputImage.configure(image=img)
        lblInputImage.image = img

        lblInfo1 = CTkLabel(root, text="Imagen seleccionada")
        lblInfo1.grid(column=0, row=1, padx=5, pady=5)

def mostrar_histograma():
    
    global gray
    global gray_hist
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray_hist = cv2.calcHist([gray], [0], None, [256], [0,256])
    plt.figure()
    plt.title("Histograma en escala de grises")
    plt.xlabel("Intensidad iluminacion")
    plt.ylabel("# de pixeles")
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()


def equalizar_histograma():

    global image

    # Separar los canales de color de la imagen
    b, g, r = cv2.split(image)

    # Ecualizar el histograma de cada canal por separado
    b_equalized = cv2.equalizeHist(b)
    g_equalized = cv2.equalizeHist(g)
    r_equalized = cv2.equalizeHist(r)

    # Fusionar los canales ecualizados en una nueva imagen
    equalized_image = cv2.merge([b_equalized, g_equalized, r_equalized])

    # Mostrar la imagen original y la imagen con el histograma ecualizado
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(equalized_image, cv2.COLOR_BGR2RGB))
    plt.title("Imagen ecualizada")
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3)
    plt.hist(b.ravel(), 256, [0, 256], color='b', alpha=0.5)
    plt.hist(g.ravel(), 256, [0, 256], color='g', alpha=0.5)
    plt.hist(r.ravel(), 256, [0, 256], color='r', alpha=0.5)
    plt.title("Histograma original")
    plt.xlim([0, 256])

    plt.subplot(2, 2, 4)
    plt.hist(b_equalized.ravel(), 256, [0, 256], color='b', alpha=0.5)
    plt.hist(g_equalized.ravel(), 256, [0, 256], color='g', alpha=0.5)
    plt.hist(r_equalized.ravel(), 256, [0, 256], color='r', alpha=0.5)
    plt.title("Histograma ecualizado")
    plt.xlim([0, 256])

    plt.show()


def expandir_histograma():
    
    global image

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Obtener los valores mínimo y máximo de intensidad
    min_intensity = np.min(gray)
    max_intensity = np.max(gray)

    # Aplicar la transformación lineal para expandir el rango de intensidad
    expanded_gray = (gray - min_intensity) * (255 / (max_intensity - min_intensity))

    # Convertir la imagen expandida a formato de 3 canales para mostrarla junto con la imagen original
    expanded_image = cv2.cvtColor(expanded_gray.astype(np.uint8), cv2.COLOR_GRAY2BGR)

    # Mostrar la imagen original y la imagen con el histograma expandido
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2)
    plt.imshow(cv2.cvtColor(expanded_image, cv2.COLOR_BGR2RGB))
    plt.title("Imagen con histograma expandido")
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3)
    plt.hist(gray.ravel(), 256, [0, 256], color='gray', alpha=0.5)
    plt.title("Histograma original")
    plt.xlim([0, 256])

    plt.subplot(2, 2, 4)
    plt.hist(expanded_gray.ravel(), 256, [0, 256], color='gray', alpha=0.5)
    plt.title("Histograma expandido")
    plt.xlim([0, 256])

    plt.show()


def mostrar_integrantes():

    lblIntegrantes = CTkLabel(root, text="\nGrupo 7 \n\n Mathias Adriano Hidalgo Lopez \n\n Bruno Jaime Aguilar Espinoza  \n\n Josue Daniel Valverde Lopez \n\n Diego Jesus Alonso Garay \n\n Mauricio Alberto Salas Pujay")
    lblIntegrantes.grid(column=0, row=1, padx=5, pady=10)
    lblIntegrantes.configure(fg_color="cyan", justify="center", pady="10", corner_radius=5, text_color="black")


root = CTk()
root.title("Proyecto Final - Grupo 7")
root.geometry("750x550+200+20")


image = None

lblInputImage = CTkLabel(root, text="")
lblInputImage.grid(column=0, row=2)

btn1 = CTkButton(root, text= "Subir imagen", width=25, command=elegir_imagen, hover_color="#808080")
btn1.grid(column=0, row=0, padx=280, pady=10)

btn2 = CTkButton(root, text="Mostrar Histograma", command=mostrar_histograma, hover_color="#808080")
btn2.grid(column=0, row=5, padx=280, pady=10)

btn3 = CTkButton(root, text="Equalizar Histograma", command= equalizar_histograma, hover_color="#808080")
btn3.grid(column=0, row =7, pady =10)

btn4 = CTkButton(root, text="Expandir Histograma", command= expandir_histograma, hover_color="#808080")
btn4.grid(column=0, row =9, pady=10)

btn5 = CTkButton(root, text="Integrantes", command= mostrar_integrantes, hover_color="#808080")
btn5.grid(column=0, row =11, pady=10)

root.mainloop()