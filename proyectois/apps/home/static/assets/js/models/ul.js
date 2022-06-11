export class UI {
    constructor() { }

    /**
     * 
     * @param {String} text 
     */
    showQuestion(text) {
        const questionTitle = document.getElementById('question');
        questionTitle.innerText = text;

    }
    /**
     * 
     * @param {string[]} choices 
     */
    showChoices(choices, callback) {
        const choicesConteiner = document.getElementById('choices')
        choicesConteiner.innerHTML =''

        for (let i = 0; i < choices.length; i++) {
            const button = document.createElement('button');
            button.innerText = choices[i];
            button.className = 'button';
            button.addEventListener("click",()=> callback(choices[i]));

            choicesConteiner.append(button);
        }
    }
    /**
     * 
     * @param {number} scores 
     * @param {number} total 
     */
    showScores(scores, total){
        const quizEndHtml = `
        <h1>Resultado<h1/> 
        <h2 id="progress">Tu resultado: ${scores} de ${total}</h2>`;
        const element = document.getElementById('quiz');
        element.innerHTML =quizEndHtml;

    }
    /**
     * 
     * @param {number} currentIndex 
     * @param {number} total 
     */

    showProgress(currentIndex, total){
        const element =document.getElementById('progress');
        element.innerHTML = `Pregunta ${currentIndex+1} de ${total}`;
    }

}