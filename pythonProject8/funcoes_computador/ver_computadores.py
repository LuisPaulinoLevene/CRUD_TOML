import toml
import yaml
def ver_computadores(computadores):
    for computador in computadores:
        print(computador)

def ver_computadores_da_base_de_dados_toml():
    dict_ds ={}
    with open('./base_de_dados.toml', 'r') as ds:
        dict_ds = toml.load(ds)
        ver_computadores(dict_ds['computadores'])