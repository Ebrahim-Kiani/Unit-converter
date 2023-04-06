class convertor():
    def __init__(self ,unit1 ,  unit2 , arguman):
        self.unit1 =unit1
        self.unit2 =  unit2
        self.arguman = arguman
        
    def convert_other_to_meter(self):
        result = None
        if self.unit1 == 'Meter':
            result = self.arguman

        elif self.unit1 =='Centimeter':
            result=  self.arguman /100

        elif self.unit1 == 'Milimeter':
            result =  self.arguman /1000

        elif self.unit1 =='Yard':
            result =   self.arguman*0.9144

        elif self.unit1 == 'Mile':
            result = self.arguman *1609.
            
        return(result)    
    
    #convert_meter_to_other    
    def convertor(self):
        meter = self.convert_other_to_meter()

        if  self.unit2 == 'Meter':
             meter =(meter) 

        elif    self.unit2 == 'Centimeter':
             meter = meter*100

        elif    self.unit2 == 'Milimeter':
             meter = meter*1000

        elif    self.unit2 == 'Yard':
             meter = meter*1.09361

        elif    self.unit2 == 'Mile':
            meter = meter*0.000621
        return meter 