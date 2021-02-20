import binascii


def function(rounds, x):
    k = 7
    f = (2 * rounds * k)
    if f >= 15:
        f = f % 15
    if x < 8:
        fe = f**x
        fm = fe % 15
        return fm
    else:
        ex = x/2
        if (x % 2) == 1:
            ex1 = int(round(ex)+1)
            ex2 = int(round(ex))  
            fe1 = f ** ex1
            fe2 = f ** ex2
            fm1 = fe1 % 15
            fm2 = fe2 % 15
            fmnext = fm1 * fm2
            fmdone = fmnext % 15
            return fmdone
        else:
            fe1 = f ** ex
            fe2 = f ** ex
            fm1 = fe1 % 15
            fm2 = fe2 % 15
            fmnext = fm1 * fm2
            fmdone = fmnext % 15
            return fmdone


def xor(binary_a, binary_b):
    xor_h = ""
    for i in range(4):
        if binary_a[i] == binary_b[i]:
            xor_h += "0"
        else:
            xor_h += "1"
    return xor_h


def bintodeci(binary):
    string = int(binary, 2)
    return string


def decitobin(decimal):
    if decimal == 1:
        return "0001"
    elif decimal == 3:
        return "0011"
    elif decimal == 7:
        return "0111"
    else:
        return bin(decimal).replace("0b", "")


def split(plaintext):
    n = 4
    chunks = [plaintext[i:i + n] for i in range(0, len(plaintext), n)]
    return chunks


def feistel_decrypt():
    ciphertext = input("Enter a 8-bit ciphertext: ")
    lists = split(ciphertext)
    l0 = lists[1]
    r0 = lists[0]
    print("Perform swap of ciphertext")
    print("")
    print("L0=", l0, "   R0=", r0)
    # ################ROUND 2###########################
    f2 = function(2, bintodeci(r0))
    f2int = int(f2)
    f2bin = decitobin(f2int)
    print("            F2=", decitobin(int(f2)))

    r1 = xor(f2bin, l0)
    l1 = r0
    print("L1=", l1, "   R1=", r1)

    # ##################ROUND 1############################
    f1 = function(1, bintodeci(r1))
    f1int = int(f1)
    f1bin = decitobin(f1int)
    print("            F2=", decitobin(int(f1)))
    r2 = xor(f1bin, l1)
    l2 = r1
    print("L2=", l2, "   R2=", r2)
    print("")
    print("Final swap to achieve plaintext:")
    print("Plaintext:", r2, l2)
    print("")


def feistel_encrypt():
    plaintext = input("Enter a 8-bit plaintext: ")
    lists = split(plaintext)

    l0 = lists[0]
    r0 = lists[1]
    print("")
    print("L0=", l0, "   R0=", r0)
    # ################ROUND 1#############################
    f1 = function(1, bintodeci(r0))
    f1int = int(f1)
    f1bin = decitobin(f1int)
    print("            F1=", decitobin(int(f1)))
    r1 = xor(f1bin, l0)
    l1 = r0
    print("L1=", l1, "   R1=", r1)

    # ##################ROUND 2############################
    f2 = function(2, bintodeci(r1))
    f2int = int(f2)
    f2bin = decitobin(f2int)
    print("            F2=", decitobin(int(f2)))
    r2 = xor(f2bin, l1)
    l2 = r1
    print("L2=", l2, "   R2=", r2)
    print("")
    print("Ciphertext:", l2, r2)
    print("")


def main():
    inMenu = 1
    while inMenu == 1:
        print("0. Exit")
        print("1. Feistel Encrypt")
        print("2. Feistel Decrypt")
        choice = int(input("Choice: "))
        if choice == 1:
            feistel_encrypt()
        elif choice == 2:
            feistel_decrypt()
        else:
            inMenu = 0


if __name__ == '__main__':
    main()
