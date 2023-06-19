from django.db import migrations


def add_examples(apps, schema_editor):

    # CATEGORIES
    Category = apps.get_model('ecommerce', 'Category')

    computacion = Category(
        name='Computación',
        parent=None,
        slug='computacion'
    )
    computacion.save()

    monitor = Category(
        name='Monitor',
        parent=computacion,
        slug='monitor'
    )
    monitor.save()

    led = Category(
        name='Led',
        parent=monitor,
        slug='led'
    )
    led.save()

    consolas_y_videojuegos = Category(
        name='Consolas y videojuegos',
        parent=None,
        slug='consolas_y_videojuegos'
    )
    consolas_y_videojuegos.save()

    consolas = Category(
        name='Consolas',
        parent=consolas_y_videojuegos,
        slug='consolas'
    )
    consolas.save()

    muebles = Category(
        name='Muebles',
        parent=None,
        slug='muebles'
    )
    muebles.save()

    sillas = Category(
        name='Sillas',
        parent=muebles,
        slug='sillas'
    )
    sillas.save()
    
    smartphones = Category(
        name='Smartphones',
        parent=None,
        slug='smartphones'
    )
    smartphones.save()
    

    # TAGS
    Tag = apps.get_model('ecommerce', 'Tag')

    apple = Tag(
        name='Apple',
        slug='apple'
    )
    apple.save()
    
    iphone = Tag(
        name='Iphone',
        slug='iphone'
    )
    iphone.save()
    
    motorola = Tag(
        name='Motorola',
        slug='motorola'
    )
    motorola.save()
    
    asus = Tag(
        name='Asus',
        slug='asus'
    )
    asus.save()
    
    samsung = Tag(
        name='Samsung',
        slug='samsung'
    )
    samsung.save()
    
    xbox = Tag(
        name='Xbox',
        slug='xbox'
    )
    xbox.save()
    
    microsoft = Tag(
        name='Microsoft',
        slug='microsoft'
    )
    microsoft.save()
    
    gamer = Tag(
        name='Gamer',
        slug='gamer'
    )
    gamer.save()
    
    negro = Tag(
        name='Negro',
        slug='negro'
    )
    negro.save()
    
    intel = Tag(
        name='Intel',
        slug='intel'
    )
    intel.save()
    
    lenovo = Tag(
        name='Lenovo',
        slug='lenovo'
    )
    lenovo.save()
    
    azul = Tag(
        name='Azul',
        slug='azul'
    )
    azul.save()
    
    xiaomi = Tag(
        name='Xiaomi',
        slug='xiaomi'
    )
    xiaomi.save()
    

    # PRODUCTS
    Product = apps.get_model('ecommerce', 'Product')

    product1 = Product(
        name='Xiaomi Redmi Note 11 (Snapdragon) Dual SIM 128 GB azul estelar 4 GB RAM',
        description='Dispositivo liberado para que elijas la compañía telefónica que prefieras. Pantalla AMOLED de 6.43. Tiene 4 cámaras traseras de 50Mpx / 8Mpx / 2Mpx / 2Mpx. Cámara delantera de 13Mpx. Procesador Snapdragon 680 Octa-Core de 2.4GHz con 4GB de RAM. Batería de',
        price=100999,
        on_sale=True,
        stock='2',
        category=smartphones,
    )
    product1.save()
    product1.tag.add(xiaomi, azul)
    
    product2 = Product(
        name='Notebook Lenovo Ideapad I7 1165g7 8gb 512gb Pantalla 14 Full Hd Windows 11 Home',
        description='Procesador Intel Core i7. Memoria RAM de 8GB. La duración de la batería depende del uso que se le dé al producto.',
        price=362999.00,
        on_sale=True,
        stock='1',
        category=computacion,
    )
    product2.save()
    product2.tag.add(lenovo, intel)

    product3 = Product(
        name='Silla de escritorio Xtrike Me GC-905 gamer ergonómica azul y negro con tapizado de cuero sintético',
        description='Confortable y duradera. Posee altura ajustable. Cómodos apoyabrazos. Soporte lumbar regulable. Tiene apoya cabeza. Con ruedas. Giratoria. Peso máximo soportado: 135 kg. Medidas del asiento: 53 cm de ancho, 44 cm de altura mínima desde el piso, 54 cm de al',
        price=62853.00,
        on_sale=True,
        stock='1',
        category=muebles,
    )
    product3.save()
    product3.tag.add(negro, azul, gamer)

    product4 = Product(
        name='Microsoft Xbox Series X 1TB Standard color negro con joystick inalámbrico',
        description='Incluye control. Resolución de 2560px x 1440px. Memoria RAM de 16GB. Cuenta con: 1 cable hdmi, 1 cable de alimentación ca. La duración de la batería de los controles depende del uso que se le dé al producto.',
        price=359999.00,
        on_sale=False,
        stock='4',
        category=consolas,
    )
    product4.save()
    product4.tag.add(negro, gamer, microsoft, xbox)

    product5 = Product(
        name='Monitor Gamer Samsung F24t35 Led 24 Full Hd Full HD Widescreen 16:9',
        description='Alto 42.5. Ancho 53.9. Color NEGRO. Modelo LF24T350FH. Origen ARGENTINA. Peso 2.7. Profundidad 23.2. Brillo 250 CD/M2. Formato de pantalla WIDESCREEN 16:9. Frecuencia Vert. 60. Radio de contraste 1000 A 1. Tiempo de respuesta 5',
        price=57799.00,
        on_sale=True,
        stock='10',
        category=led,
    )
    product5.save()
    product5.tag.add(negro, gamer, samsung)

    product6 = Product(
        name='Samsung Galaxy A54 5g 256gb 8gb Ram Awesome Graphite',
        description='Dispositivo liberado para que elijas la compañía telefónica que prefieras. Compatible con redes 5G. Pantalla de 6.4". Cámara delantera de 32Mpx. Batería de 5000mAh. Memoria interna de 256GB.',
        price='226999,00',
        on_sale=False,
        stock='4',
        category=smartphones,
    )
    product6.save()
    product6.tag.add(negro, samsung)

    product7 = Product(
        name='Apple iPhone 13 (128 GB) - Azul medianoche',
        description='Pantalla Super Retina XDR de 6.1 pulgadas.(1) Modo Cine con baja profundidad de campo y cambios de enfoque automáticos en tus videos. Sistema avanzado de dos cámaras de 12 MP (gran angular y ultra gran angular) con Estilos Fotográficos, HDR Inteligente 4,',
        price='484157,00',
        on_sale=False,
        stock='0',
        category=smartphones,
    )
    product7.save()
    product7.tag.add(iphone, apple, azul)

    product8 = Product(
        name='Moto E22 32gb 3gb Ram Azul',
        description='Dispositivo liberado para que elijas la compañía telefónica que prefieras. Memoria interna de 32GB.',
        price='46400,00',
        on_sale=False,
        stock='10',
        category=smartphones,
    )
    product8.save()
    product8.tag.add(azul, motorola)

    product9 = Product(
        name='Samsung Galaxy A04 128 GB negro 4 GB RAM',
        description='Dispositivo liberado para que elijas la compañía telefónica que prefieras. Pantalla PLS de 6.5". Tiene 2 cámaras traseras de 50Mpx/2Mpx. Cámara delantera de 5Mpx. Batería de 5000mAh. Memoria interna de 128GB. Con reconocimiento facial.',
        price='79999,00',
        on_sale=True,
        stock='10',
        category=smartphones,
    )
    product9.save()
    product9.tag.add(negro, samsung)

    product10 = Product(
        name='Monitor gamer Asus VP228HE led 21.5" negro 100V/240V',
        description='Pantalla led de 21.5". Tiene una resolución de 1920px-1080px. Relación de aspecto de 16:9. Panel TN. Su brillo es de 200cd/m². Tipos de conexión: HDMI 1.4, VGA/D-Sub, Jack 3.5 mm. Altavoces incluidos. Comodidad visual en todo momento.',
        price=56999.00,
        on_sale=False,
        stock='5',
        category=led,
    )
    product10.save()
    product10.tag.add(negro, gamer, asus)


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(add_examples),
    ]