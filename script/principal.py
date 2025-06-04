# bibliotecas
import tkinter, math, numpy, os
import matplotlib
import matplotlib.pyplot as aux_pyplot

matplotlib.use("TkAgg")

# variáveis globais
global toOnde
global m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m, RP3_a, FP4_m, FP4_a, RP4_m, RP4_a, FP2_m, FP2_a, RP2_m, RP2_a, T2
global O2A, AB, BO4, O2O4, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m, Rg2_a, Rg3_m, Rg3_a, Rg4_m, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a

toOnde = [] 
toOnde.append("main")
m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m, RP3_a, FP4_m, FP4_a, RP4_m, RP4_a, FP2_m, FP2_a, RP2_m, RP2_a, T2, O2A, AB, BO4, O2O4, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m, Rg2_a, Rg3_m, Rg3_a, Rg4_m, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a = 0.35,	3.5, 17.51,	0.011,	0.023,	0.056,	-1.69,	2.82, 42.96, 0,	0,	0, 177.93, -30,	203.2,	0,	0,	0,	0,	0,	0,	101.6,	304.8,	203.2,	381, 45, 24.97,	99.3, 20, 75.29, 244.4, 20,	-5.62,	3.56, 50.8,	0, 127,	0, 101.6, 30, 20.35, 222.14, 42.96, 208.24, 24.87, 222.27


# > funções
def f_grau2rad(angulo):
    return (angulo * math.pi/180)


def f_rad2grau(angulo):
    return (angulo * 180 / math.pi)


def f_decompoeXY(modulo, angulo):
    'Convertendo para radiano'
    angulo = f_grau2rad(angulo)
    
    'Componente x'
    componenteX = modulo * math.cos(angulo)
    'Componente y'
    componenteY = modulo * math.sin(angulo)
    
    return componenteX, componenteY


def f_compoeBarra(cateto0, cateto1a, cateto1b, anguloG):
    angulo = f_grau2rad(anguloG)
    
    moduloBarra = math.sqrt((cateto0 * math.sin(angulo))**2 + (cateto1a - cateto1b * math.cos(angulo))**2);
    anguloBarra = math.atan2(cateto0 * math.sin(angulo), cateto1a - cateto1b * math.cos(angulo));
    
    anguloBarra = f_rad2grau(anguloBarra)
    
    return moduloBarra, anguloBarra


def f_leDados(quais):
    if quais == "dadosCinematicos":
        " comprimento dos braços (cadeia cinemática) "
        O2A = float(caixaO2A.get()); # mm
        AB = float(caixaAB.get()); # mm
        BO4 = float(caixaBO4.get()); # mm
        O2O4 = float(caixaO2O4.get()); # mmm
         
        ' ângulo entre sistema global e braço da cadeia cinemática'
        theta2 = float(caixaTheta2.get()); # graus    
        theta3 = float(caixaTheta3.get()); # graus    
        theta4 = float(caixaTheta4.get()); # graus   
         
        ' acelerações angulares dos componentes'
        alfa2 = float(caixaAlfa2.get()); # rad/s²    
        alfa3 = float(caixaAlfa3.get()); # rad/s²  
        alfa4 = float(caixaAlfa4.get()); # rad/s²    
        
        ' velocidades angulares dos componentes'
        omega2 = float(caixaOmega2.get()); # rad/s    
        omega3 = float(caixaOmega3.get()); # rad/s  
        omega4 = float(caixaOmega4.get()); # rad/s    
        
        ' braços para achar o CG de cada componente. *Uso apenas para achar CG*'
        Rg2_m = float(caixaRG2_m.get()); # mm
        Rg2_a = float(caixaRG2_a.get()); # graus -> delta2
        Rg3_m = float(caixaRG3_m.get()); # mm
        Rg3_a = float(caixaRG3_a.get()); # graus -> delta3
        Rg4_m = float(caixaRG4_m.get()); # mm
        Rg4_a = float(caixaRG4_a.get()); # graus -> delta4
        
        ' aceleração de cada componente (no CG)'
        ag2_m = float(caixaAG2_m.get()); # m/s²
        ag2_a = float(caixaAG2_a.get()); # graus
        ag3_m = float(caixaAG3_m.get()); # m/s²
        ag3_a = float(caixaAG3_a.get()); # graus
        ag4_m = float(caixaAG4_m.get()); # m/s²
        ag4_a = float(caixaAG4_a.get()); # graus
        
        return O2A, AB, BO4, O2O4, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m, Rg2_a, Rg3_m, Rg3_a, Rg4_m, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a
        
    if quais == "dadosDinamicos":        
        ' massas dos componentes'
        m2 = float(caixaM2.get()); # kg    
        m3 = float(caixaM3.get()); # kg 
        m4 = float(caixaM4.get()); # kg 
        
        ' inércia dos componentes'
        I2 = float(caixaI2.get()); # kg.m²    
        I3 = float(caixaI3.get()); # kg.m² 
        I4 = float(caixaI4.get()); # kg.m²    
        
        ' torques'
        T2 = float(caixaT2.get()); # N.m
        T3 = float(caixaT3.get()); # N.m
        T4 = float(caixaT4.get()); # N.m
        
        ' forças aplicadas nos componentes e raios desssas forças aos respectivos CGs'
        FP2_m = float(caixaF2_m.get()); # N
        FP2_a = float(caixaF2_a.get()); # graus
        RP2_m = float(caixaRP2_m.get()); # mm
        RP2_a = float(caixaRP2_a.get()); # graus
        FP3_m = float(caixaF3_m.get()); # N
        FP3_a = float(caixaF3_a.get()); # graus
        RP3_m = float(caixaRP3_m.get()); # mm
        RP3_a = float(caixaRP3_a.get()); # graus
        FP4_m = float(caixaF4_m.get()); # N
        FP4_a = float(caixaF4_a.get()); # graus
        RP4_m = float(caixaRP4_m.get()); # mm
        RP4_a = float(caixaRP4_a.get()); # graus
        
        return m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m, RP3_a, FP4_m, FP4_a, RP4_m, RP4_a, FP2_m, FP2_a, RP2_m, RP2_a, T2


def f_printaResultados(forcasTorque):
    # F12x
    variavel = round(forcasTorque[0], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 242, y = 175, height = 23, width = 60)
    
    # F12y
    variavel = round(forcasTorque[1], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 345, y = 176, height = 23, width = 60)
    
    # F12
    variavel = round(math.sqrt(forcasTorque[0]**2 + forcasTorque[1]**2), 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 471, y = 176, height = 23, width = 60)
    
    # F14x
    variavel = round(forcasTorque[2], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 733, y = 175, height = 23, width = 60)
    
    # F14y
    variavel = round(forcasTorque[3], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 836, y = 175, height = 23, width = 60)
    
    # F14
    variavel = round(math.sqrt(forcasTorque[2]**2 + forcasTorque[3]**2), 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 961, y = 177, height = 23, width = 60)
    
    # F32x
    variavel = round(forcasTorque[4], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 243, y = 271, height = 23, width = 60)
    
    # F32y
    variavel = round(forcasTorque[5], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 344, y = 271, height = 23, width = 60)
    
    # F32
    variavel = round(math.sqrt(forcasTorque[4]**2 + forcasTorque[5]**2), 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 469, y = 272, height = 23, width = 60)
    
    # F43x
    variavel = round(forcasTorque[6], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 733, y = 272, height = 23, width = 60)
    
    # F43y
    variavel = round(forcasTorque[7], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 836, y = 271, height = 23, width = 60)
    
    # F43
    variavel = round(math.sqrt(forcasTorque[6]**2 + forcasTorque[7]**2), 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 961, y = 273, height = 23, width = 60)
    
    # T12
    variavel = round(forcasTorque[8], 2)
    textoSaidaCAIXA = tkinter.Label(janelaPrincipal, text = str(variavel), font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat")
    textoSaidaCAIXA.place(x = 554, y = 345, height = 23, width = 60)
  
     
def f_mostraCaixas(quais):
    # caixas de input dos dados cinemáticos
    if quais == "dadosCinematicos":   
        global caixaRG2_m, caixaRG2_a, caixaRG3_m, caixaRG3_a, caixaRG4_m, caixaRG4_a, caixaAG2_m, caixaAG2_a, caixaAG3_m, caixaAG3_a, caixaAG4_m, caixaAG4_a, caixaO2A, caixaAB, caixaBO4, caixaO2O4, caixaOmega2, caixaAlfa2, caixaOmega3, caixaAlfa3, caixaOmega4, caixaAlfa4, caixaTheta2, caixaTheta3, caixaTheta4      
        caixaRG2_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRG2_m.place(x = 86, y = 500, height= 23, width = 60)
        caixaRG2_m.insert(0, Rg2_m)
        caixaRG2_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRG2_a.place(x = 86, y = 535, height= 23, width = 60)
        caixaRG2_a.insert(0, Rg2_a)
        caixaRG3_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRG3_m.place(x = 240, y = 500, height= 23, width = 60)
        caixaRG3_m.insert(0, Rg3_m)
        caixaRG3_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRG3_a.place(x = 240, y = 535, height= 23, width = 60)
        caixaRG3_a.insert(0, Rg3_a)
        caixaRG4_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRG4_m.place(x = 398, y = 500, height= 23, width = 60)
        caixaRG4_m.insert(0, Rg4_m)
        caixaRG4_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRG4_a.place(x = 398, y = 535, height= 23, width = 60)
        caixaRG4_a.insert(0, Rg4_a)
        caixaAG2_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAG2_m.place(x = 564, y = 500, height= 23, width = 60)
        caixaAG2_m.insert(0, ag2_m)
        caixaAG2_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAG2_a.place(x = 564, y = 535, height= 23, width = 60)
        caixaAG2_a.insert(0, ag2_a)
        caixaAG3_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAG3_m.place(x = 721, y = 500, height= 23, width = 60)
        caixaAG3_m.insert(0, ag3_m)
        caixaAG3_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAG3_a.place(x = 721, y = 535, height= 23, width = 60)
        caixaAG3_a.insert(0, ag3_a)
        caixaAG4_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAG4_m.place(x = 876, y = 500, height= 23, width = 60)
        caixaAG4_m.insert(0, ag4_m)
        caixaAG4_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAG4_a.place(x = 876, y = 535, height= 23, width = 60)
        caixaAG4_a.insert(0, ag4_a)
        
        caixaO2A = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaO2A.place(x = 1010, y = 18, height= 23, width = 60)
        caixaO2A.insert(0, O2A)
        caixaAB = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAB.place(x = 1010, y = 57, height= 23, width = 60)
        caixaAB.insert(0, AB)
        caixaBO4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaBO4.place(x = 1010, y = 95, height= 23, width = 60)
        caixaBO4.insert(0, BO4)
        caixaO2O4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaO2O4.place(x = 1010, y = 128, height= 23, width = 60)
        caixaO2O4.insert(0, O2O4)
        
        caixaOmega2 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaOmega2.place(x = 160, y = 313, height= 23, width = 60)
        caixaOmega2.insert(0, omega2)
        caixaAlfa2 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAlfa2.place(x = 160, y = 348, height= 23, width = 60)
        caixaAlfa2.insert(0, alfa2)
        
        caixaOmega3 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaOmega3.place(x = 543, y = 143, height= 23, width = 60)
        caixaOmega3.insert(0, omega3)
        caixaAlfa3 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAlfa3.place(x = 543, y = 180, height= 23, width = 60)
        caixaAlfa3.insert(0, alfa3)
        
        caixaOmega4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaOmega4.place(x = 890, y = 267, height= 23, width = 60)
        caixaOmega4.insert(0, omega4)
        caixaAlfa4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaAlfa4.place(x = 890, y = 299, height= 23, width = 60)
        caixaAlfa4.insert(0, alfa4)
        
        caixaTheta2 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaTheta2.place(x = 410, y = 373, height= 23, width = 60)
        caixaTheta2.insert(0, theta2)
        caixaTheta3 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaTheta3.place(x = 640, y = 275, height= 23, width = 60)
        caixaTheta3.insert(0, theta3)
        caixaTheta4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaTheta4.place(x = 972, y = 372, height= 23, width = 60)
        caixaTheta4.insert(0, theta4)
       
        
    # caixas de input dos dados dinâmicos
    if quais == "dadosDinamicos":
        global caixaM2, caixaI2, caixaI2, caixaT2, caixaM3, caixaI3, caixaT3, caixaM4, caixaI4, caixaT4, caixaRP2_m, caixaRP2_a, caixaRP3_m, caixaRP3_a, caixaRP4_m, caixaRP4_a, caixaF2_m, caixaF2_a, caixaF3_m, caixaF3_a, caixaF4_m, caixaF4_a      
        caixaM2 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaM2.place(x = 160, y = 313, height= 23, width = 60)
        caixaM2.insert(0, m2)
        caixaI2 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaI2.place(x = 160, y = 348, height= 23, width = 60)
        caixaI2.insert(0, I2)
        caixaT2 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaT2.place(x = 160, y = 382, height= 23, width = 60)
        caixaT2.insert(0, T2)
        caixaM3 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaM3.place(x = 566, y = 169, height= 23, width = 60)
        caixaM3.insert(0, m3)
        caixaI3 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaI3.place(x = 566, y = 203, height= 23, width = 60)
        caixaI3.insert(0, I3)
        caixaT3 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaT3.place(x = 566, y = 238, height= 23, width = 60)
        caixaT3.insert(0, T3)
        caixaM4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaM4.place(x = 916, y = 276, height= 23, width = 60)
        caixaM4.insert(0, m4)
        caixaI4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaI4.place(x = 916, y = 310, height= 23, width = 60)
        caixaI4.insert(0, I4)
        caixaT4 = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaT4.place(x = 916, y = 347, height= 23, width = 60)
        caixaT4.insert(0, T4)
        
        caixaRP2_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRP2_m.place(x = 160, y = 501, height= 23, width = 60)
        caixaRP2_m.insert(0, RP2_m)
        caixaRP2_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRP2_a.place(x = 160, y = 536, height= 23, width = 60)
        caixaRP2_a.insert(0, RP2_a)
        caixaRP3_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRP3_m.place(x = 361, y = 502, height= 23, width = 60)
        caixaRP3_m.insert(0, RP3_m)
        caixaRP3_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRP3_a.place(x = 361, y = 535, height= 23, width = 60)
        caixaRP3_a.insert(0, RP3_a)
        caixaRP4_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRP4_m.place(x = 566, y = 500, height= 23, width = 60)
        caixaRP4_m.insert(0, RP4_m)
        caixaRP4_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaRP4_a.place(x = 566, y = 533, height= 23, width = 60)  
        caixaRP4_a.insert(0, RP4_a)  
        
        caixaF2_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaF2_m.place(x = 1010, y = 19, height= 23, width = 60)
        caixaF2_m.insert(0, FP2_m)
        caixaF2_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaF2_a.place(x = 1010, y = 56, height= 23, width = 60)
        caixaF2_a.insert(0, FP2_a)
        caixaF3_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaF3_m.place(x = 731, y = 45, height= 23, width = 60)
        caixaF3_m.insert(0, FP3_m)
        caixaF3_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaF3_a.place(x = 708, y = 90, height= 23, width = 60)
        caixaF3_a.insert(0, FP3_a)
        caixaF4_m = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaF4_m.place(x = 1010, y = 90, height= 23, width = 60)
        caixaF4_m.insert(0, FP4_m)
        caixaF4_a = tkinter.Entry(janelaPrincipal, font = ("comfortaa", 12), justify="right", background="#1e3e58", foreground = "#c2c3c2", relief= "flat", insertbackground = "#91c344") 
        caixaF4_a.place(x = 1010, y = 126, height= 23, width = 60)
        caixaF4_a.insert(0, FP4_a)


def f_calculaDinamica(O2A, AB, BO4, O2O4, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m, Rg2_a, Rg3_m, Rg3_a, Rg4_m, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a, m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m, RP3_a, FP4_m, FP4_a, RP4_m, RP4_a, FP2_m, FP2_a, RP2_m, RP2_a, T2):
    
    '> decompondo acelerações [m/s²] e forças externas [N]'
    
    [ag2_x, ag2_y] = f_decompoeXY(ag2_m, ag2_a) # [m/s²]
    [ag3_x, ag3_y] = f_decompoeXY(ag3_m, ag3_a) # [m/s²]
    [ag4_x, ag4_y] = f_decompoeXY(ag4_m, ag4_a) # [m/s²]
    [FP2_x, FP2_y] = f_decompoeXY(FP2_m, FP2_a) # [N]
    [FP3_x, FP3_y] = f_decompoeXY(FP3_m, FP3_a) # [N]
    [FP4_x, FP4_y] = f_decompoeXY(FP4_m, FP4_a) # [N]
    
        
    '> decompondo componentes de raio [m]'
    '>> raio das forças aplicadas'
    '>>> barra 2'
    [RP2_x, RP2_y] = f_decompoeXY(RP2_m, theta2 + RP2_a) # [m]
        
    '>>> barra 3'
    [RP3_x, RP3_y] = f_decompoeXY(RP3_m, theta3 + RP3_a) # [m]
    
    '>>> barra 4'
    [RP4_x, RP4_y] = f_decompoeXY(RP4_m, theta4 + RP4_a) # [m]
    
    '>> raio das barras'
    '>>> barra 2'
    [R12x, R12y] = f_decompoeXY(Rg2_m, theta2 + Rg2_a + 180) # [m]
    [R32_m, R32_a] = f_compoeBarra(Rg2_m, O2A, Rg2_m, Rg2_a) # [m], [grau]
    [R32x, R32y] = f_decompoeXY(R32_m, theta2 - R32_a) # [m]
        
    '>>> barra 3'
    [R23x, R23y] = f_decompoeXY(Rg3_m, theta3 + Rg3_a + 180) # [m]
    [R43_m, R43_a] = f_compoeBarra(Rg3_m, AB, Rg3_m, Rg3_a) # [m], [grau]
    [R43x, R43y] = f_decompoeXY(R43_m, theta3 - R43_a) # [m]
    
    '>>> barra 4'
    [R14x, R14y] = f_decompoeXY(Rg4_m, theta4 + Rg4_a + 180) # [m]
    [R34_m, R34_a] = f_compoeBarra(Rg4_m, BO4, Rg4_m, Rg4_a) # [m], [grau]
    [R34x, R34y] = f_decompoeXY(R34_m, theta4 - R34_a) # [m]
    
    '> Montando matrizes e resolvendo sistema linear'
    A = [[1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 1, 0, 0, 0, 0, 0],
         [-R12y, R12x, -R32y, R32x, 0, 0, 0, 0, 1], 
         [0, 0, -1, 0, 1, 0, 0, 0, 0], 
         [0, 0, 0, -1, 0, 1, 0, 0, 0], 
         [0, 0, R23y, -R23x, -R43y, R43x, 0, 0, 0],
         [0, 0, 0, 0, -1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, -1, 0, 1, 0],
         [0, 0, 0, 0, R34y, -R34x, -R14y, R14x, 0]]
        
    b = [m2 * ag2_x - FP2_x,
         m2 * ag2_y - FP2_y,
         I2 * alfa2 - T2 - RP2_x * FP2_y + RP2_y * FP2_x,
         m3 * ag3_x - FP3_x,
         m3 * ag3_y - FP3_y,
         I3 * alfa3 - T3 - RP3_x * FP3_y + RP3_y * FP3_x,
         m4 * ag4_x - FP4_x,
         m4 * ag4_y - FP4_y,
         I4 * alfa4 - T4 - RP4_x * FP4_y + RP4_y * FP4_x]
        
    x = numpy.linalg.inv(A).dot(b)
        
    return x


def meLocaliza(agora):
    toOnde.clear()
    toOnde.append(agora)
    

def plotaGraficos():
    
    # Cálculos
    '> CINEMÁTICA: Pelo capítulo 04 do Norton, página 202, gráficos de deslocamentos'
    '>> pelas equações 4.8 a 4.13 (para thetas), 6.18 (para ômegas) e 7.12 (para alfas),'
    g_K1 = O2O4 / O2A;
    g_K2 = O2O4 / BO4;
    g_K3 = (O2A ** 2 - AB ** 2 + BO4 ** 2 + O2O4 ** 2) / (2 * O2A * BO4);
    g_K4 = O2O4 / AB;
    g_K5 = (-O2A ** 2 - AB ** 2 + BO4 ** 2 - O2O4 ** 2) / (2 * O2A * AB);
   
    '>> calculando termos a cada variação de theta2'
    g_theta2 = numpy.arange(0, 2 * math.pi , .1) # rad
    g_A = []
    g_B = []
    g_C = []
    g_D = []
    g_E = []
    g_F = []
    g_AA = []
    g_BB = []
    g_CC = []
    g_DD = []
    g_EE = []
    g_FF = []
    g_theta3 = []
    g_theta4 = []
    
    g_omega3 = []
    g_omega4 =[]
        
    g_alfa3 = []
    g_alfa4 =[]
    
    
    for indice in range(len(g_theta2)):
        # velocidade angular [rad/s]
        g_D.append(math.cos(g_theta2[indice]) - g_K1 + g_K4 * math.cos(g_theta2[indice]) + g_K5)
        g_E.append(-2 * math.sin(g_theta2[indice]))
        g_F.append(g_K1 + (g_K4 - 1) * math.cos(g_theta2[indice]) + g_K5)
        g_theta3.append(2 * math.atan((-g_E[indice] - math.sqrt( g_E[indice] ** 2 - 4 * g_D[indice] * g_F[indice])) / (2 * g_D[indice]) ) ) # [rad] 
        g_A.append(math.cos(g_theta2[indice]) - g_K1 - g_K2 * math.cos(g_theta2[indice]) + g_K3)
        g_B.append(-2 * math.sin(g_theta2[indice]))
        g_C.append(g_K1 - (g_K2 + 1) * math.cos(g_theta2[indice]) + g_K3)
        g_theta4.append(2 * math.atan((-g_B[indice] - math.sqrt( g_B[indice] ** 2 - 4 * g_A[indice] * g_C[indice])) / (2 * g_A[indice]) ) ) # [rad] 
        
        g_omega3.append((O2A * omega2 * math.sin(g_theta4[indice] - g_theta2[indice])) / (AB * omega2 * math.sin(g_theta3[indice] - g_theta4[indice])) ) 
        g_omega4.append((O2A * omega2 * math.sin(g_theta2[indice] - g_theta3[indice])) / (BO4 * omega2 * math.sin(g_theta4[indice] - g_theta3[indice])) )
        
        
        # aceleração angular [rad/s²]
        g_AA.append(BO4 * math.sin(g_theta4[indice]))
        g_BB.append(AB * math.sin(g_theta3[indice]))
        g_CC.append(O2A * alfa2 * math.sin(g_theta2[indice]) + O2A * omega2 ** 2 * math.cos(g_theta2[indice]) + AB * g_omega3[indice] ** 2 * math.cos(g_theta3[indice]) - BO4 * g_omega4[indice] ** 2 * math.cos(g_theta4[indice]))
        g_DD.append(BO4 * math.cos(g_theta4[indice]))
        g_EE.append(AB * math.cos(g_theta3[indice]))
        g_FF.append(O2A * alfa2 * math.cos(g_theta2[indice]) - O2A * omega2 ** 2 * math.sin(g_theta2[indice]) - AB * g_omega3[indice] ** 2 * math.sin(g_theta3[indice]) + BO4 * g_omega4[indice] ** 2 * math.sin(g_theta4[indice]))
        
        g_alfa3.append((g_CC[indice] * g_DD[indice] - g_AA[indice] * g_FF[indice]) / (g_AA[indice] * g_EE[indice] - g_BB[indice] * g_DD[indice])) 
        g_alfa4.append((g_CC[indice] * g_EE[indice] - g_BB[indice] * g_FF[indice]) / (g_AA[indice] * g_EE[indice] - g_BB[indice] * g_DD[indice])) 
        
        
        # transformando thetas de [rad] para [grau]
        g_theta2[indice] = f_rad2grau(g_theta2[indice]) # [graus]
        g_theta3[indice] = f_rad2grau(g_theta3[indice]) # [graus]
        g_theta4[indice] = f_rad2grau(g_theta4[indice]) # [graus]
        
        
        
    #plt.plot(g_theta2, g_omega3, g_theta2, g_omega4)
    #plt.plot(g_theta2, g_alfa3, g_theta2, g_alfa4)
    
    

    '>> plotando '
    aux_pyplot.rcParams['axes.facecolor'] = '#1e3e58'
    
    # theta
    figura1 = matplotlib.figure.Figure(figsize=(3.1, 2.7), dpi=100, facecolor = "#1e3e58", edgecolor = "#1e3e58")
    grafico1 = figura1.add_subplot(1, 1, 1)
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figura1, janelaPrincipal)
    canvas.get_tk_widget().grid(row=8, column=8)
    canvas.get_tk_widget().place(x = 58, y = 100)
    
    grafico1.grid(color = "#a3a9ae", alpha = 0.3)
    grafico1.spines['bottom'].set_color("#a3a9ae")
    grafico1.spines['left'].set_color("#a3a9ae")
    grafico1.spines['top'].set_color("#a3a9ae")
    grafico1.spines['right'].set_color("#a3a9ae")
    grafico1.tick_params(axis='x', colors="#a3a9ae")
    grafico1.tick_params(axis='y', colors="#a3a9ae")
    
    grafico1.plot(g_theta2, g_theta4, color="#e8b948",  linewidth = 2)
    grafico1.plot(g_theta2, g_theta3, color="#6d9847",  linewidth = 2)
    
    
    # omega
    figura2 = matplotlib.figure.Figure(figsize=(3.1, 2.7), dpi=100, facecolor = "#1e3e58", edgecolor = "#1e3e58")
    grafico2 = figura2.add_subplot(1, 1, 1)
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figura2, janelaPrincipal)
    canvas.get_tk_widget().grid(row=8, column=8)
    canvas.get_tk_widget().place(x = 420, y = 100)
    
    grafico2.grid(color = "#a3a9ae", alpha = 0.3)
    grafico2.spines['bottom'].set_color("#a3a9ae")
    grafico2.spines['left'].set_color("#a3a9ae")
    grafico2.spines['top'].set_color("#a3a9ae")
    grafico2.spines['right'].set_color("#a3a9ae")
    grafico2.tick_params(axis='x', colors="#a3a9ae")
    grafico2.tick_params(axis='y', colors="#a3a9ae")
    
    grafico2.plot(g_theta2, g_omega3, color="#e8b948",  linewidth = 2)
    grafico2.plot(g_theta2, g_omega4, color="#6d9847",  linewidth = 2)
    
    
    # alfa
    figura3 = matplotlib.figure.Figure(figsize=(3.1, 2.7), dpi=100, facecolor = "#1e3e58", edgecolor = "#1e3e58")
    grafico3 = figura3.add_subplot(1, 1, 1)
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figura3, janelaPrincipal)
    canvas.get_tk_widget().grid(row=8, column=8)
    canvas.get_tk_widget().place(x = 780, y = 100)
    
    grafico3.grid(color = "#a3a9ae", alpha = 0.3)
    grafico3.spines['bottom'].set_color("#a3a9ae")
    grafico3.spines['left'].set_color("#a3a9ae")
    grafico3.spines['top'].set_color("#a3a9ae")
    grafico3.spines['right'].set_color("#a3a9ae")
    grafico3.tick_params(axis='x', colors="#a3a9ae")
    grafico3.tick_params(axis='y', colors="#a3a9ae")
    
    grafico3.plot(g_theta2, g_alfa3, color="#e8b948",  linewidth = 2)
    grafico3.plot(g_theta2, g_alfa4, color="#6d9847",  linewidth = 2)
    
    
def mainClique(eventorigin):
    x0 = eventorigin.x
    y0 = eventorigin.y
    #print(toOnde)
    #print(toOnde)
    
    # quando na tela inicial
    if(toOnde[0] == "main"):
        # start
        if(x0 >= 830 and x0 <= 1010 and y0 >= 510 and y0 <= 547):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg1_arquivo)
            backgroundLabel.place(x=0, y=0)
            meLocaliza("dadosCinematicos")
            f_mostraCaixas("dadosCinematicos")
        
    # quando na primeira tela de entrada de dados (dados cinemáticos)
    elif(toOnde[0] == "dadosCinematicos"):
        # saída para main
        if(x0 >= 1048 and x0 <= 1100 and y0 >= 490 and y0 <= 556):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg0_arquivo)
            backgroundLabel.place(x=0, y=0)  
            
            meLocaliza("main")
            
        # próxima página (dados dinâmicos)
        if(x0 >= 1085 and x0 <= 1107 and y0 >= 452 and y0 <= 478):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg2_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            
            # lendo dados cinemáticos
            global O2A, AB, BO4, O2O4, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m, Rg2_a, Rg3_m, Rg3_a, Rg4_m, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a
            [O2A, AB, BO4, O2O4, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m, Rg2_a, Rg3_m, Rg3_a, Rg4_m, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a] = f_leDados("dadosCinematicos")
            
            
            
            f_mostraCaixas("dadosDinamicos")
            meLocaliza("dadosDinamicos")
            
            
    # quando na segunda tela de entrada de dados (dados dinâmicos)
    elif(toOnde[0] == "dadosDinamicos"):
        # saída para main
        if(x0 >= 1048 and x0 <= 1100 and y0 >= 490 and y0 <= 556):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg0_arquivo)
            backgroundLabel.place(x=0, y=0)  
            
            meLocaliza("main")
            
        # página anterior (dados cinemáticos)
        if(x0 >= 1045 and x0 <= 1073 and y0 >= 451 and y0 <= 477):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg1_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            meLocaliza("dadosCinematicos")
            f_mostraCaixas("dadosCinematicos")
            
        # próxima página (resultados)
        if(x0 >= 1085 and x0 <= 1107 and y0 >= 452 and y0 <= 478):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg3_arquivo)
            backgroundLabel.place(x=0, y=0)
            
             # lendo dados dinâmicos
            global m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m, RP3_a, FP4_m, FP4_a, RP4_m, RP4_a, FP2_m, FP2_a, RP2_m, RP2_a, T2
            [m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m, RP3_a, FP4_m, FP4_a, RP4_m, RP4_a, FP2_m, FP2_a, RP2_m, RP2_a, T2] = f_leDados("dadosDinamicos")
            
            auxx = f_calculaDinamica(O2A / 1E3, AB / 1E3, BO4 / 1E3, O2O4 / 1E3, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m / 1E3, Rg2_a, Rg3_m / 1E3, Rg3_a, Rg4_m / 1E3, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a, m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m / 1E3, RP3_a, FP4_m, FP4_a, RP4_m / 1E3, RP4_a, FP2_m, FP2_a, RP2_m / 1E3, RP2_a, T2)
            
            
            meLocaliza("resultados0")
             
            
    # quando na primeira tela de resultados (dinâmica)
    elif(toOnde[0] == "resultados0"):
        # saída para main
        if(x0 >= 1048 and x0 <= 1100 and y0 >= 490 and y0 <= 556):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg0_arquivo)
            backgroundLabel.place(x=0, y=0) 
            
            meLocaliza("main")
            
        # página anterior (dados dinâmicos)
        if(x0 >= 1045 and x0 <= 1073 and y0 >= 451 and y0 <= 477):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg2_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            meLocaliza("dadosDinamicos")
            
            f_mostraCaixas("dadosDinamicos")
            
        # próxima página (resultados)
        if(x0 >= 1085 and x0 <= 1107 and y0 >= 452 and y0 <= 478):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg4_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            # realizando gráficos
            # f_fazGraficos()
            plotaGraficos()
            meLocaliza("resultados1")
            
        # realiza cálculos e plota (resultados)
        if(x0 >= 740 and x0 <= 920 and y0 >= 490 and y0 <= 527):
            # realizando cálculos dinâmicos
            global forcasTorque
            
            forcasTorque = f_calculaDinamica(O2A / 1E3, AB / 1E3, BO4 / 1E3, O2O4 / 1E3, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m / 1E3, Rg2_a, Rg3_m / 1E3, Rg3_a, Rg4_m / 1E3, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a, m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m / 1E3, RP3_a, FP4_m, FP4_a, RP4_m / 1E3, RP4_a, FP2_m, FP2_a, RP2_m / 1E3, RP2_a, T2)
            # %
            f_printaResultados(forcasTorque)
            
    
    # quando na segunda tela de resultados (primeira de gráficos, cinemática)
    elif(toOnde[0] == "resultados1"):
        # saída para main
        if(x0 >= 1048 and x0 <= 1100 and y0 >= 490 and y0 <= 556):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg0_arquivo)
            backgroundLabel.place(x=0, y=0) 
            
            meLocaliza("main")
            
        # página anterior (resultados dinâmicos)
        if(x0 >= 1045 and x0 <= 1073 and y0 >= 451 and y0 <= 477):
            backgroundLabel = tkinter.Label(janelaPrincipal, image = bg3_arquivo)
            backgroundLabel.place(x=0, y=0)
            
            # mostrando resultados dinâmicos 
            forcasTorque = f_calculaDinamica(O2A / 1E3, AB / 1E3, BO4 / 1E3, O2O4 / 1E3, theta2, theta3, theta4, alfa2, alfa3, alfa4, omega2, omega3, omega4, Rg2_m / 1E3, Rg2_a, Rg3_m / 1E3, Rg3_a, Rg4_m / 1E3, Rg4_a, ag2_m, ag2_a, ag3_m, ag3_a, ag4_m, ag4_a, m2, m3, m4, I2, I3, I4, T3, T4, FP3_m, FP3_a, RP3_m / 1E3, RP3_a, FP4_m, FP4_a, RP4_m / 1E3, RP4_a, FP2_m, FP2_a, RP2_m / 1E3, RP2_a, T2)
            f_printaResultados(forcasTorque)
            
            meLocaliza("resultados0")
     
               
"""_______________________________________________________'

> main """
# > definições iniciais importantes
pastaAtual = os.path.dirname(os.path.realpath(__file__))
auxDiretorioPROJETO = pastaAtual.split('script')
caminhoBackground = str(auxDiretorioPROJETO[0]) + 'layout\\' + '/'

# > imagens dos backgrounds
bg0 = caminhoBackground + '0.png'
bg1 = caminhoBackground + '1.png'
bg2 = caminhoBackground + '2.png'
bg3 = caminhoBackground + '3.png'
bg4 = caminhoBackground + '4.png'

# > criação da janela
global janelaPrincipal
janelaPrincipal = tkinter.Tk()
janelaPrincipal.geometry('1120x573')
janelaPrincipal.title('4barras solver | solução de mecanismos de 4 barras')
janelaPrincipal.resizable(False, False)
# janelaPrincipal.attributes("-alpha", .75)

# linkando backgrounds
bg0_arquivo = tkinter.PhotoImage(file = bg0)
bg1_arquivo = tkinter.PhotoImage(file = bg1)
bg2_arquivo = tkinter.PhotoImage(file = bg2)
bg3_arquivo = tkinter.PhotoImage(file = bg3)
bg0_arquivo = tkinter.PhotoImage(file = bg0)
bg4_arquivo = tkinter.PhotoImage(file = bg4)

# setando background
backgroundLabel = tkinter.Label(janelaPrincipal, image = bg0_arquivo)
backgroundLabel.place(x=0, y=0)

# >>> cliques
janelaPrincipal.bind("<Button 1>", mainClique)

janelaPrincipal.mainloop()
# <<fim  início de loop da janela principal
