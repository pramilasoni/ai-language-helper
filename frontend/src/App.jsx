import { useRef, useState } from "react";

import "./App.css";

import ModeSelector from "./components/ModeSelector";
import RecordingButton from "./components/RecordingButton";
import ResultCard from "./components/ResultCard";
import HistoryList from "./components/HistoryList";
import { processVoice } from "/api/languageApi";

function App() {
    const mediaRecorderRef = useRef(null);

    const audioChunksRef = useRef([]);
    
    const [mode, setMode] =
      useState("translation");
    
    const [sourceLanguage,
      setSourceLanguage] =
      useState("Danish");
    
    const [targetLanguage,
      setTargetLanguage] =
      useState("English");
    
    const [practiceLanguage,
      setPracticeLanguage] =
      useState("Danish");
    
    const [history, setHistory] =
      useState([]);
    
    const [isRecording,
      setIsRecording] =
      useState(false);
    
    const [result, setResult] =
      useState(null);
    
    const [loading, setLoading] =
      useState(false);

  const startRecording = async () => {
    try {
      setResult(null);

      const stream =
        await navigator.mediaDevices.getUserMedia({
          audio: true,
        });

      const mediaRecorder = new MediaRecorder(stream);

      mediaRecorderRef.current = mediaRecorder;
      audioChunksRef.current = [];

      mediaRecorder.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      mediaRecorder.start();
      setIsRecording(true);
    } catch (error) {
      console.error("Microphone access error:", error);
    }
  };

  const stopRecording = () => {
    mediaRecorderRef.current.stop();

    mediaRecorderRef.current.onstop = async () => {
      const audioBlob = new Blob(audioChunksRef.current, {
        type: "audio/webm",
      });

      try {
        setResult(null);
        setLoading(true);

        const data = await processVoice(
          audioBlob,
          mode,
          sourceLanguage,
          targetLanguage,
          practiceLanguage
        );

        setResult(data);
        setHistory((prev) => [data, ...prev]);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    setIsRecording(false);
  };

  return (
    <div className="app-container">
      <div className="card">
        <h1>AI Language Helper</h1>

        <p className="subtitle">
          Speak, improve your sentence, or translate it into another language.
        </p>

        <ModeSelector
          mode={mode}
          setMode={setMode}
          sourceLanguage={sourceLanguage}
          setSourceLanguage={setSourceLanguage}
          targetLanguage={targetLanguage}
          setTargetLanguage={setTargetLanguage}
          practiceLanguage={practiceLanguage}
          setPracticeLanguage={setPracticeLanguage}
        />

        <RecordingButton
          loading={loading}
          isRecording={isRecording}
          startRecording={startRecording}
          stopRecording={stopRecording}
        />

        {isRecording && (
          <p className="recording-text">
            Recording in progress...
          </p>
        )}

        <ResultCard result={result} loading={loading} />

        <HistoryList history={history} />
      </div>
    </div>
  );
}

export default App;