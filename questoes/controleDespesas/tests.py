from django.test import TestCase
from django.urls import reverse
from .models import Despesa


class DespesaPagamentoTests(TestCase):
    def test_cria_despesa_como_paga_quando_checkbox_marcada(self):
        self.client.post(
            reverse('controleDespesas:controleDeDespesas'),
            {
                'descricao': 'Conta de luz',
                'categoria': 'Casa',
                'valor': '120.00',
                'data': '2026-10-19',
                'pago': 'on',
            },
        )

        despesa = Despesa.objects.get()
        self.assertTrue(despesa.pago)

    def test_cria_despesa_como_nao_paga_quando_checkbox_desmarcada(self):
        self.client.post(
            reverse('controleDespesas:controleDeDespesas'),
            {
                'descricao': 'Conta de luz',
                'categoria': 'Casa',
                'valor': '120.00',
                'data': '2026-10-19',
            },
        )

        despesa = Despesa.objects.get()
        self.assertFalse(despesa.pago)
