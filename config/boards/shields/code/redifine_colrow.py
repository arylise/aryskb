map = {
    "c0": 20,
    "c1": 19,
    "r5": 18,
    "c2": 15,
    "r3": 14,
    "c5": 16,
    "r6": 10,
    "c8": 9,
    "c7": 8,
    "c6": 7,
    "c4": 6,
    "r1": 5,
    "r2": 4,
    "r7": 3,
    "r4": 2,
    "r0": 0,
    "c3": 21,
}


col = [""] * 9

row = [""] * 8

# <&pro_micro 9 (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>
# = <&pro_micro 21 GPIO_ACTIVE_HIGH>

for key, value in map.items():
    if key.startswith("c"):
        idx = int(key.removeprefix("c"))
        if idx != 0:
            col[idx] = f"        , <&pro_micro {value} GPIO_ACTIVE_HIGH>\n"
        else:
            col[idx] = f"        = <&pro_micro {value} GPIO_ACTIVE_HIGH>\n"

    if key.startswith("r"):
        idx = int(key.removeprefix("r"))
        if idx != 0:
            row[idx] = (
                f"        , <&pro_micro {value} (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>\n"
            )

        else:
            row[idx] = (
                f"        = <&pro_micro {value} (GPIO_ACTIVE_HIGH | GPIO_PULL_DOWN)>\n"
            )


str_a = """
        row-gpios
"""
for val in row:
    str_a += val

str_a += """        ;
        
        col-gpios
"""
for val in col:
    str_a += val

str_a += """        ;
"""


print(str_a)
