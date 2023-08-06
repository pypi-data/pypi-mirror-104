import math
from abc import abstractmethod, ABC


class Calculador(ABC):

    @staticmethod
    @abstractmethod
    def calcula_inercia(elemento):
        pass

    @staticmethod
    @abstractmethod
    def calcula_resistencia(elemento):
        pass

    @staticmethod
    def calcula_area(elemento):
        if elemento.circulo_ou_retangulo == '1':
            area = (math.pi * elemento.dimensoes ** 2) / 4
            return area
        else:
            area = elemento.dimensoes[0] * elemento.dimensoes[1]
            return round(area, 6)

    @staticmethod
    def calcula_fc0d(elemento):
        fc0d = (elemento.kmod * elemento.Fc0k) / 1.4
        return round(fc0d, 2)
    
    @staticmethod
    def calcula_modulo_elasticidade(viga):
        Eef = (viga.Ec0m * viga.kmod) * 1000
        return round(Eef, 2)


class CalculadorViga(Calculador):

    @staticmethod
    def calcula_inercia(viga):
        if viga.circulo_ou_retangulo == '1':
            inercia = (math.pi * (viga.dimensoes ** 4)) / 64
        else:
            inercia = (viga.dimensoes[0] * viga.dimensoes[1] ** 3) / 12

        return round(inercia, 8)

    @staticmethod
    def calcula_resistencia(viga):
        if viga.circulo_ou_retangulo == '1':
            W = (math.pi * (viga.dimensoes ** 3)) / 32
        else:
            W = (viga.dimensoes[0] * (viga.dimensoes[1] ** 2)) / 6

        return W

    @staticmethod
    def calcula_carga_permanente(viga):
        carga_permanente = viga.area * 10 + viga.peso_proprio
        return carga_permanente

    @staticmethod
    def calcula_momento_fletor(viga):
        momento_fletor = (1.4 * (viga.carga_permanente + viga.carga_acidental) * viga.comprimento ** 2) / 8
        return momento_fletor

    @staticmethod
    def calcula_tensao_normal(viga):
        tensao_normal = (viga.momento_fletor / viga.modulo_resistencia) / 1000
        return round(tensao_normal, 3)

    @staticmethod
    def calcula_flecha_maxima(viga):
        flecha_maxima = (viga.comprimento / 200) * 1000
        return flecha_maxima

    @staticmethod
    def calcula_flecha_efetiva(viga):
        Vef = ((5 * (viga.carga_permanente + 0.2 * viga.carga_acidental) * viga.comprimento ** 4) / (
                384 * viga.modulo_elasticidade * viga.inercia)) * 1000
        return round(Vef, 3)


class CalculadorPilar(Calculador):

    @staticmethod
    def calcula_inercia(pilar):
        if pilar.circulo_ou_retangulo == '1':
            inercia = (math.pi * (pilar.dimensoes ** 4)) / 64
            return inercia, inercia
        else:
            inercia_z = (pilar.dimensoes[0] * pilar.dimensoes[1] ** 3) / 12
            inercia_y = (pilar.dimensoes[1] * pilar.dimensoes[0] ** 3) / 12
            return inercia_z, inercia_y

    @staticmethod
    def calcula_resistencia(pilar):
        if pilar.circulo_ou_retangulo == '1':
            W = (math.pi * (pilar.dimensoes ** 3)) / 32
            return W, W
        else:
            Wz = (pilar.dimensoes[0] * (pilar.dimensoes[1] ** 2)) / 6
            Wy = (pilar.dimensoes[1] * (pilar.dimensoes[0] ** 2)) / 6
            return Wz, Wy

    @staticmethod
    def calcula_raio_giracao(pilar):
        raio_giracao_z = math.sqrt((pilar.inercia[0]/pilar.area))
        raio_giracao_y = math.sqrt((pilar.inercia[1]/pilar.area))

        return raio_giracao_z, raio_giracao_y

    @staticmethod
    def calcula_indice_esbeltez(pilar):
        esbeltez_z = pilar.comprimento/pilar.raio_giracao[0]
        esbeltez_y = pilar.comprimento/pilar.raio_giracao[1]

        return esbeltez_z, esbeltez_y

    @staticmethod
    def calcula_tensao_normal(pilar):
        tensao_normal = pilar.flexao_composta/pilar.area

        return tensao_normal * 10

    @staticmethod
    def calcula_tensao_momento_fletor(pilar):
        tensao_z = (pilar.momentos[0] * 100)/pilar.modulo_resistencia[0]
        tensao_y = (pilar.momentos[1] * 100)/pilar.modulo_resistencia[1]

        return (tensao_z * 10), (tensao_y * 10)

    @staticmethod
    def retorna_excentricidade(pilar):
        if (pilar.indice_esbeltez[0] > 40) and (pilar.indice_esbeltez[1] > 40):
            excentricidade = []
            for item in (0, 1):
                excentricidade.append(CalculadorPilar.calcula_excentricidade(pilar, item))

        elif pilar.indice_esbeltez[0] > 40:
            excentricidade = CalculadorPilar.calcula_excentricidade(pilar, 0)

        elif pilar.indice_esbeltez[1] > 40:
            excentricidade = CalculadorPilar.calcula_excentricidade(pilar, 1)

        else: 
            excentricidade = None

        return excentricidade

    @staticmethod
    def calcula_excentricidade(pilar, algo):
        
        excentricidade_acidental = (pilar.comprimento * 10) / 300
        eiz = (pilar.momentos[algo] / pilar.flexao_composta) * 1000
        e1z = excentricidade_acidental + eiz

        fe = ((math.pi**2) * pilar.modulo_elasticidade * pilar.inercia[algo] * 10**-8) / ((pilar.comprimento / 100) ** 2)
        ezd = e1z * (fe/(fe-pilar.flexao_composta))
        myd = (pilar.flexao_composta * (ezd * 10**-3))
        sigma_myd = myd / (pilar.modulo_resistencia[algo] * 10**-6) / 1000

        resultados = (sigma_myd, myd, fe, algo, (excentricidade_acidental, eiz, e1z, ezd))
        return resultados