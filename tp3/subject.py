from string import ascii_lowercase

"""
Le but de ce tp est de voir des chiffrement/dechiffrement classique symétrique
"""


def cesar_cipher(text: str, key: int) -> str:
    """
    Le chiffrement césar est un chiffrement par décalage avec une clef:
    https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage
    
    Nous feront un décalage que sur les lettres se trouvant dans "ascii_lowercase"
    ascii_letters = "abcdefghijklmnopqrstuvwxyz"
    Donc que les minuscules, les autres haractere seront gardé.

    :key example:
    cesar_cipher("Le soleil est beau.", 5) = "Lj xtqjnq jxy gjfz."
    
    :key indication: 
    - ascii_letters.find(c) 
        -> premet d'avoir l'indice de la lettre dans la string ascii_letters
        -> cette meme fonction renvoie -1 si elle n'est pas trouvé
    - la fonction modulo (%) sera aussi tres utile pour bouclé sur ascii_letters dans un décalage
    
    :param text: text a chiffé
    :param key: décalage a faire
    :return: texter chiffré
    """
    if key % len(ascii_lowercase) == 0:
        return text

    res = ""
    for c in text:
        if (i := ascii_lowercase.find(c)) != -1:
            c = ascii_lowercase[(i + key) % len(ascii_lowercase)]
        res += c
    return res


def cesar_decipher(text: str, key: int) -> str:
    """
    Cette fonction déchiffre un message
    :param text: text a déchiffré
    :param key: clef de chiffrage utilisé
    :return: text déchiffré
    """
    return cesar_cipher(text, -key)


"""
Dans cette partie nous allons voir comment casser un chiffrace Cesar avec l'analyse fréquenciel
"""

l_fth = [9.42, 1.02, 2.64, 3.39, 15.87, 0.95,
         1.04, 0.77, 8.41, 0.89, 0.00, 5.34,
         3.24, 7.15, 5.14, 2.86, 1.06, 6.46,
         7.90, 7.26, 6.24, 2.15, 0.00, 0.30,
         0.24, 0.32]
# mapping des fréquence théorique en francais
fth = {letter: freq for (letter, freq) in zip(ascii_lowercase, l_fth)}


def total_char(text: str) -> int:
    count = 0
    for s in text:
        if s in ascii_lowercase:
            count += 1
    return count


def frequency(text: str) -> dict[str, int]:
    """
    donne la fréquence de chaque lettre sous forme d'un dictionaire
    lettre vers frequence

    :key calcul de fréquence:
    - count_c(c) = compte de charactere c dans le text (pensé a string.count(c))
    - total_char = nombre tatal de caractere (faire une fonction auxilaire)
    - f_c(c) = count_c /  tatal
    :param text:
    :return:
    """
    total = total_char(text)
    return {c: (text.count(c) / total) for c in ascii_lowercase}


def q_freq(freq_text: dict[str, int]) -> int:
    """
    Soit:
    - f_th(c): la fréquence d'une lettre dans la langue attendue
    - f_c(c): la fréquence d'une lettre dans le message chiffré

    On définie une quantité Q tel que:
    Qf: somme_c (fc(c) - fe) ^ 2

    :param freq_text: f_c (vue plus haut)
    :return: calcul de Qf
    """
    return sum((fth[c] - freq_text[c]) ** 2 for c in ascii_lowercase)


def q_text(text: str) -> int:
    """
    Qf d'un text
    :param text: text a analysé
    :return: quantité
    """
    freq = frequency(text)
    return q_freq(freq)


def crack_cesar(text: str) -> (int, str):
    """
    Le but ici est d'utiliser l'analyse fréquenciel pour craquer le message.
    https://fr.wikipedia.org/wiki/Analyse_fr%C3%A9quentielle

    On sait que quand la quantité est minimal sur tout les décalage possible.
    On va donc testé les 26 décalage possible et voir quand la quantité est minimal.
    (la quantité minimal signifie donc la meilleur solution de décalage)

    :param: text chiffré a casser
    :return: on renvoie le couple clef, text déchifré
    """
    qte_min = q_text(text)
    solution = 0, text
    for i in range(1, len(ascii_lowercase)):
        cur_text = cesar_decipher(text, i)
        if (qte := q_text(cur_text)) < qte_min:
            qte_min = qte
            solution = (i, cur_text)
    return solution
