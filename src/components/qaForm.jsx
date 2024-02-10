import { useState } from "react";

const QuestionForm = ({ questions }) => {
  console.log(questions);
  return (
    <div className="flex flex-col w-[640px]">
      <h1 className="text-4xl font-bold mb-6 text-center text-green-500">
        Good luck!
      </h1>
      {questions.map((question, i) => {
        return (
          <form
            onSubmit={(e) => handleSubmit(e)}
            className="flex flex-col gap-4 p-4 rounded-2xl bg-pale"
          >
            <p className="text-2xl font-bold text-white">{question}</p>
            <textarea
              className="p-3 rounded-lg flex-auto resize-none"
              placeholder="Body"
              type="text"
              onChange={(e) => setBody(e.target.value)}
            />
            <div className="flex justify-end">
              <button
                onSubmit={(e) => handleSubmit(e)}
                type="submit"
                className="fefont-semibold rounded-full text-jet bg-green-500 px-4 py-2 hover:bg-green-400"
              >
                Check
              </button>
            </div>
          </form>
        );
      })}
    </div>
  );
};

export default QuestionForm;
