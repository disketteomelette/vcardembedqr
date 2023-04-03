import pandas as pd
import qrcode
import vobject

# Cargamos el archivo CSV
df = pd.read_csv('datos.csv', sep=';')

# Iteramos sobre cada fila del archivo
for _, row in df.iterrows():
    # Creamos la vCard
    v = vobject.vCard()
    v.add('n').value = vobject.vcard.Name(family=row['apellido'], given=row['nombre'])
    v.add('tel').value = row['telefono']
    v.add('email').value = row['email']
    v.add('org').value = row['compañia']
    v.add('title').value = row['puesto']
    v.add('adr').value = vobject.vcard.Address(street=row['calle'], city=row['ciudad'], code=row['codigopostal'], country=row['pais'])
    v.add('url').value = row['paginaweb']

    # Creamos el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(v.serialize())
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Guardamos la imagen
    filename = f"{row['nombre']}_{row['apellido']}.jpg"
    img.save(filename)