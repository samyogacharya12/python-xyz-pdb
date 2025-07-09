import sys

def xyz_to_pdb(xyz_path, pdb_path):
    with open(xyz_path) as f:
        lines = f.read().strip().splitlines()

    pdb_lines, serial = [], 1
    for line in lines[2:]:
        parts = line.strip().split()
        if len(parts) != 4: continue
        atom, x, y, z = parts
        pdb_lines.append(
            f"ATOM  {serial:5d} {atom:<4} UNK A   1    "
            f"{float(x):8.3f}{float(y):8.3f}{float(z):8.3f}  1.00  0.00           {atom[0].upper()}"
        )
        serial += 1

    with open(pdb_path, 'w') as f:
        f.write('\n'.join(pdb_lines))

    print(f"✅ Converted {serial-1} atoms to {pdb_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python circDNA.xyz.py input.xyz output.pdb")
        sys.exit(1)
    xyz_to_pdb(sys.argv[1], sys.argv[2])
