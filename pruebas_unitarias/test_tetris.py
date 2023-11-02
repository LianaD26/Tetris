from implementacion.tetris import JuegoTetris
# letras: I, O, T, S, Z, J, L
def test_crear_correctamente_tetris():
    # Arrange
    tetris = JuegoTetris()
    letra = "Z"
    matriz = [[".", ".", ".", "."],
              [".", "@", "@", "."],
              [".", ".", "@", "@"],
              [".", ".", ".", "."]]
    # Act
    resultado = tetris.pos_iniciales(letra)
    # Assert
    assert resultado == matriz

def test_rotar_correctamente_90grados_tetris():
    # Arrange
    tetris = JuegoTetris()
    letra = "L"
    num_rotacion = 1 # 90 grados
    matriz_rot = [[".", ".", ".", "."],
                  [".", "@", "@", "@"],
                  [".", "@", ".", "."],
                  [".", ".", ".", "."]]
    # Act
    resultado = tetris.mostrar_matriz(tetris.rotacion(letra, num_rotacion))
    # Assert
    assert resultado == matriz_rot

def test_rotar_correctamente_180grados_tetris():
    # Arrange
    tetris = JuegoTetris()
    letra = "L"
    num_rotacion = 2 # 180 grados
    matriz_rot = [[".", ".", ".", "."],
                  [".", "@", "@", "."],
                  [".", ".", "@", "."],
                  [".", ".", "@", "."]]
    # Act
    resultado = tetris.mostrar_matriz(tetris.rotacion(letra, num_rotacion))
    # Assert
    assert resultado == matriz_rot

def test_rotar_correctamente_270grados_tetris():
    # Arrange
    tetris = JuegoTetris()
    letra = "L"
    num_rotacion = 3 # 270 grados
    matriz_rot = [[".", ".", ".", "."],
                  [".", ".", "@", "."],
                  ["@", "@", "@", "."],
                  [".", ".", ".", "."]]
    # Act
    resultado = tetris.mostrar_matriz(tetris.rotacion(letra, num_rotacion))
    # Assert
    assert resultado == matriz_rot

def test_rotar_correctamente_360grados_tetris():
    # Arrange
    tetris = JuegoTetris()
    letra = "L"
    num_rotacion = 4 # 360 grados
    matriz_rot = [[".", "@", ".", "."],
                  [".", "@", ".", "."],
                  [".", "@", "@", "."],
                  [".", ".", ".", "."]]
    # Act
    resultado = tetris.mostrar_matriz(tetris.rotacion(letra, num_rotacion))
    # Assert
    assert resultado == matriz_rot

def test_verificar_letras_con_igualdad():
    #se debe corregir la función igualdad
    pass

def test_verificar_letra_correcta_en_archivo():
    # Arrange
    tetris = JuegoTetris()
    letra = "S"
    num_rotacion = 2
    name = "file.txt"
    matriz_correcta = [[".", ".", ".", "."],
                       [".", "@", "@", "."],
                       ["@", "@", ".", "."],
                       [".", ".", ".", "."]]
    # Act
    # escribir el archivo con matriz_correcta
    archivo_esperado = open("matriz_correcta.txt", "w")
    for row in range(len(matriz_correcta)):
        fila = ""
        for col in range(len(matriz_correcta)):
            simbolo = str(matriz_correcta[row][col])
            fila += simbolo
        archivo_esperado.write(fila + "\n")
    archivo_esperado.close()
    # llamar funcion del archivo de Tetris
    tetris.archivo_letra(letra, num_rotacion, name) #archivo con la solucion
    archivo_actual = open(f"{name}", "r")
    # comparar los archivos
    actual = archivo_actual.readlines()
    esperado = archivo_esperado.readlines()
    # Assert
    assert esperado == actual