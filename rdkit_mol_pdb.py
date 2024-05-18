import os
from rdkit import Chem
from rdkit.Chem import AllChem

# Loop through files 1.mol to 5.mol
for i in range(1, 6):
    mol_file = f"{i}.mol"

    # Check if the .mol file exists
    if os.path.exists(mol_file):
        print(f"Converting {mol_file} to .pdb")

        # Read the .mol file using RDKit
        mol = Chem.MolFromMolFile(mol_file)

        if mol is not None:
            # Generate 3D coordinates for the molecule
            AllChem.EmbedMolecule(mol)

            # Get the directory of the input file
            input_dir = os.path.dirname(mol_file)

            # Write the molecule with 3D coordinates to a .pdb file in the same directory
            pdb_file = os.path.join(input_dir, f"{i}.pdb")
            Chem.MolToPDBFile(mol, pdb_file)
        else:
            print(f"Error reading {mol_file}")
    else:
        print(f"{mol_file} does not exist")
