from datetime import datetime

def kg_from_lb(w):
    w = w * 0.45359237
    return w

def cm_from_in(h):
    h = h * 2.54
    return h

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years

def body_mass_index(weight, height):
    bmi = ( 10000 * weight ) / (height * height)
    return bmi
    
def bmr_calculator(sex, weight, height, age):
    sex = sex.strip(" .,?abcdeghijklnopqrstuvwxyz")
    print(f"SEX IS: {sex}")
    if sex.lower() == "m":
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
    return bmr
        

def main():
    sex = input("Enter gender M/F: ").lower()
    birth_str = input("Enter birthdate (YYYY-MM-DD): ")
    weight = float(input("Enter weight in lbs: "))
    height = float(input("Enter height in in: "))
    # sex = "f"
    # birth_str = "2003-3-21"
    # weight = 125
    # height = 54
    print(f"Age (years): {compute_age(birth_str)}")
    print(f"Weight (kg): {kg_from_lb(weight):.2f}")
    print(f"Height (cm): {cm_from_in(height):.1f}")
    print(f"Body mass index (BMI): {body_mass_index(kg_from_lb(weight), cm_from_in(height)):.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr_calculator(sex, kg_from_lb(weight), cm_from_in(height), compute_age(birth_str))}")

    pass

main()