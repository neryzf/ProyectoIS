const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn=> modalBtn.addEventListener('click', ()=>{
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-quiz')

    modalBody.innerHTML =`
    <div class="h5 mb-3">
        esta seguro que quiere iniciar con "<b>${name}</b>"?
    </div>`
    
    startBtn.addEventListener('click',()=>{
        window.location.href = url + pk
    })

}))
