#!/usr/bin/env python
# -*- coding: utf-8 -*-

def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        values = []
        while len(values) < 10:
            values.append(input("Entez une valeur:"))
    return sorted(values)

def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        words = []
        words.append(sorted(input("Premier mot:")))
        words.append(sorted(input("Deuxième mot:")))
    return words[0] == words[1]

def contains_doubles(items: list) -> bool:
    return not len(set(items)) == len(items)

def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return max([(sum(score) / len(score), student) for (student, score) in student_grades.items()])[1]

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    count = {}
    for l in sentence:
        if l in count:
            count[l] += 1
        else:
            count[l] = 1
    count = {k: v for k, v in sorted(count.items(), key=lambda item: item[1], reverse=True)}
    for i in count.items():
        if i[1] >= 5:
            count[i[0]] = i[1]
    return count

def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass

def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass

def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    anagrams()

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    # grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    # best_student = best_grades(grades)
    # print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    print(frequence(sentence))

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
