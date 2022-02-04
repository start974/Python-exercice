from string import ascii_lowercase

"""
Le but de ce tp est de voir des chiffrement/dechiffrement classique symétrique
"""


def cesar_cipher(text: str, key: int) -> str:
    """
    Le chiffrement césar est un chiffrement par décalage avec une clef:
    https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calageV
    
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
    pass


def cesar_decipher(text: str, key: int) -> str:
    """
    Cette fonction déchiffre un message
    :param text: text a déchiffré
    :param key: clef de chiffrage utilisé
    :return: text déchiffré
    """
    pass


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
    pass


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
    pass


def q_text(text: str) -> int:
    """
    Qf d'un text
    :param text: text a analysé
    :return: quantité
    """
    pass


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
    pass


"""
Dans cette partie nous allons voir le chiffrage Vigenère
https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re
"""


def vigenere_cipher(text: str, key: str) -> str:
    """
    Le chiffrage vigenere est un peut plus complexe que celui de cesar.
    Il comporte une clef de chifrement qui nous fera un décalage au fur et a mesure

    Dans notre cas si un caractere non décaler consomme quand meme le décalage (var exemple).
    Et le caractere "a" à un décalage de 1, le "b" de 2, etc...

    Example: cesar_cipher("Le soleil est beau.", "abc") = "Lf spnejn fut debw."
    Car:
    Le soleil est beau.
    abcabcabcabcabcabca
    -------------------
    Lf spnejn fut debw.

    Le a nous fait un décalage de 1, le b de 2 et le c de 3

    :key fonction utile
    - ascii_letters.find(c)
        -> premet d'avoir l'indice de la lettre dans la string ascii_letters (et donc le décalage d'une lettre)
        -> cette meme fonction renvoie -1 si elle n'est pas trouvé
    - la fonction modulo (%) sera aussi tres utile pour bouclé sur ascii_letters dans un décalage

    :param text: text à chiffré
    :param key: clef utilisé
    :return: text chiffré
    """
    pass


def vigenere_decipher(text: str, key: str) -> str:
    """
    dechiffre un message vigenere
    :param text: text chiffré
    :param key: clef a utilisé
    :return: message déchiffré
    """
    pass
