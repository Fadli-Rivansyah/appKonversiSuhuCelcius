# app konversi suhu
#rumus ========> 
#celcius -> fahrenheit = (9/5)*celcius+32
#celcius -> reamur = (4/5)*celcius
#celcius -> kelvin = celcius+273.15
#celcius -> rankie = (celcius+273.15)*9/5
# ==============

print("==== KONVERSI SUHU ====")
celcius = float(input("Masukan Celciusnya = "))
print("Celcius kamu ",celcius)

fahrenheit = (9/5) * celcius + 32  #rumus celcius->fahrenheit
reamur = (4/5) * celcius  #rumus celcius->reamur
kelvin = celcius + 273.15  #rumus celcius->kelvin

print("==========================")
print("suhu fahrenhiet = ",fahrenheit,"R")
print("suhu reamur = ", reamur, "R")
print("suhu kelvin = ", kelvin, "K")

