import random
import math

size = 50
step = 1.0
amplitude = 0.2


hill_center_x = 20
hill_center_z = 10
hill_radius = 12
hill_height = 6.0

with open("ground3.obj", "w") as f:
    f.write("# Pofalowana płaszczyzna 50x50 z górką\n")

    for z in range(size + 1):
        for x in range(size + 1):
            px = -size / 2 + x * step
            pz = -size / 2 + z * step
            py = random.uniform(-amplitude, amplitude)

            local_x = x
            local_z = z

            dist = math.sqrt((local_x - hill_center_x) ** 2 + (local_z - hill_center_z) ** 2)


            if dist < hill_radius:
                height = hill_height * (1 - dist / hill_radius)
                py += height

            f.write(f"v {px:.2f} {py:.2f} {pz:.2f}\n")

    for z in range(size + 1):
        for x in range(size + 1):
            u = x / size
            v = z / size
            f.write(f"vt {u:.2f} {v:.2f}\n")

    f.write("vn 0.0 1.0 0.0\n")

    for z in range(size):
        for x in range(size):
            i = z * (size + 1) + x + 1
            f.write(f"f {i}/{i}/1 {i + 1}/{i + 1}/1 {i + size + 2}/{i + size + 2}/1\n")
            f.write(f"f {i}/{i}/1 {i + size + 2}/{i + size + 2}/1 {i + size + 1}/{i + size + 1}/1\n")


# Jeszcze odpowiadając na pytanie z prezentacji projektu: wszystkie drzewa umieszczone są na tej samej współżędnej Y.
# Z racji tego, że teren jest nierówny, drzewa wyrastają z ziemi.