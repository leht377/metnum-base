import numpy as np
from .decoradores import potencias_args_types_checking, potencias_args_transform_np_array


@potencias_args_types_checking
@potencias_args_transform_np_array
def potencias(A, x, tolerancia: float = 10 ** -12, maxIter: int = 100):
    """
    Calcula el autovalor dominante y el autovector asociado utilizando el método de las potencias.

    Parámetros
    --------------
    A: np.array
        Matriz de entrada para la cual se desea calcular el autovalor dominante y el autovector asociado.
    x: np.array
        Vector inicial utilizado en el proceso iterativo.
    tolerancia: float
        Tolerancia utilizada como criterio de convergencia del método de las potencias.
        El proceso iterativo se detendrá cuando el cambio relativo en el autovalor sea menor o igual que la tolerancia.
    maxIter: int
        Número máximo de iteraciones permitidas antes de detener el proceso iterativo,
        independientemente de si se ha alcanzado o no la tolerancia de convergencia.

    Retorna:
    --------------

    lambda_: float
        El autovalor dominante calculado a partir de la matriz de entrada.
    x: np.array
        El autovector asociado al autovalor dominante.

    Ejemplos:
    >>> A = np.array([[1, 2], [3, 4]])
    >>> x = np.array([1, 1])
    >>> potencias(A, x, 1e-6, 100)
    (5.372281323269014, array([0.41597356, 0.90937671]))
    """

    lambdaviejo = np.random.rand()
    k = 0
    error = 1000
    while k <= maxIter and error >= tolerancia:
        x = np.dot(A, x) / np.linalg.norm(np.dot(A, x))
        lambda_ = np.dot(np.dot(A, x), x) / np.dot(x, x)

        # lambda = (Ax)*x/ (x*x)
        error = abs(lambda_ - lambdaviejo) / lambda_
        lambdaviejo = lambda_
        k = k + 1
    return lambda_, x