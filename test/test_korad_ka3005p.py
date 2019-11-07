import sys

from sipyco.test.generic_rpc import GenericRPCCase


class GenericKoradKA3005PTest:
    def test_parameters_readback(self):
        # check device ID baked into firmware
        ids = self.cont.get_id()
        self.assertEqual(ids, "KORADKA3005PV2.0")


class TestKoradKA3005PSim(GenericRPCCase, GenericKoradKA3005PTest):
    def setUp(self):
        GenericRPCCase.setUp(self)
        command = (sys.executable.replace("\\", "\\\\")
                            + " -m korad_ka3005p.aqctl_korad_ka3005p "
                            + "-p 3256 --simulation")
        self.cont = self.start_server("korad_ka3005p", command, 3256)
