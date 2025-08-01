import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")
summary = df.describe()

# Save a chart
plt.figure(figsize=(6,4))
df['column_name'].plot(kind='hist')
plt.title('Distribution')
plt.savefig('chart.png')

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, "Automated Report", ln=True, align='C')
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, str(summary))
pdf.image('chart.png', x=10, y=100, w=180)
pdf.output("report.pdf")