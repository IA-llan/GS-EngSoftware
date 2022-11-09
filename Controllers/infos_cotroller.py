from Models.info_model import Info_model


class Info_controller:
    def __init__(self):
        self.value = Info_model()

    def get_index(self, index):
        self.value.infos(index)
