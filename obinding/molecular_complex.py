from molsysmt import get

class MolecularComplex():

    def __init__(self, molecular_system, selection='all', syntax='MolSysMT'):

        self.molecular_system = molecular_system
        self.component_atoms = []
        self.component_groups = []
        self.component_names = []
        self.component_types = []
        self.component_ids = []
        self._component_original_indices = []
        self.n_components = 0

        atom_indices, group_indices, indices, names, types, ids = get(molecular_system, element='component',
                    selection=selection, atom_index=True, group_index=True, component_index=True, component_name=True,
                    component_type=True, component_id=True, syntax=syntax)

        self.component_atoms = atom_indices
        self.component_groups = group_indices
        self.component_names = names
        self.component_types = types
        self.component_ids = ids
        self._component_original_indices = indices
        self.n_components = len(self.component_atoms)

        del(atom_indices, group_indices, indices, names, types, ids)

