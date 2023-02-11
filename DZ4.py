class Videocarta:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.gtx1660 = 'gtx 1660 6gb'

class Processor:
    def __init__(self, *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.processor = 'razen 5 2600'

class Pc(Videocarta, Processor):
    def __init__(self, prise,  *rgs, **kwargs):
        super().__init__(*rgs, **kwargs)
        self.prise = prise

    def print_info(self):
        print(self.gtx1660)
        print(self.processor)
        print(self.prise)

comp = Pc(prise=30000)
comp.print_info()