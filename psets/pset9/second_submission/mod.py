def build_mod_tex(divisor: int, dividend: int) -> str:
    return f"${divisor % dividend} \\Mod {{{dividend}}}$"

if __name__ == "__main__":
    dividend = int(input("Enter dividend: "))

    for base in range(1, dividend):
        print(base, end=" & ")
        for power in range(2, dividend):
            divisor = base ** power
            if (power == dividend - 1):
                print(build_mod_tex(divisor, dividend), end=" \\\\ \n")
            else:
                print(build_mod_tex(divisor, dividend), end=" & ")