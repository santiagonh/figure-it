#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PIL as pl
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from IPython.display import display
import random
import math


# In[2]:


#función que crea las áreas de las figuras, devuelve un diccionario.
def areas():
    area_principal=random.randint(2000, 18000)
    
    area_a=area_principal + (random.randint(-1000, 1800))
    area_b=area_principal + (random.randint(-1000, 1800))
    area_c=area_principal + (random.randint(-1000, 1800))
    diccionario_areas = {"principal":area_principal, "figura_a":area_a, "figura_b":area_b, "figura_c":area_c}
    return diccionario_areas


    
    


# In[3]:


diccionario_areas=areas()
diccionario_areas


# In[4]:


#función que obtiene los lados del rectángulo a partir del area obtenida en def areas()
def lados_rect(area):
    base=random.randint(100, 200)
    altura=area/base
    dic_principal={"base":base, "altura":altura}
    return dic_principal


# In[5]:


dic_principal=lados_rect(diccionario_areas["principal"])


# In[17]:


dic_principal


# In[7]:


#función para crear diámetros a partir de las áreas de def areas(), devuelve otro diccionario
def diametros(area_a,area_b,area_c):
    diametro_a=(area_a/math.pi)**(1/2)*2
    diametro_b=(area_b/math.pi)**(1/2)*2
    diametro_c=(area_c/math.pi)**(1/2)*2
    dic_diametro={"diametro_a":diametro_a,"diametro_b":diametro_b,"diametro_c":diametro_c}
    return dic_diametro


# In[8]:


diametros=diametros(diccionario_areas['figura_a'], diccionario_areas['figura_b'], diccionario_areas['figura_c'])


# In[9]:


diametros


# In[23]:


#función que hace el dibujo para adivinar las figuras a partir de diámetros (obtenidos de def diametros) 
# y lados de rectangulo (obtenidos de def lados_rect()), traza dibujo.
def rect (a, b, c, d, e):
    im = Image.new('RGB', (666, 400), (200, 200, 200))
    draw = ImageDraw.Draw(im)

    # font = ImageFont.truetype(<font-file>, <font-size>)
    font_type="/Users/groundcontrol/Documents/Processing/modes/PythonMode/examples/Basics/Data/DatatypeConversion/data/Georgia.ttf"
    font = ImageFont.truetype(font_type, 25)
    
    draw.rectangle((272, 50, 272+e, 50+d), fill="red")
    
    draw.ellipse((50, 200, 50+a, 200+a), fill=(0, 192, 192))
    draw.ellipse((272, 200, 272+b, 200+b), fill=(0, 192, 192))
    draw.ellipse((472, 200, 472+c, 200+c), fill=(0, 192, 192))
    


    draw.text((50, 250),"a",(255,255,255), font=font)
    draw.text((272, 250),"b",(255,255,255), font=font)
    draw.text((472, 250),"c",(255,255,255), font=font)

    return im


# In[11]:


# función que calcula qué figura es la ganadora
def figura_ganadora(principal, figura_a, figura_b, figura_c):
    dic_fig_ganadora={"a":(principal-figura_a)**2, "b":(principal-figura_b)**2, "c":(principal-figura_c)**2}
    print(dic_fig_ganadora)
    return dic_fig_ganadora
    
    


# In[12]:


diferencia=figura_ganadora(diccionario_areas["principal"], diccionario_areas["figura_a"], diccionario_areas["figura_b"], diccionario_areas["figura_c"])


# In[13]:


diccionario_areas


# In[24]:


im=rect(diametros["diametro_a"], diametros["diametro_b"], diametros["diametro_c"],dic_principal["base"], dic_principal["altura"] )


# In[15]:



#función que obtiene input de usuario y comunica ganador"
def ganador():

    input_usuario=input("Elige cuál de las figuras azules tienen el área más parecida a la figura roja")
    if input_usuario == min(diferencia,key=diferencia.get):
        return print(f"\nFelicidades!\nGanaste el juego: La figura {min(diferencia,key=diferencia.get)} tiene el área más parecida a la figura roja!",f'\n\nÁreas:\nFigura Principal: {diccionario_areas["principal"]}\nFigura a: {diccionario_areas["figura_a"]}\nFigura b: {diccionario_areas["figura_b"]}\nFigura c: {diccionario_areas["figura_c"]}')
    else: 
        return print(f"\nPerdiste!\nLa figura {min(diferencia,key=diferencia.get)} tiene el área más parecida a la figura roja. Buena suerte en la próxima vez.", f'\n\nÁreas:\nFigura Principal: {diccionario_areas["principal"]}\nFigura a: {diccionario_areas["figura_a"]}\nFigura b: {diccionario_areas["figura_b"]}\nFigura c: {diccionario_areas["figura_c"]}')    


# In[25]:


im.show()


# In[16]:


ganador()

