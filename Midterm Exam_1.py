# ---Program 1: Modify the program below by adding two conversion methods - #
# Fahrenheit to Celsius and Kelvin to Celsius (50 points)--- #

def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * (5 / 9)

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convertctk = CelsiusToKelvin(tempInCelsius)
    print(str(f"{tempInCelsius} Celsius is equivalent to {convertctk.conversion()} Kelvin"))
    convertctf = CelsiusToFahrenheit(tempInCelsius)
    print(str(f"{tempInCelsius} Celsius is equivalent to {convertctf.conversion()} Fahrenheit"))

    convertftc = FahrenheitToCelsius(convertctf.conversion())
    print(str(f"{convertctf.conversion()} Fahrenheit is equivalent to {round(convertftc.conversion(), 2)} Celsius"))

    convertftk = KelvinToCelsius(convertctk.conversion())
    print(str(f"{convertctk.conversion()} Kelvin is equivalent to {round(convertftk.conversion(), 2)} Celsius"))


# --------------Other Method---------------- #
# tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
# convert = FahrenheitToCelsius(tempInFahrenheit)
# print(str(f"{round(convert.conversion(),2)} Celsius"))

# tempInKelvin = float(input("Enter the temperature in Kelvin: "))
# convert = KelvinToCelsius(tempInKelvin)
# print(str(f"{round(convert.conversion(),2)} Celsius"))

main()