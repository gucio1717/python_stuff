from mfw.controller import Controller
from mfw.dataprovider.hwdata import HwData
from mfw.dataprovider.softwaredata import SoftwareData
from mfw.controller.rpsoftware import RpSoftware


class DtGenerator(Controller):
    """
    Controller that generates full DT.
    """

    def __init__(self, hw_file, bsc_config, laeip_file, features):
        super(DtGenerator, self).__init__()
        self.root_dir = self._glob.root_dir
        self.hw_file = hw_file
        self.bsc_config = bsc_config
        self.laeip_file = laeip_file
        self.features = features

    def _load_data(self):
        """
        Load configuration data.
        """
        stp_config_file = '{}/bsc_hardware/{}.xml'.format(self.root_dir,
                                                          self.hw_file)
        stp_config_file = self.hw_file
        print(stp_config_file)


        bschw = self.get_result(HwData(stp_config_file))
        laeip = self.get_result(SoftwareData(self.laeip_file))

        return bschw, laeip

    def generate(self):
        '''
        Generates full DT, and returns it as string.
        :rtype string
        '''
        bschw, laeip = self._load_data()

        print(bschw)
        print(laeip)
        print(self._glob.env)
        self._glob.
        outputStream = self._glob.env.stream(dts='a',stp='b')

        print(outputStream)
        
        data = self.get_result(RpSoftware(laeip))

        try:
            self.load_view('template_name', data)
        except:
            self.logger.info('It is only demo app!!')
            pass

        return self.result
