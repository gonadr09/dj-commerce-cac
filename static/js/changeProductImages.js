product_images = document.querySelectorAll('.product_images')
main_image = document.querySelector('#main_image')

product_images.forEach( product_image => {
    product_image.addEventListener('click', (e) => {
        main_image.src = product_image.src
    })
})