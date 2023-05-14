from customtkinter import *
from tkinter import filedialog, PhotoImage
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

    gray_hist = cv2.calcHist([gray], [0], None, [200], [0,200])
    plt.figure()
    plt.title("Histograma en escala de grises")
    plt.xlabel("bins")
    plt.ylabel("# de pixeles")
    plt.plot(gray_hist)
    plt.xlim([0,256])
    plt.show()



def equalizar_histograma():

    global image, gray, gray_hist
    
    #Ecualizar el histograma de la imagen en escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)

    # Mostrar la imagen original y la imagen ecualizada
    plt.subplot(2, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Imagen original")
    plt.xticks([]), plt.yticks([])
    
    plt.subplot(2, 2, 2)
    plt.imshow(equalized, cmap='gray')
    plt.title("Imagen ecualizada")
    plt.xticks([]), plt.yticks([])
    
    # Mostrar el histograma de la imagen original
    plt.subplot(2, 2, 3)
    plt.hist(gray.ravel(), 256, [0, 256])
    plt.title("Histograma original")
    plt.xlim([0, 256])
    
    # Mostrar el histograma de la imagen ecualizada
    plt.subplot(2, 2, 4)
    plt.hist(equalized.ravel(), 256, [0, 256])
    plt.title("Histograma ecualizado")
    plt.xlim([0, 256])
    
    plt.show()


def expandir_histograma():
    '''
    '''
    print("histograma expandido")



root = CTk()
root.title("Proyecto Final - Grupo 7")
root.geometry("700x500+200+20")

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

root.mainloop()