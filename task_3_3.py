def thesaurus(names):
    names_dict = {}
    for name in names:
        first_letter = name[0]
        if names_dict.get(first_letter):
            names_dict[first_letter].append(name)
        else:
            names_dict.setdefault(first_letter, [name])
    return names_dict


users = ("Иннокентий", "Василий", "Роман", "Патрик", "Земфира", "Кэрол", )
name_list = thesaurus(users)
print(name_list)
