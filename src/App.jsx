import { useState } from "react";
import QuestionForm from "./components/qaForm";

export default function Home() {
  const [url, setUrl] = useState("");
  const [uploadedFile, setUploadedFile] = useState(null);
  const [questionType, setQuestionType] = useState("Multiple Choice Questions");
  const [numQuestions, setNumQuestions] = useState(1);
  const [difficulty, setDifficulty] = useState("Easy");
  const [isLoading, setIsLoading] = useState(false);
  const [showQuestions, setShowQuestions] = useState(false);
  const [questionArray, setQuestionArray] = useState([]);

  // Handle file upload
  const handleFileChange = (event) => {
    setUploadedFile(event.target.files[0]);
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    setIsLoading(true);
    e.preventDefault();
    // Perform API call to generate quiz
    const response = await fetch("http://localhost:3000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        pdfPath: "/home/mohamed/Downloads/macbeth.pdf",
        startPage: "15",
        endPage: "17",
        questionCount: "10",
        difficulty: "Easy",
      }),
    });
    setIsLoading(false);
    setShowQuestions(true)
    const results = await response.json();
    setQuestionArray(results.questions);
  };

  return (
    <div className="dark:bg-gray-900 h-screen flex items-center justify-center">
      {isLoading ? (
        <h2 className="text-white text-4xl">LOADING...</h2>
      ) : showQuestions ? <QuestionForm questions={questionArray}/> : (
        <div className="container mx-auto p-4 text-white max-w-2xl">
          <h1 className="text-4xl font-bold mb-6 text-center">
            Welcome to <span className="text-green-400">Quizmify</span> your AI
            Learning Companion
          </h1>

          <form className="space-y-6" onSubmit={handleSubmit}>
            {/* URL Input */}
            <div>
              <input
                type="text"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                placeholder="Enter a URL you would like to know more about"
                className="w-full p-3 rounded bg-gray-700 text-white placeholder-gray-400"
              />
            </div>

            {/* File Uploader */}
            <div>
              <label className="block w-full bg-gray-700 rounded p-3 cursor-pointer text-center">
                <span className="text-sm text-gray-300">
                  Upload Your PDF Document Here!
                </span>
                <input
                  type="file"
                  onChange={handleFileChange}
                  className="hidden"
                  accept=".pdf"
                />
              </label>
            </div>

            {/* Question Type Selector */}
            <div>
              <select
                value={questionType}
                onChange={(e) => setQuestionType(e.target.value)}
                className="w-full p-3 rounded bg-gray-700 text-white"
              >
                <option>Multiple Choice Questions</option>
                <option>Free Response Questions</option>
              </select>
            </div>

            {/* Number of Questions Selector */}
            <div>
              <input
                type="number"
                value={numQuestions}
                onChange={(e) => setNumQuestions(e.target.value)}
                min="1"
                max="20"
                className="w-full p-3 rounded bg-gray-700 text-white"
              />
            </div>

            {/* Difficulty Selector */}
            <div>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="w-full p-3 rounded bg-gray-700 text-white"
              >
                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>
              </select>
            </div>

            {/* Submit Button */}
            <div>
              <button
                type="submit"
                className="w-full p-3 rounded bg-green-600 hover:bg-green-500 text-white font-bold"
              >
                Generate Quiz
              </button>
            </div>
          </form>
        </div>
      )}
    </div>
  );
}
