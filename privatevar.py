class Sample:
   def __init__(self, nv, pv):
      self.nv = nv
      self.__pv = pv

sample = Sample('Normal variable', 'Private variable')

print(sample.nv)
print(sample._Sample__pv)