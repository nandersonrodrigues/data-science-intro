import math

def vector_add(v, w):
    """Soma elementos correspondentes"""
    return [ v_i + w_i for v_i, w_i in zip(v, w)]

def vector_subtract(v, w):
    """Subtrai elementos correspondentes"""
    return [ v_i - w_i for v_i, w_i in zip(v, w)]

def vectors_sum(vectors):
    """Soma todos elementos correspondentes"""
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result

def scalar_multiply(c, v):
    """c é um numero v é um vetor"""
    return [c * v_i for v_i in v]

def vector_mean(vectors):
    """i-ésimo elemento seja a média dos i-ésimos elemento dos vetores inclusos"""
    n = len(vectors)
    return scalar_multiply(1/n, vectors_sum(vectors))

def dot(v, w):
    """Produto escalar - soma do produto dos componentes, compoente a componente"""
    return sum(v_i * w_i for v_i, w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
    return magnitude(vector_subtract(v, w))

    