import sys

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


tests = {}

# Barnase - Barstar

tests['Barnase-Barstar'] = {}
tests['Barnase-Barstar']['barnase_barstar.msmpk'] = path('molsysmt.data.msmpk', 'vacuum.msmpk')
tests['Barnase-Barstar']['1brs.mmtf'] = path('molsysmt.data.mmtf', '1brs.mmtf')

