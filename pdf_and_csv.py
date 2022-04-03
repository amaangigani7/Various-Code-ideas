# import csv

# data = open('csv_one.csv', encoding='utf-8')
# csv_data = csv.reader(data)
#
# data_lines = list(csv_data)
# for i in data_lines[:5]:
#     print(i)

# save to csv

# file_to_output = open('to_save.csv', mode='w', newline='') # mode='a' means append
# csv_writer = csv.writer(file_to_output, delimiter=',')
# csv_writer.writerow(['a', 'b', 'c'])

# PDF  working
# import PyPDF2
#
# f = open('resume.pdf', 'rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# # # print(pdf_reader.numPages)
# pdf_text = []
# page_one = pdf_reader.getPage(0)
# pdf_text.append(page_one.extractText())
# print(pdf_text)
# # f.close()
#
# # writing
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(page_one)
#
# pdf_output = open('some.pdf', 'wb')
# pdf_writer.write(pdf_output)
