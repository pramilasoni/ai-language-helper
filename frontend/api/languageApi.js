import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;


export const processVoice = async (
  audioBlob,
  mode,
  targetLanguage
) => {

  const formData = new FormData();

  formData.append("file", audioBlob, "recording.webm");

  formData.append("mode", mode);


    if (mode === "translate" || mode === "auto") {
      formData.append("target_language", targetLanguage);
    }

  const response = await axios.post(
    `${API_BASE_URL}/voice-process`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};