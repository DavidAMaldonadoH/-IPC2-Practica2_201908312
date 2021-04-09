class NodoContacto:

   def __init__(self, telefono, nombre, apellido):
      self.telefono = telefono
      self.nombre = nombre
      self.apellido = apellido
      self.siguiente = None
      self.anterior = None

   def setSiguiente(self, siguiente):
      self.siguiente = siguiente 

   def getSiguiente(self):
      return self.siguiente

   def setAnterior(self, anterior):
      self.anterior = anterior

   def getAnterior(self):
      return self.anterior
   
   def getTelefono(self):
      return self.telefono

   def getNombre(self):
      return self.nombre

   def getApellido(self):
      return self.apellido

class ListaDobleAgenda:

   def __init__(self):
      self.cabeza = None
      self.size = 0

   def isEmpty(self):
      return self.cabeza == None
   
   def getSize(self):
      return self.size

   def add(self, nodo):
      if self.cabeza == None:#Si la lista esta vacia
         self.cabeza = nodo
      else:
         nodo_aux = self.cabeza
         while nodo_aux.getSiguiente() != None:
            nodo_aux = nodo_aux.getSiguiente() 
         nodo_aux.setSiguiente(nodo)
         nodo.setAnterior(nodo_aux)
      self.size+=1
   
   def buscar(self, telefono):
      nodo_aux = self.cabeza
      while nodo_aux != None:
         if nodo_aux.getTelefono() == telefono:
            return nodo_aux
         nodo_aux = nodo_aux.getSiguiente()
      return None

   def get(self, i):
      if self.cabeza == None:
         return None
      if i >= self.size:
         return None
      nodo_aux = self.cabeza
      for j in range(self.size):
         if j == i:
            return nodo_aux
         nodo_aux = nodo_aux.getSiguiente()

   def imprimir(self):
      for i in range(self.size):
         if i == 0:
            print(f'Ninguno - {self.get(i).nombre} - {self.get(i).getSiguiente().nombre}')
         elif i == self.size-1:
            print(f'{self.get(i).getAnterior().nombre} - {self.get(i).nombre} - Ninguno')
         else:
            print(f'{self.get(i).getAnterior().nombre} - {self.get(i).nombre} - {self.get(i).getSiguiente().nombre}')

         