var input_field = document.querySelector('.create_post_image_input')
 
var drag_area = document.querySelector('.create_post_area_main_1_container_main_wraper')

var browser_btn = document.querySelector('create_post_area_upload_btn')

browser_btn.addEventListener('click',()=>{
    input_field.value = ''
    input_field.click();
})
input_field.addEventListener('change',(e)=>{
    file = this.files[0];
    fileHandler(file)
})

const fileHandler = (file)=>{
    const fileReader = new FileReader();
    fileReader.onload = ()=>{
        const fileURL = fileReader.result;
        let imgTag = `<img src=${fileURL} alt="">`
        drag_area.innerHTML = imgTag;
    }
}
