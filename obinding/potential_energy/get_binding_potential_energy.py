from molsysmt.basic import get
from molsysmt.molecular_mechanics import get_non_bonded_potential_energy
from obinding import pyunitwizard as puw

def get_binding_potential_energy(molecular_complex, per_groups=False):

    tmp_molecular_system = molecular_complex.molecular_system
    tmp_selection = None

    if not per_groups:
        tmp_selection = molecular_complex.component_atoms
    else:
        tmp_selection = []
        for tmp_groups in molecular_complex.component_groups:
            tmp_atoms_in_groups = get(tmp_molecular_system, element='group', selection=tmp_groups,
                    atom_index=True)
            tmp_selection.append(tmp_atoms_in_groups)

    #output =  get_non_bonded_potential_energy(molecular_complex.molecular_system,
    #        selection=tmp_selection)

    output =  get_non_bonded_potential_energy(molecular_complex.molecular_system,
            selection=tmp_selection[0], selection_2=tmp_selection[1])

    output = puw.standardize(output)

    return output

