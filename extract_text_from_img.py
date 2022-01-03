import ocrspace
api = ocrspace.API(api_key='355d8c6d3788957',
                   language=ocrspace.Language.English)
TEST_FILENAME = 'test.jpg'
print(api.ocr_file(open(TEST_FILENAME, 'rb')))
