import { newQuestion } from './data/questions.js';
import { Quiz } from './models/quiz.js';
import { UI } from "./models/ul.js";


/**
 * 
 * @param {Quiz} quiz 
 * @param {UI} ui 
 */
const renderPage = (quiz, ui) => {
    if (quiz.isEnded()) {
        console.log(quiz.score);
        ui.showScores(quiz.score,quiz.preguntas.length);

    } else {
        ui.showQuestion(quiz.getQuestionIndex().text);
        ui.showChoices(quiz.getQuestionIndex().choices, (currentChoice) => {
            quiz.guess(currentChoice);
            renderPage(quiz, ui);
        });
        ui.showProgress(quiz.questionIndex,quiz.preguntas.length);
    }
}


function main() {

    
    const quiz = new Quiz(newQuestion);
    const ui = new UI();
    
    renderPage(quiz, ui);
}

main()

