def squarecubes(l: list) -> tuple[list]:
    squares = [x**2 for x in l]
    cubes = [x**3 for x in l]

    return squares, cubes
