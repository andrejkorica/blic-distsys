def prvi_zadatak(l):
    assert isinstance(l, list) and all([isinstance(x, str) for x in l])
    return {(i):(x[::-1]) for i,x in enumerate(l)}

lista = ["Stol", "Stolica", "Krevet"]
print(prvi_zadatak(lista))