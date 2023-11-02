class JuegoTetris:
    def __init__(self):
        self.piezas = {
            "I": [[0, 2], [1, 2], [2, 2], [3, 2]],
            "O": [[1, 1], [1, 2], [2, 1], [2, 2]],
            "T": [[1, 1], [1, 2], [1, 3], [2, 2]],
            "S": [[1, 2], [1, 3], [2, 1], [2, 2]],
            "Z": [[1, 1], [1, 2], [2, 2], [2, 3]],
            "J": [[0, 2], [1, 2], [2, 1], [2, 2]],
            "L": [[0, 1], [1, 1], [2, 1], [2, 2]],
        }

    def mostrar_matriz(self, indices):
        matriz = [["."] * 4 for _ in range(4)]
        for i in indices:
            matriz[i[0]][i[1]] = "@"
        return matriz
    def pos_iniciales(self, letra):
        return self.mostrar_matriz(self.piezas[letra])

    def rotacion(self, letra, num_rot):  # num_rot es la cant de rotaciones de 90° que hará
        if num_rot == 1:
            original = self.piezas[letra]
            nueva_pieza = [[row, 3 - col] for col, row in original]
        elif num_rot == 2:
            original = self.rotacion(letra, 1)
            nueva_pieza = [[row, 3 - col] for col, row in original]
        elif num_rot == 3:
            original = self.rotacion(letra, 2)
            nueva_pieza = [[row, 3 - col] for col, row in original]
        elif num_rot == 4:
            original = self.rotacion(letra, 3)
            nueva_pieza = [[row, 3 - col] for col, row in original]

        return nueva_pieza

    def verificar_igualdad(self, letra):
      matrices = []
      matrices.append(self.pos_iniciales(letra))

      for rotar in range(1, 5):
          matriz_rotada = self.mostrar_matriz(self.rotacion(letra, rotar))
          matrices.append(matriz_rotada)

      for i in range(len(matrices)):
        for j in range(i + 1, len(matrices)):
            if matrices[i] == matrices[j]:
                return True
      return False

    def archivo_letra(self, letra, num_rotacion, name):
      tetromino = self.mostrar_matriz(self.rotacion(letra, num_rotacion))
      archivo = open(f"{name}", "w")
      for row in range(len(tetromino)):
        fila = ""
        for col in range(len(tetromino)):
          simbolo = str(tetromino[row][col])
          fila += simbolo
        archivo.write(fila+"\n")
      archivo.close()