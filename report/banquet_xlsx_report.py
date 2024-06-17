class BanquetXlsxReport(models.AbstractModel):
    _name = 'report.banquet.management.banquet_report_excel'
    _inherit = 'report.report_xlsx.abstract'


def generate_xlsx_report(self, workbook, data, banquet):
    # Define formats
    bold = workbook.add_format({'bold': True})
    date_format = workbook.add_format({'num_formats': 'yyyy-mm-dd'})

    # Add a worksheet
    sheet = workbook.add_worksheet('Banquet Report')

    # Define headers
    headers = ['Name', 'Date', 'Location', 'Attendees', 'Notes']
    for col, header in enumerate(headers):
        sheet.write(1, col, header, bold)

    # Write data rows
    row = 2
    col = 0
    for obj in banquet:
        sheet.write(row, col, obj.name or '')
        sheet.write(row, col + 1, obj.date or '', date_format)
        sheet.write(row, col + 2, obj.location or '')
        sheet.write(row, col + 3, obj.attendees or 0)
        sheet.write(row, col + 4, obj.notes or '')
        row += 1
