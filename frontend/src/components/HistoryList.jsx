function HistoryList({ history }) {
  if (!history.length) {
    return null;
  }

  return (
    <div className="history-list">
      <h3>History</h3>

      {history.map((item, index) => (
        <div
          key={index}
          className="history-item"
        >
          <p>
            <strong>Original:</strong>{" "}
            {item.original_text ||
              item.transcribed_text}
          </p>

          <p>
            <strong>Corrected:</strong>{" "}
            {item.corrected_text}
          </p>

          {item.english_translation && (
            <p>
              <strong>English:</strong>{" "}
              {item.english_translation}
            </p>
          )}

          {item.translated_text && (
            <p>
              <strong>Translation:</strong>{" "}
              {item.translated_text}
            </p>
          )}

          {item.score !== undefined && (
            <p>
              <strong>Score:</strong>{" "}
              {item.score}/100
            </p>
          )}
        </div>
      ))}
    </div>
  );
}

export default HistoryList;