const target_form = document.querySelector('.jss_content_form')
const counted_text = document.querySelector('.counted_text')

target_form.addEventListener(
    "keyup", function() {
        counted_text.innerHTML = target_form.value.length
    }
)