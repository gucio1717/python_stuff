from mfw import MfwObject
from io import StringIO
from jinja2 import Environment


class Controller(MfwObject):
    """
    Extends BaseController functionality with template support functionality.
    """

    def __init__(self):
        super(Controller, self).__init__()
        self._buff = StringIO()
        if isinstance(self._glob.env, Environment):
            self._env = self._glob.env

    def load_view(self, name, data):
        '''Load template from template environment,
        fills it with data and saves it to internal buffer.
        :type name: str
        :type data: dict
        '''
        if not self._env:
            raise Exception('jinja2.Environment class'
                            ' is not in GlobalRegister')
        template = self._env.get_template(name + '.dtt')
        self._buff.write(template.render(data))

    def append_result(self, data):
        '''
        Appends data to internal result buffer
        :type data: str
        '''
        self._buff.write(data)

    @property
    def result(self):
        return self._buff.getvalue()
