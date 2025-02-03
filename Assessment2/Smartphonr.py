class Electronics:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def device_info(self):
        return f"Brand: {self.brand}, Power Source: {self.power}"

class MobileDevice(Electronics):
    def __init__(self, brand, power,):
        super().__init__(brand, power)
       

    def device_info(self):
        return f"{super().device_info()}"

class SmartPhone(MobileDevice):
    def __init__(self, brand, power,os, camera_megapixels):
        super().__init__(brand, power)
        self.os = os
        self.camera_megapixels = camera_megapixels

    def device_info(self):
        return f"{super().device_info()}, OS: {self.os}, Camera: {self.camera_megapixels} MP"

phone = SmartPhone("Samsung", "Battery", "Android", 108)
print(phone.device_info())
