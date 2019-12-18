import PyPDF2
import io
import docx
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

############################################################
#                #From PDF to Word Document
#                  #Needs more work
#pdfFileObj=open(path,'rb')
#pdfReader=PyPDF2.PdfFileReader(pdfFileObj)

##print(pdfReader.numPages)
#pageObj=pdfReader.getPage(0)

#extText=pageObj.extractText()
#doc=docx.Document()
#doc.add_paragraph(extText,style='List Bullet')
#savepath='C:/Users/Skills/Desktop/demo.docx'
#doc.save(savepath)

#pdfFileObj.close()
#########################################################
#io is a python library for working with streams BytesIo is a buffer


path='C:/Users/Skills/prototype.pdf' #we just save the file path to a variable so we dont type the whole path everytime we need it
packet =io.BytesIO() #
#io stands for input/output

##### creating a new pdf file with report lab #########
can=canvas.Canvas(packet,pagesize=letter)
can.drawString(200,800,"Chapter 1")
can.save()


###### we move to the beginning of the StringIO Buffer ########
packet.seek(0)
new_pdf=PyPDF2.PdfFileReader(packet)


####### here we read the existing pdf in which we want to print the new text #########
existing_pdf=PyPDF2.PdfFileReader(open(path,'rb'))
output=PyPDF2.PdfFileWriter()

######## we add the text(which is the new_pdf) to the existing pdf ########
page=existing_pdf.getPage(0)
page.mergePage(new_pdf.getPage(0))
output.addPage(page)

######## here we save the new merged pdf file to a new real file (we use the word real because until this line everything was inside buffer) #######
outputStream=open('C:/Users/Skills/Desktop/destination2.pdf','wb')
output.write(outputStream)
outputStream.close()





