import sys

def calculate_bmi(height, weight):
    # Convert height from cm to meters
    height_meters = height / 100
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    return bmi

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
    if len(sys.argv) != 3:
        print("Usage: python calculateAndDetermineHealth.py <height_in_cm> <weight_in_kg>")
        sys.exit(1)

    try:
        height = float(sys.argv[1])
        weight = float(sys.argv[2])
    except ValueError:
        print("Error: Height and weight must be numeric values.")
        sys.exit(1)

    bmi = calculate_bmi(height, weight)
    health_state = determine_health_state(bmi)

    print(f"BMI: {bmi}")
    print(f"Health State: {health_state}")
