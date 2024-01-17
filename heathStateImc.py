# heathStateImc.py

def determine_health_state(imc):
    if imc < 18.5:
        return "Underweight"
    elif 18.5 <= imc < 25:
        return "Normal weight"
    elif 25 <= imc < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python heathStateImc.py <IMC>")
        sys.exit(1)

    imc = float(sys.argv[1])
    health_state = determine_health_state(imc)
    print(f"Health State: {health_state}")
