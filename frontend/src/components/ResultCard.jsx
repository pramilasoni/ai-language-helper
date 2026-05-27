function ResultCard({ result, loading }) {
  const API_BASE_URL =
    import.meta.env.VITE_API_BASE_URL ||
    "http://127.0.0.1:8000";

  return (
    <div className="result-card">
      <h3>AI Result</h3>

      {loading && <p>Processing your audio...</p>}

      {result && (
        <>
          <h4>Original Text</h4>
          <p>{result.original_text || result.transcribed_text}</p>

          <h4>Corrected Text</h4>
          <p>{result.corrected_text}</p>

          {result.english_translation && (
            <>
              <h4>English Translation</h4>
              <p>{result.english_translation}</p>
            </>
          )}

          {result.translated_text && (
            <>
              <h4>Translation</h4>
              <p>{result.translated_text}</p>
            </>
          )}

          {result.score !== undefined && (
            <div className="score-container">
              <div className="score-ring">
                <svg width="140" height="140">
                  <circle
                    className="score-ring-bg"
                    cx="70"
                    cy="70"
                    r="54"
                  />

                  <circle
                    className="score-ring-progress"
                    cx="70"
                    cy="70"
                    r="54"
                    style={{
                      strokeDasharray: 339.3,
                      strokeDashoffset:
                        339.3 -
                        (339.3 * result.score) / 100,
                    }}
                  />
                </svg>

                <div className="score-text">
                  {result.score}
                </div>
              </div>
            </div>
          )}

          {result.feedback && result.feedback.length > 0 && (
            <>
              <h4>Feedback</h4>
              <ul>
                {result.feedback.map((item, index) => (
                  <li key={index}>
                    <strong>{item.issue}</strong>:{" "}
                    {item.suggestion}
                  </li>
                ))}
              </ul>
            </>
          )}

          {result.audio_response_url && (
            <>
              <h4>Audio</h4>
              <audio
                controls
                src={`${API_BASE_URL}${result.audio_response_url}`}
              />
            </>
          )}
        </>
      )}
    </div>
  );
}

export default ResultCard;