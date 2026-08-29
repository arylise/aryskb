stri = """

&kp ESC        &kp F1      &kp F2      &kp F3      &kp F4         &kp F5      &kp F6         &kp F7      &kp F8         &kp F9      &kp F10        &kp F11     &kp F12     &none       
&none     &none    &kp PAGE_UP    &kp UP      &kp PAGE_DOWN          &none       &none       &none       &none       &none       &none       &kp BSPC       &kp DEL     &none       &trans      
&trans       &none      &kp LEFT    &kp DOWN    &kp RIGHT   &none          &none       &none       &none       &none             &kp RET           &none       &none       &trans      
&trans               &kp HOME       &kp DOWN       &kp END       &none       &none       &none       &none       &none       &none          &kp UP         &none       &none       &trans      
&trans         &trans         &trans         &trans            &trans      &trans         &trans         &trans         &kp LEFT    &kp DOWN    &kp RIGHT      &none       &trans      


"""

parts = []

max_len = 0

for line in stri.split("\n"):
    line = line.strip()
    line_ = []
    i = 0
    for part in line.split("&"):
        cur_len = len(part)
        if cur_len == 0:
            continue
        key = part.rstrip()
        line_.append(key)
        if len(key) > max_len and i != len(line):
            max_len = len(key)
        i += 1
    if len(line_) == 0:
        continue
    parts.append(line_)

key_diff = (max_len + 4) // 4

key_len = key_diff * 4

print(key_diff)
print(key_len)

diff = [
    [1, 5, 7, 9, 11],
    [12],
    [1, 10, 10, 11, 11],
    [1, 1, 1, 10, 11],
    [1, 2, 3, 4, 4, 6, 7, 8, 11],
]

formated = ""

line_id = 0
for line in parts:
    _map = {}
    for spc in diff[line_id]:
        _map[spc] = _map.get(spc, 0) + 1
    i = 0
    for key in line:
        formated += " " * (_map.get(i, 0) * key_diff) + "&" + key
        if line.index(key) != len(line):
            formated += " " * (key_len - len(key) - 1)
        i += 1

    formated += "\n"
    line_id += 1

print(formated)
