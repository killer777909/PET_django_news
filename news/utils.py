class MyMixin(object):
    mixin_prop = ''

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, text):
        if isinstance(text, str):
            return text.upper()
        else:
            return text.title.upper()
