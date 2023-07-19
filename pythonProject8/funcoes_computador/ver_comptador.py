import toml
import yaml
def ver_computador(computadores):
    ID = input('Escreva o codigo computador: ')
    for computador in computadores:
        if computador['ID'] == ID:
            print(computador)

def ver_computador_da_base_de_dados_toml():
    dict_ds ={}
    with open('./base_de_dados.toml', 'r') as ds:
        dict_ds = toml.load(ds)
        ver_computador(dict_ds['computadores'])