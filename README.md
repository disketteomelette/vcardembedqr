# vcardembedqr
Generates vCards and QR codes from a CSV file with contact information

The following code in Python reads a CSV file containing data for creating a vCard, with fields corresponding to "name;last name;phone;email;company;position;street;city;postal code;country;website". For each row in the CSV file, a vCard is created using the vobject library and then a QR code is generated using the qrcode library. The QR code is saved as a JPG file in the same directory as the script, with the filename being a concatenation of the name and last name fields from the CSV. This code assumes that the CSV file is named "datos.csv" and is located in the same directory as the script. Pandas, vobject, and qrcode libraries need to be installed in order for this code to work properly.
