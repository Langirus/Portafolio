class Portafolio:
    """
    Representa un portafolio de inversión simple que puede rebalancearse
    según una distribución objetivo.
    """

    def __init__(self, valores_actuales, distribucion_objetivo):
        """
        valores_actuales: dict
            Dinero actual invertido por acción.
            Ejemplo: {"META": 200, "AAPL": 200}

        distribucion_objetivo: dict
            Porcentaje objetivo por acción (debe sumar 1.0).
            Ejemplo: {"META": 0.4, "AAPL": 0.6}
        """
        self.valores_actuales = valores_actuales
        self.distribucion_objetivo = distribucion_objetivo

    def rebalancear(self):
        """
        Calcula qué acciones se deben comprar y vender
        para alcanzar la distribución objetivo.
        """

        # 1. Calcular el valor total del portafolio
        valor_total = sum(self.valores_actuales.values())

        comprar = {}
        vender = {}

        # 2. Revisar cada acción objetivo
        for accion, porcentaje in self.distribucion_objetivo.items():

            # Valor que debería tener esta acción
            valor_objetivo = valor_total * porcentaje

            # Valor que tiene actualmente (0 si no existe)
            valor_actual = self.valores_actuales.get(accion, 0)

            # Diferencia entre lo ideal y lo actual
            diferencia = valor_objetivo - valor_actual

            # 3. Decidir si comprar o vender
            if diferencia > 0:
                comprar[accion] = diferencia
            elif diferencia < 0:
                vender[accion] = abs(diferencia)

        return comprar, vender


# Ejemplo de uso
if __name__ == "__main__":
    portafolio = Portafolio(
        valores_actuales={"META": 200, "AAPL": 200},
        distribucion_objetivo={"META": 0.4, "AAPL": 0.6},
    )

    comprar, vender = portafolio.rebalancear()

    print("Comprar:", comprar)
    print("Vender:", vender)
