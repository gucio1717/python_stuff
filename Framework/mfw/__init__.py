import logging
from jinja2 import Environment, FileSystemLoader

from mfw.globregister import GlobalRegister


class MfwObject(object):

    def __init__(self):
        self.logger = logging.getLogger(self.__module__ + '.' +
                                        self.__class__.__name__)
        self._glob = GlobalRegister()

    def execute(self):
        """
        Main function that should be overwritten in each child class.
        :rtype is not specified
        """
        pass

    def get_result(self, mfw_object):
        """
        :type controller: mfw.MfwObject
        :rtype str
        """
        if isinstance(mfw_object, MfwObject):
            return mfw_object.execute()
        else:
            raise Exception('get_result method requires MfwObject type!')


def configure_logging(log_lvl):
    strForm = logging.Formatter('%(levelname)s|%(name)s: %(message)s')

    strHnd = logging.StreamHandler()
    strHnd.setLevel(logging.DEBUG)
    strHnd.setFormatter(strForm)

    mainLogger = logging.getLogger('mfw')  # Get main logger
    mainLogger.setLevel(log_lvl)
    mainLogger.addHandler(strHnd)


def configure(root_dir, log_lvl):
    configure_logging(log_lvl)

    # Root dir for finding templates
    templateLoader = FileSystemLoader(root_dir + '/templates/')
    env = Environment(loader=templateLoader)
    GlobalRegister().add('env', env).add('root_dir',
                                         root_dir)
