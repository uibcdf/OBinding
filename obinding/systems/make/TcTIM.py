import molsysmt as msm
import os

# purge
print('Removing old files...')
files_to_be_purged = ['../../data/msmpk/TcTIM_vacuum.msmpk', '../../data/mmtf/1TCD.mmtf']
for filename in files_to_be_purged:
    if os.path.isfile(filename):
        os.remove(filename)

#
print('Making new files...')
molecular_system = msm.convert('1TCD', to_form='../../data/mmtf/1TCD.mmtf')
molecular_system = msm.convert(molecular_system)
molecular_system = msm.extract(molecular_system, selection='molecule_type=="protein"')
molecular_system = msm.build.add_missing_hydrogens(molecular_system, pH=7.4)
msm.molecular_mechanics.potential_energy_minimization(molecular_system)
_ = msm.convert(molecular_system, to_form='../../data/msmpk/TcTIM_vacuum.msmpk')

