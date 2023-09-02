import sys
from molsysmt import convert

if sys.version_info[1]==10:
    from importlib.resources import files
    def path(package, file):
        return files(package).joinpath(file)
elif sys.version_info[1] in (8,9):
    from pathlib import PurePath
    parent = PurePath(__file__).parent
    def path(package, file):
        data_dir = package.split('.')[-1]
        return parent.joinpath('../data/'+data_dir+'/'+file).__str__()

demo_dict = {}

# TcTIM

demo_dict['TcTIM'] = {}
demo_dict['TcTIM']['vacuum'] = path('obinding.data', 'TcTIM_vacuum.msmpk')

# Barnase - Barstar

demo_dict['Barnase-Barstar'] = {}
demo_dict['Barnase-Barstar']['vacuum'] = path('obinding.data', 'Barnase_Barstar_vacuum.msmpk')

def demo(system='Barnase-Barstar', name=None):


    if name is None:
        if system=='Barnase-Barstar':
            name='vacuum'
        elif system=='TcTIM':
            name='vacuum'

    return convert(demo_dict[system][name])

