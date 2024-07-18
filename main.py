import math


class Constantes:
    C = 299792458  # Velocidad de la luz en el vacío (m/s)
    H = 6.62607015e-34  # Constante de Planck (J·s)
    G = 6.67430e-11  # Constante gravitacional (m^3·kg^-1·s^-2)


class RelatividadEspecial:
    @staticmethod
    def energia_mc2(masa):
        """ Calcula la energía según la fórmula de Einstein E = mc^2. """
        return masa * Constantes.C**2

    @staticmethod
    def dilatacion_tiempo(t, v):
        """ Calcula la dilatación del tiempo. """
        return t / math.sqrt(1 - (v**2 / Constantes.C**2))

    @staticmethod
    def contraccion_longitud(L, v):
        """ Calcula la contracción de la longitud. """
        return L * math.sqrt(1 - (v**2 / Constantes.C**2))

    @staticmethod
    def energia_relativista_total(masa_reposo, p):
        """ Calcula la energía relativista total. """
        return math.sqrt((p * Constantes.C)**2 + (masa_reposo * Constantes.C**2)**2)

    @staticmethod
    def energia_cinetica_relativista(masa_reposo, v):
        """ Calcula la energía cinética relativista. """
        gamma = 1 / math.sqrt(1 - (v**2 / Constantes.C**2))
        return (gamma - 1) * masa_reposo * Constantes.C**2


class RelatividadGeneral:
    @staticmethod
    def ecuacion_friedmann(rho, k, a, Lambda):
        """
        Calcula la ecuación de Friedmann para la expansión del universo.

        Parámetros:
        rho (float): Densidad de materia y energía.
        k (float): Curvatura del universo.
        a (float): Factor de escala.
        Lambda (float): Constante cosmológica.

        Retorna:
        float: La tasa de expansión del universo.
        """
        return math.sqrt((8 * math.pi * Constantes.G * rho / 3) - (k / a**2) + (Lambda / 3))


class EfectoFotoelectrico:
    @staticmethod
    def energia_fotoelectrico(frecuencia, funcion_trabajo):
        """
        Calcula la energía del electrón emitido en el efecto fotoeléctrico.

        Parámetros:
        frecuencia (float): Frecuencia de la luz incidente en Hz.
        funcion_trabajo (float): Función de trabajo del material en julios.

        Retorna:
        float: Energía del electrón emitido en julios.
        """
        return Constantes.H * frecuencia - funcion_trabajo
