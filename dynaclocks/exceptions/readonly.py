class readonly(property):
    def fset(self):
        raise Exception(self,"Property is readonly")