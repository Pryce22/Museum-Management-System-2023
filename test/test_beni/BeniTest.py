import unittest
import os
import pickle
from test.test_beni.ControlloreBeniTest import *
from test.test_beni.BeneTest import *


class TestControlloreListaBeni(unittest.TestCase):
    def setUp(self):
        self.controllore = ControlloreListaBeni()
        self.bene_di_test = Bene(nome="Bene di Test", immagine="test.jpg", area="Area Test", descrizione="Descrizione di Test", stato=True, stato_area=True,id_bene=1, data_di_aggiunta="01-01-2023")
        self.controllore.inserisci_bene(self.bene_di_test)

    def test_inserisci_bene(self):
        bene_da_inserire = Bene(nome="Nuovo Bene", immagine="nuovo.jpg", area="Nuova Area", descrizione="Descrizione Nuova", stato=True, stato_area=True,id_bene=2, data_di_aggiunta="01-01-2023")
        self.controllore.inserisci_bene(bene_da_inserire)
        self.assertEqual(bene_da_inserire.nome, self.controllore.cerca_bene_per_id(bene_da_inserire.id_bene).nome)

    def test_elimina_bene(self):
        self.assertTrue(self.controllore.elimina_bene(self.bene_di_test))

    def test_cerca_bene_per_id(self):
        bene_trovato = self.controllore.cerca_bene_per_id(1)
        self.assertEqual(bene_trovato.id_bene, self.bene_di_test.id_bene)

    def test_cerca_bene_per_nome(self):
        bene_trovato = self.controllore.cerca_bene_per_nome("Bene di Test")
        self.assertEqual(bene_trovato.nome, self.bene_di_test.nome)

    def test_controlla_nome(self):
        risultato = self.controllore.controlla_nome("Bene di Test")
        self.assertFalse(risultato)

    def tearDown(self):
        # Ripristina lo stato iniziale eliminando il bene di test
        self.controllore.elimina_bene(self.bene_di_test)


if __name__ == '__main__':
    unittest.main()
