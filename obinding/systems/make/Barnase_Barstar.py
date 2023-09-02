import molsysmt as msm
import os

# purge
print('Removing old files...')
files_to_be_purged = ['../../data/msmpk/Barnase_Barstar_vacuum.msmpk', '../../data/mmtf/1BRS.mmtf']
for filename in files_to_be_purged:
    if os.path.isfile(filename):
        os.remove(filename)

# purge
print('Making new files...')
molecular_system = msm.convert('1BRS', to_form='../../data/mmtf/1BRS.mmtf')
molecular_system = msm.convert(molecular_system)
molecular_system = msm.extract(molecular_system, selection='molecule_type=="protein"')
barnase = msm.extract(molecular_system, selection="chain_name=='B'")
barstar_E = msm.extract(molecular_system, selection="chain_name=='E'")
barstar_F = msm.extract(molecular_system, selection="chain_name=='F'")
barstar_F_over_E = msm.structure.align(barstar_F, selection='atom_name=="CA"',
                                       reference_molecular_system=barstar_E, reference_selection='atom_name=="CA"')
barnase_barstar = msm.merge([barnase, barstar_F_over_E])
barnase_barstar = msm.build.add_missing_heavy_atoms(barnase_barstar)
barnase_barstar = msm.build.add_missing_hydrogens(barnase_barstar, pH=7.4)
msm.molecular_mechanics.potential_energy_minimization(barnase_barstar)
_ = msm.convert(barnase_barstar, to_form='../../data/msmpk/Barnase_Barstar_vacuum.msmpk')

