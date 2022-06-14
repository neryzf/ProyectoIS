
const url = window.location.href
const quizBox = document.getElementById('quiz-box')
const resulQ = document.getElementById('wrapper')





$.ajax({
    type:'GET',
    url: `${url}data`,
    success: function(response){
        console.log(response)
        const data = response.data
        data.forEach(el => {
            for(const[question, answers] of Object.entries(el)){
                quizBox.innerHTML+=`
                <hr>
                <div class = "mb-2">
                <b>${question}</b>
                </div>
                `
                answers.forEach(answer=>{
                    quizBox.innerHTML += `
                    <div>
                        <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                        <h3><label for="${question}">${answer}</label></h3>
                    </div>
                    `
                })
            }
        });

    },
    error: function(error){
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const scores = document.getElementById('result-box')
const resultbox= document.getElementById('score-box')




const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked){
            data[el.name] = el.value
        }else{
            if(!data[el.name])
            {
                data[el.name]= null
            }
        }
    })

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            //console.log(response)
            const results = response.Resultados
            console.log(results)

            resultbox.innerHTML+=`<h2>Tuviste una calificación del ${response.Calificación}% de 100%</h2>`

            results.forEach(res =>{
                const resDiv = document.createElement("div")
                quizForm.remove()
                
                for(const [question, resp] of Object.entries(res)){
                    
                    resDiv.innerHTML+= question
                    const cls = ['container', 'p-3', 'text-light','h1']
                    resDiv.classList.add(...cls)

                    if(resp=='Respuesta_Incorrecta'){
                        resDiv.innerHTML += '- Sin Resultados'
                        resDiv.classList.add('bg-danger')
                    }
                    else{
                        const answer = resp['Respuesta']
                        resDiv.classList.add('bg-success')
                        resDiv.innerHTML+= ` Respuesta: ${answer}`                        
                    }

                }              
                //const body = document.getElementsByTagName('BODY')[0]
                scores.append(resDiv)
            })
        },
        error: function(error){
            console.log(error)
        }

    })
}

quizForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
})