from tp3.subject import *


def test_cesar_cipher_example():
    assert cesar_cipher("Le soleil est beau", 5) == "Lj xtqjnq jxy gjfz"


au_clair_de_la_lune = \
    """
    Au clair de la lune,
    Mon ami Pierrot,
    Prête-moi ta plume
    Pour écrire un mot.
    Ma chandelle est morte,
    Je n'ai plus de feu ;
    Ouvre-moi ta porte,
    Pour l'amour de Dieu.
    """

au_clair_de_la_lune_5 = \
    """
    Az hqfnw ij qf qzsj,
    Mts frn Pnjwwty,
    Pwêyj-rtn yf uqzrj
    Ptzw éhwnwj zs rty.
    Mf hmfsijqqj jxy rtwyj,
    Jj s'fn uqzx ij kjz ;
    Ozawj-rtn yf utwyj,
    Ptzw q'frtzw ij Dnjz.
    """


def test_cesar_cipher():
    assert cesar_cipher(au_clair_de_la_lune, 5) == au_clair_de_la_lune_5
    assert cesar_cipher(au_clair_de_la_lune, 26) == au_clair_de_la_lune
    assert cesar_cipher(au_clair_de_la_lune, 31) == au_clair_de_la_lune_5


def test_cesar_decipher_example():
    assert cesar_decipher("Lj xtqjnq jxy gjfz!", 5) == "Le soleil est beau!"


def test_cesar_decipher():
    assert cesar_decipher(au_clair_de_la_lune_5, 5) == au_clair_de_la_lune
    assert cesar_decipher(au_clair_de_la_lune, 26) == au_clair_de_la_lune


def test_crack_cesar():
    assert crack_cesar("Lj xtqjnq jxy gjfz.") == (5, "Le soleil est beau.")
    assert crack_cesar(au_clair_de_la_lune) == (0, au_clair_de_la_lune)
    assert crack_cesar(au_clair_de_la_lune_5) == (5, au_clair_de_la_lune)
