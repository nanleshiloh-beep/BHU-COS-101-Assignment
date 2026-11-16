
def acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time



def momentum(mass, velocity):
    return mass * velocity



def pressure(force, area):
    return force / area



def power(work_done, time):
    return work_done / time



def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2



print("PHYSICS FORMULA CALCULATOR")
print("1. Acceleration")
print("2. Momentum")
print("3. Pressure")
print("4. Power")
print("5. Kinetic Energy")

choice = int(input("Choose a formula (1-5): "))

if choice == 1:
    v = float(input("Enter final velocity: "))
    u = float(input("Enter initial velocity: "))
    t = float(input("Enter time: "))

    if t != 0:
        print("Acceleration =", acceleration(v, u, t), "m/s²")
    else:
        print("Time cannot be zero.")

elif choice == 2:
    m = float(input("Enter mass: "))
    v = float(input("Enter velocity: "))

    print("Momentum =", momentum(m, v), "kg m/s")

elif choice == 3:
    f = float(input("Enter force: "))
    a = float(input("Enter area: "))

    if a != 0:
        print("Pressure =", pressure(f, a), "Pa")
    else:
        print("Area cannot be zero.")

elif choice == 4:
    w = float(input("Enter work done: "))
    t = float(input("Enter time: "))

    if t != 0:
        print("Power =", power(w, t), "Watts")
    else:
        print("Time cannot be zero.")

elif choice == 5:
    m = float(input("Enter mass: "))
    v = float(input("Enter velocity: "))

    print("Kinetic Energy =", kinetic_energy(m, v), "Joules")

else:
    print("Invalid choice. Please select between 1 and 5.")