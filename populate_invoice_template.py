#! /usr/bin/python

import os
import pdfrw
from pdfrw import PdfReader

INVOICE_TEMPLATE_PATH = './sampleFiles/invoice_template.pdf'
INVOICE_OUTPUT_PATH = './sampleFiles/invoice_template_output.pdf'


ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'


def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    print("Annotations : " + str(annotations))
    for annotation in annotations:
        print("\n\n")
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            print("Required Annotation subtype key: " + str(annotation[SUBTYPE_KEY]))
            if annotation[ANNOT_FIELD_KEY]:
                print("RRRRRR required annot field key ::: " + annotation[ANNOT_FIELD_KEY])
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                print("KEY::: " + str(key))
                if key in data_dict.keys():
                    print("UPdate ME")
                    print(str(pdfrw.PdfDict(V='{}'.format(data_dict[key]))))
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
            else:
                print("%%%%%NOT required annot field key ::: " + annotation[ANNOT_FIELD_KEY])
        else:
            print("****Not required annotation subtype key: " + str(annotation[SUBTYPE_KEY]))
    print(str(pdfrw.PdfDict(V='{}'.format(data_dict[key]))))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)



data_dict = {
   'business_name_1': 'Bostata',
   'customer_name': 'company.io',
   'customer_email': 'joe@company.io',
   'invoice_number': '102394',
   'send_date': '2018-02-13',
   'due_date': '2018-03-13',
   'note_contents': 'Thank you for your business, Joe',
   'item_1': 'Data consulting services',
   'item_1_quantity': '10 hours',
   'item_1_price': '$200/hr',
   'item_1_amount': '$2000',
   'subtotal': '$2000',
   'tax': '0',
   'discounts': '0',
   'total': '$2000',
   'business_name_2': 'Bostata LLC',
   'business_email_address': 'hi@bostata.com',
   'business_phone_number': '(617) 930-4294'
}

if __name__ == '__main__':

    pdf = PdfReader(INVOICE_TEMPLATE_PATH)
    print(pdf.keys())
    print(pdf.Info)
    print(pdf.Root.keys())
    print('PDF has {} pages'.format(len(pdf.pages)))
    print('\n\n******\n\n')
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)