import sys

def calculate_bmi(height, weight):
    # Convert height from cm to meters
    height_meters = height / 100
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    return bmi

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python calculImc.py <height_in_cm> <weight_in_kg>")
        sys.exit(1)

    height = float(sys.argv[1])
    weight = float(sys.argv[2])

    bmi = calculate_bmi(height, weight)
    print(bmi)
