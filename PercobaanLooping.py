def calculate_lot_sizes(Q, PA, PB, SB):
    Q1 = (Q * PA - SB) / (PB + PA)
    Q2 = Q - Q1
    return Q1, Q2


def calculate_makespan(C):
    m = len(C)
    F = [[0] * m for _ in range(m)]

    for i in range(m):
        for j in range(i + 1):
            if j == 0:
                F[i][j] = C[i][j]
            else:
                F[i][j] = max(F[i][j - 1], F[i - 1][j]) + C[i][j]

    return F


# Meminta input dari pengguna
D = float(input("Masukkan demand perorder (D): "))
dd = float(input("Masukkan lama waktu pengerjaan (dd): "))
PA = float(input("Masukkan waktu proses stage A (PA): "))
PB = float(input("Masukkan waktu proses stage B (PB): "))
SB = float(input("Masukkan waktu setup stage B (SB): "))

# Langkah 2: Hitung target produksi (n)
n = D / dd
print("Target Produksi Perhari (Unit):", n)

# Langkah 3: Input jumlah lot (N)
N = int(input("Masukkan jumlah lot (N): "))

# Langkah 4: Input jumlah sublot (k)
k = int(input("Masukkan jumlah sublot (k): "))

# Loop melalui setiap lot
for i in range(1, N + 1):
    # Hitung target produksi (n) perhari
    n = D / dd

    # Hitung lot size (Q)
    Q = n / i

    print(f"\nJumlah Lot (N): {i}")
    print("Lot Size (Q):", Q)

    if k >= 2:
        for j in range(1, k + 1):
            # Hitung ukuran sub lot
            Q1, Q2 = calculate_lot_sizes(Q, PA, PB, SB)

            if j == 1:
                sub_lot_size = Q1
            elif j == 2:
                sub_lot_size = Q2

            # Hitung Makespan stage 1
            C1 = [[sub_lot_size * PA, sub_lot_size * PB]]
            F1 = calculate_makespan(C1)
            last_makespan_1 = F1[0][0]  # Makespan untuk sublot pada stage 1

            # Cetak ukuran sub-lot dan makespan stage 1
            print(
                f"Ukuran Sub lot {j}: {sub_lot_size:.2f} - Makespan: {last_makespan_1:.2f} (Stage 1)")

            # Hitung Makespan tahap 2
            C2 = [[sub_lot_size * PA, sub_lot_size * PB]]
            F2 = calculate_makespan(C2)
            last_makespan_2 = last_makespan_1 + F2[0][0]  # Makespan untuk sublot pada stage 2

            # Cetak ukuran sub-lot dan makespan stage  2
            print(
                f"Ukuran Sub lot {j}: {sub_lot_size:.2f} - Makespan: {last_makespan_2:.2f} (Stage 2)")