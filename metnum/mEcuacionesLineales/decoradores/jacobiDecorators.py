from numpy import array


def jacobi_args_types_checking(fn):
    pass


def jacobi_args_transform_np_array(fn):
    def wrapper(*args):

        tempList = list(args)
        tempList = [array(arg, dtype=float) if isinstance(
            arg, (list)) else arg for arg in tempList]

        # Verificando shape de algunos args (b,x0) y haciendo reshape
        if tempList[1].ndim == 1:
            tempList[1] = tempList[1].reshape(tempList[1].shape[0], 1)
        if tempList[2].ndim == 1:
            tempList[2] = tempList[2].reshape(tempList[2].shape[0], 1)

        argsModified = tuple(tempList)
        return fn(*argsModified)

    return wrapper
