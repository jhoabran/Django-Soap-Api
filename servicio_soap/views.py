from typing import Optional

from spyne import Application, ServiceBase, String, rpc
from spyne.error import ResourceAlreadyExistsError, ResourceNotFoundError
from spyne.model.complex import ComplexModel, Iterable
from spyne.model.primitive import Integer, Unicode
from spyne.protocol.soap import Soap11

from books.models import Book as BookModel

from .serializers import Book


class MiServicio(ServiceBase):
    @rpc(String, String, _returns=String)
    def metodo1(ctx, parametro1, parametro2):
        return "Hola, " + parametro1 + " y " + parametro2 + "!"
    
    @rpc(String, String, _returns=Iterable(Book))
    def getList(ctx, parametro1, parametro2):
        return BookModel.objects.all()

    @rpc(Integer,_returns=String)
    def getBook(ctx, parametro1):
        books = BookModel.objects.all()
        return "Nombre:"+books[parametro1].nombre+"\n ; Descripción:"+books[parametro1].descripcion
    
    @rpc(String,String,_returns=String)
    def setBook(ctx, parametro1,parametro2):
        new_book = BookModel(nombre=parametro1, descripcion=parametro2)
        new_book.save()
        return "Libro creado exitosamente!."

    @rpc(Integer,_returns=String)
    def deleteBook(ctx, parametro1):
        try:
            book_to_delete = BookModel.objects.get(id=parametro1)
            book_to_delete.delete()
            return "Libro eliminado exitosamente!."
        except BookModel.DoesNotExist:
            return "El libro que intenta eliminar no existe."
    
    @rpc(Integer, String, String, _returns=String)
    def updateBook(ctx, id, nombre, descripcion):
        try:
            book_to_update = BookModel.objects.get(id=id)
        except BookModel.DoesNotExist:
            raise ResourceNotFoundError(f"El libro con el id {id} no existe.")
        
        book_to_update.nombre = nombre
        book_to_update.descripcion = descripcion
        book_to_update.save()
        
        return f"El libro con el id {id} ha sido actualizado."
        




app = Application([MiServicio], 'servicio_soap',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())


# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <ns0:metodo1 xmlns:ns0="servicio_soap">
#       <ns0:parametro1>valor1</ns0:parametro1>
#       <ns0:parametro2>valor2</ns0:parametro2>
#     </ns0:metodo1>
#   </soap:Body>
# </soap:Envelope>

# getBook
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <ns0:getBook xmlns:ns0="servicio_soap">
#       <ns0:parametro1>1</ns0:parametro1>
#     </ns0:getBook>
#   </soap:Body>
# </soap:Envelope>

# setBook
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <ns0:setBook xmlns:ns0="servicio_soap">
#       <ns0:parametro1>Libro de prueba</ns0:parametro1>
#       <ns0:parametro2>Descripcion de Libro de prueba</ns0:parametro2>
#     </ns0:setBook>
#   </soap:Body>
# </soap:Envelope>

# deleteBook
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <ns0:deleteBook xmlns:ns0="servicio_soap">
#       <ns0:parametro1>56</ns0:parametro1>
#     </ns0:deleteBook>
#   </soap:Body>
# </soap:Envelope>

# updateBook
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <ns0:updateBook xmlns:ns0="servicio_soap">
#       <ns0:id>2</ns0:id>
#       <ns0:nombre>Harry Potter y la Piedra filosofal</ns0:nombre>
#       <ns0:descripcion>Descripcion de Harry Potter y la Piedra filosofal</ns0:descripcion>
#     </ns0:updateBook>
#   </soap:Body>
# </soap:Envelope>

#getList
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#   <soap:Body>
#     <ns0:getList xmlns:ns0="servicio_soap">
#       <ns0:parametro1>valor1</ns0:parametro1>
#       <ns0:parametro2>valor2</ns0:parametro2>
#     </ns0:getList>
#   </soap:Body>
# </soap:Envelope>