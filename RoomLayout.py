from enum import Enum

"""
X: Filled
O: Empty

Default:                -----
                        |O|O|
                        -----
                        |X|O|
                        -----
                        
Large:                  -----
                        |X|X|
                        -----
                        |X|X|
                        -----
                        
Gamma:                  -----
                        |X|X|
                        -----
                        |X|O|
                        -----
                        
FlippedGamma:           -----
                        |X|O|
                        -----
                        |X|X|
                        -----
                        
InverseGamma:           -----
                        |X|X|
                        -----
                        |O|X|
                        -----
                        
FlippedInverseGamma:    -----
                        |O|X|
                        -----
                        |X|X|
                        -----
                        
Long:                   -----
                        |X|O|
                        -----
                        |X|O|
                        -----
                        
wide:                   -----
                        |O|O|
                        -----
                        |X|X|
                        -----
                        

"""
class RoomLayout(Enum):
    default = "default"
    Large = "Large"
    Gamma = "Gamma"
    FlippedGamma = "FlippedGamma"
    InverseGamma = "InverseGamma"
    FlippedInverseGamma = "FlippedInverseGamma"
    Long = "Long"
    Wide = "Wide"
