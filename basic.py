class Basic:

    def __init__(self,MdId,MdNm,Ty,Cr,Ec,Pz,Qty):
        self.ModelId = MdId
        self.ModelName = MdNm
        self.Type = Ty
        self.Color = Cr
        self.EngineCapacity = Ec
        self.Price = Pz
        self.Quantity = Qty

    def __str__(self):
        return str(self.ModelId) + "," + str(self.ModelName) + "," + str(self.Type) + "," + str(self.Color) + "," + str(self.EngineCapacity) + str("cc") + "," + str(self.Price) + "," + str(self.Quantity) + str("\n")