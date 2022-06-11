import {Question} from './question.js'
export class Quiz{

    questionIndex =0
    score =0
    /**
     * 
     * @param {Question[]} preguntas 
     */

    constructor(preguntas){
        this.preguntas =preguntas;
    }
    
    /**
     * 
     * @returns {Question}
     */
    getQuestionIndex(){
        return this.preguntas[this.questionIndex]
    }
    isEnded(){
        return this.preguntas.length === this.questionIndex
    }

    /**
     * 
     * @param {String} respuesta 
     */
    guess(respuesta){
        if(this.getQuestionIndex().correctAnswer(respuesta))
        {
            this.score++
        }
        this.questionIndex++
    }


}