print (

  '''
                 *
                *  *
               *    *
              *      *
             *        *
            *          *
           *            *            
   * * * * *             * * * * *                   
   *     Ēriks Veselovs 10.a     *  
   *                             *   
   *                             *   
   * * * * *             * * * * *
           *            *
            *          *
             *        *
              *      *
               *    *
                *  *
                  *

+***********************************************+
*      Programmas uzdevumi :                    *    
|  - Taisnstūra garuma un platuma atrašana      |           *  - Laukuma atrašana                           *
*  - Lauka brīvā laukuma aprēķināšana           *           <  - Mājas un šķūņa laukuma aprēķināšana        >
|  - Lauku laukuma atrašana                     |           *                                               *
*                                               *
|                                               |
*                                               *
+************************************************+

  ''')
what = str(input ("rakstiet zvaigznīti un dariet to, ko vēlaties! (*):"))

while True:
    a= (input("\nTagad pasaki taisnstūra garumu "))
    try:
        a= float(a)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if a <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
 
    
while True:
    b= (input("\nUn tagad taisnstūra platumu "))
    try:
        b= float(b)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if b <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
  
 
if what == "*":
 c = a * b  
 print ("Rezultāts:", c)


else :
 print ("Atlasīta nepareiza operācija!") 

what = input ("Es domāju, ka tu vēl gribi, zvaigzne mums pateiks!(*):")  

a = float(input("Pasakiet taisnstūra iznākumu!.:"))
b = float(input("Cik daudz lauku mums bija?.:"))

if what =="*":
 c = a * b
 print ("Rezultāts:", c)


else :
 print ("Atlasīta nepareiza operācija!") 


what = str(input("Zvaigzne saka, ka tev ir vēlmes(*):") )


if what =="*":
 c = a * b
 print ("Rezultāts:" + (c))


else :
 print ("Atlasīta nepareiza operācija!")


what = str( input("Vai tev ir ļoti daudz vēlmju, neko nesaliekt? Bet tev ir arī vēlmes!(*):"))




while True:
    a= (input("\nNu, tad saki šķūņa garumu! "))
    try:
        a= float(a)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if a <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
 
    
while True:
    b= (input("\nUn platumu "))
    try:
        b= float(b)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if b <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
  

if what =="*":
 с = a * b
 print ("Rezultāts:" + (c))


else :
 print ("Atlasīta nepareiza operācija!")


what = str( input("Vai tu prasi plus?Ogļracis(+):"))



while True:
    a= (input("\nNosauc pirmo laukumu! "))
    try:
        a= float(a)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if a <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
 
    
while True:
    b= (input("\nNosauc otro laukumu! "))
    try:
        b= float(b)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if b <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
  


if what =="*":
 с = a * b
 print ("Rezultāts:" + c)


else :
 print ("Atlasīta nepareiza operācija!")
what = input("Tagad arī mīnus šeit uzrakstīja, varbūt vēl cto-to padarīt, vai ne?(-)")



while True:
    a= (input("\nNosauc lauku laukumu "))
    try:
        a= float(a)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if a <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
 
    
while True:
    b= (input("\nTagad pasaki mājas laukumu un šķūni kopā "))
    try:
        b= float(b)
    except:
        print('\nIevadiet korekto daudzumu!')
        continue
    if b <= 0:
        print('\nIevadiet korekto daudzumu!')
        continue
    break
  

if what =="*":
 с = a * b
 print ("Rezultāts:" + c)


else :
 print ("Atlasīta nepareiza operācija!")