import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ||
  "http://127.0.0.1:8000";

export async function processVoice(
  audioBlob,
  mode,
  sourceLanguage,
  targetLanguage,
  practiceLanguage
) {
  const formData = new FormData();

  formData.append(
    "file",
    audioBlob,
    "recording.webm"
  );

  // -------------------------
  // Translation Mode
  // -------------------------
  if (mode === "translation") {

    formData.append(
      "source_language",
      sourceLanguage
    );

    formData.append(
      "target_language",
      targetLanguage
    );

    const response = await axios.post(
      `${API_BASE_URL}/voice-translate`,
      formData,
      {
        headers: {
          "Content-Type":
            "multipart/form-data",
        },
      }
    );

    return response.data;
  }

  // -------------------------
  // Perfection Mode
  // -------------------------
  if (mode === "perfection") {

    formData.append(
      "practice_language",
      practiceLanguage
    );

    const response = await axios.post(
      `${API_BASE_URL}/voice-perfect`,
      formData,
      {
        headers: {
          "Content-Type":
            "multipart/form-data",
        },
      }
    );

    return response.data;
  }

  throw new Error("Invalid mode");
}