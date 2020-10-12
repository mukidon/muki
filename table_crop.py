import tabula
df = tabula.read_pdf("C:/Users/New/Downloads/input.pdf", pages='all')
tabula.convert_into("C:/Users/New/Downloads/input.pdf", "C:/Users/New/Desktop/output.csv", output_format="csv", pages='all')
print (df)