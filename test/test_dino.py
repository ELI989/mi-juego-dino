import unittest
from unittest.mock import patch
import pygame
import sys
import os

# Añadir el directorio src al sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Mock para evitar que el juego se inicie automáticamente
with patch("main.main", lambda: None):
    from main import Dinosaur, RUNNING, JUMPING, DUCKING

class TestDinosaur(unittest.TestCase):

    def setUp(self):
        pygame.init()  # Inicializamos pygame antes de ejecutar las pruebas.
        self.dino = Dinosaur()  # Creamos una instancia del dinosaurio.

    def test_initial_state(self):
        # Verificamos que el estado inicial del dinosaurio sea correcto
        self.assertEqual(self.dino.dino_rect.y, self.dino.Y_POS)
        self.assertEqual(self.dino.image, self.dino.run_img[0])
        self.assertTrue(self.dino.dino_run)
        self.assertFalse(self.dino.dino_jump)
        self.assertFalse(self.dino.dino_duck)

    def test_jump(self):
        # Hacemos que el dinosaurio salte y verificamos el cambio en su posición.
        self.dino.dino_jump = True
        initial_pos = self.dino.dino_rect.y
        self.dino.jump()
        # Verificamos que la posición del dinosaurio haya disminuido después de saltar.
        self.assertLess(self.dino.dino_rect.y, initial_pos)

    def test_duck(self):
        # Hacemos que el dinosaurio se agache y verificamos que la posición cambia.
        self.dino.dino_duck = True
        self.dino.duck()
        self.assertEqual(self.dino.dino_rect.y, self.dino.Y_POS_DUCK)
        self.assertEqual(self.dino.image, self.dino.duck_img[0])

    def test_run(self):
        # Verificamos que el dinosaurio esté corriendo y su imagen cambie.
        self.dino.dino_run = True
        self.dino.run()
        self.assertEqual(self.dino.image, self.dino.run_img[0])  # La imagen debería estar en la primera imagen de correr.

    def tearDown(self):
        pygame.quit()  # Limpiamos pygame después de las pruebas.

if __name__ == '__main__':
    unittest.main()
