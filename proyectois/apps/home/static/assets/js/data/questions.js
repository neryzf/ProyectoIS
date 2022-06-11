import { Question } from "../models/question.js";
import { data } from "./data.js";

export const newQuestion = data.map(question => new Question(question.question, question.choice, question.answer))

