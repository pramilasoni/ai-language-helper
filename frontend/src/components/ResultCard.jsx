function ResultCard({ result, loading }) {

  return (
    <div className="result-box">

      <h3>AI Result</h3>

      {loading && (
        <p>Processing your audio...</p>
      )}

      {result && (
        <>
          <div className="result-section">

            <strong>Transcribed Text</strong>

            <p>{result.transcribed_text}</p>

          </div>

          <div className="result-section">

            <strong>AI Response</strong>

            <p>
              {result.response.result_text}
            </p>

          </div>

          <audio
            key={result.audio_response_url}
            controls
            autoPlay
          >
            <source
              src={`${import.meta.env.VITE_API_BASE_URL}${result.audio_response_url}`}
              type="audio/mpeg"
            />
          </audio>
        </>
      )}
    </div>
  );
}

export default ResultCard;