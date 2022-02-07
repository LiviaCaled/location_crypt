import crypt_lib

def test_encrypti_simple():
    hsh = crypt_lib.encrypt(548000, (43.16,131.89))
    assert hsh == [8, 45, 42, 42, 42, 1, 169, 42]

