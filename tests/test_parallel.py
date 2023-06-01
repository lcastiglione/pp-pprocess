﻿"""Test unitarios para pprocess"""

import unittest
from pprocess import TaskProcess
from tests.utils import TestController


# Listado de testa a realizar:
#
# ✔️ send
# ✔️ send_bacth
# ❌ start
# ❌ close
# ❌ _requests_manager
# ❌ _repsonse_manager
# ❌ Distintas configuraciones en el __init__
# ❌ Error en ejecución de tarea en proceso remoto
# ❌ Cancelación de request por parte del usuario


class TaskProcessTestCase(unittest.IsolatedAsyncioTestCase):
    '''Clase de prueba para ParallelProcess
    '''

    def __init__(self, methodName="runTest"):
        '''Inicializador de la clase EventBusTestCase.
        '''
        super().__init__(methodName=methodName)
        self.task_process = None

    async def asyncSetUp(self):
        '''Tareas asincrónas que se ejcutan antes de cada prueba.
        '''
        test_controller = TestController()
        try:
            self.task_process = TaskProcess(controller=test_controller, num_processes=1)
            await self.task_process.start()
        except Exception as exc:
            print(exc)

    async def asyncTearDown(self):
        '''Tareas asincrónas que se ejcutan después de cada prueba.
        '''
        await self.task_process.close()

    async def test_send(self):
        '''Test que pruba la función send de TaskProcess
        '''
        input_data = 1
        result = await self.task_process.send(input_data)
        self.assertEqual(result, 20000)

    async def test_send_batch(self):
        '''Test que pruba la función send de TaskProcess
        '''
        input_data = [0, 1, 2]
        result = await self.task_process.send_batch(input_data)
        self.assertEqual(result, [0, 20000, 40000])
