import unittest
from ..metnum import biseccion


class test_biseccion(unittest.TestCase):
    def test_retorna_una_tupla(self):
        resultado = biseccion(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6)
        self.assertIsInstance(resultado, tuple)

    def test_encontro_raiz_aproximada(self):
        resultado = biseccion(lambda x: x**2 + 53 * x + 5, -1, 1, 10**-6)
        resultado2 = biseccion(lambda x: x**3 + 3 * x**2, -5, -2, 10**-8)

        self.assertAlmostEqual(resultado[0], -0.09450811)
        self.assertAlmostEqual(resultado2[0], -3.00000)

    def test_laza_TypeError_si_f_no_es_una_funcion(self):
        with self.assertRaises(TypeError):
            biseccion("2", -1, 1, 10**-6)

    def test_laza_TypeError_si_los_parametros_no_son_numericos(self):
        with self.assertRaises(TypeError):
            biseccion(lambda x: x**2 + 53 * x + 5, -1, "a", 10**-6)

    # def test_error_si_el_intervalo_no_tiene_una_raiz(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
